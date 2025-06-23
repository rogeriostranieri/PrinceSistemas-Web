from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import re
import logging
import time
from datetime import datetime

logger = logging.getLogger(__name__)

class SecurityMiddleware(MiddlewareMixin):
    """
    Middleware de proteção inteligente - diferencia acessos locais vs externos
    """
    
    # IPs suspeitos conhecidos
    BLOCKED_IPS = [
        '45.82.78.254',
        # Ranges de IPs suspeitos comuns
        '185.220.100.',  # Tor exit nodes
        '185.220.101.',
        '198.98.51.',    # Scanners conhecidos
    ]
    
    # Padrões de User-Agents suspeitos
    BLOCKED_USER_AGENTS = [
        r'.*bot.*', r'.*crawler.*', r'.*spider.*', r'.*scanner.*',
        r'.*hack.*', r'.*nikto.*', r'.*sqlmap.*', r'.*nmap.*',
        r'.*masscan.*', r'.*zmap.*', r'.*nuclei.*'
    ]
    
    # Caminhos suspeitos
    BLOCKED_PATHS = [
        '/admin/login/', '/wp-admin/', '/phpmyadmin/', '/.env',
        '/config/', '/backup/', '/test/', '/setup/', '/install/',
        '/database/', '/db/', '/mysql/', '/postgres/', '/sql/',
        '/.git/', '/composer.json', '/package.json', '/web.config'
    ]

    # Rate limiting diferenciado
    REQUEST_COUNTS = {}
    
    # Bloqueio temporário de IPs
    TEMP_BLOCKED_IPS = {}
    BLOCK_DURATION = 300  # 5 minutos

    def get_rate_limit(self, ip):
        """Rate limit diferenciado: mais permissivo para IPs locais"""
        if self.is_local_ip(ip):
            return 120  # 120 req/min para IPs locais
        elif settings.DEBUG:
            return 60   # 60 req/min em desenvolvimento
        else:
            return 30   # 30 req/min para IPs externos em produção

    def process_request(self, request):
        client_ip = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        path = request.path
        
        # Verificar bloqueio temporário (apenas para IPs externos)
        if not self.is_local_ip(client_ip) and self.is_temporarily_blocked(client_ip):
            logger.warning(f"🚫 IP TEMPORARIAMENTE BLOQUEADO: {client_ip}")
            return JsonResponse({'error': 'IP temporariamente bloqueado'}, status=403)
        
        # Log inteligente: apenas acessos externos ou em produção
        if not self.is_local_ip(client_ip) or settings.PRODUCTION:
            access_type = "LOCAL" if self.is_local_ip(client_ip) else "EXTERNO"
            logger.info(f"Acesso {access_type}: IP={client_ip}, Path={path}, UA={user_agent[:50]}")
        
        # Verificações de segurança (mais rigorosas para IPs externos)
        if not self.is_local_ip(client_ip):
            # Verificações completas para IPs externos
            if self.is_blocked_ip(client_ip):
                return self.block_request(client_ip, "IP bloqueado", path)
                
            if self.is_blocked_user_agent(user_agent):
                return self.block_request(client_ip, "User-Agent suspeito", path, user_agent[:100])
                
            if self.is_blocked_path(path):
                return self.block_request(client_ip, "Caminho suspeito", path)
                
            if self.is_sql_injection_attempt(request):
                return self.block_request(client_ip, "Tentativa SQL Injection", path)
        
        # Rate limiting (aplicado a todos, mas com limites diferentes)
        if self.is_rate_limited(client_ip):
            access_type = "local" if self.is_local_ip(client_ip) else "externo"
            return self.block_request(client_ip, f"Rate limit excedido ({access_type})", path)
        
        return None
    
    def block_request(self, ip, reason, path, extra_info=""):
        # Adicionar IP ao bloqueio temporário (apenas IPs externos)
        if not self.is_local_ip(ip):
            self.add_temp_block(ip)
        
        access_type = "LOCAL" if self.is_local_ip(ip) else "EXTERNO"
        logger.warning(f"🚫 {reason.upper()} ({access_type}): {ip} -> {path} {extra_info}")
        
        return JsonResponse({
            'error': 'Acesso negado',
            'reason': reason,
            'type': access_type.lower(),
            'timestamp': datetime.now().isoformat()
        }, status=403)
    
    def add_temp_block(self, ip):
        """Adicionar IP ao bloqueio temporário"""
        self.TEMP_BLOCKED_IPS[ip] = time.time()
    
    def is_temporarily_blocked(self, ip):
        """Verificar se IP está temporariamente bloqueado"""
        if ip not in self.TEMP_BLOCKED_IPS:
            return False
        
        # Verificar se o tempo de bloqueio expirou
        if time.time() - self.TEMP_BLOCKED_IPS[ip] > self.BLOCK_DURATION:
            del self.TEMP_BLOCKED_IPS[ip]
            return False
        
        return True
    
    def get_client_ip(self, request):
        """Obter IP real do cliente (com proxy support)"""
        # Para nginx/apache com proxy
        real_ip = request.META.get('HTTP_X_REAL_IP')
        if real_ip:
            return real_ip
            
        # Para load balancers
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_for:
            return forwarded_for.split(',')[0].strip()
            
        # CloudFlare
        cf_ip = request.META.get('HTTP_CF_CONNECTING_IP')
        if cf_ip:
            return cf_ip
            
        return request.META.get('REMOTE_ADDR', 'unknown')
    
    def is_local_ip(self, ip):
        """Verificar se é IP local - EXPANDIDO"""
        local_ranges = [
            '127.0.0.1', '::1', 'localhost',
            '0.0.0.0'  # Servidor local
        ]
        return (ip in local_ranges or 
                ip.startswith('192.168.') or 
                ip.startswith('10.') or 
                ip.startswith('172.16.') or
                ip.startswith('172.17.') or
                ip.startswith('172.18.') or
                ip.startswith('172.19.') or
                ip.startswith('172.20.') or
                ip.startswith('172.21.') or
                ip.startswith('172.22.') or
                ip.startswith('172.23.') or
                ip.startswith('172.24.') or
                ip.startswith('172.25.') or
                ip.startswith('172.26.') or
                ip.startswith('172.27.') or
                ip.startswith('172.28.') or
                ip.startswith('172.29.') or
                ip.startswith('172.30.') or
                ip.startswith('172.31.'))
    
    def is_blocked_ip(self, ip):
        """Verificar IP bloqueado"""
        for blocked_ip in self.BLOCKED_IPS:
            if blocked_ip.endswith('.'):
                if ip.startswith(blocked_ip):
                    return True
            elif ip == blocked_ip:
                return True
        return False
    
    def is_blocked_user_agent(self, user_agent):
        """Verificar User-Agent suspeito"""
        if not user_agent or len(user_agent) < 10:
            return True
            
        # Permitir navegadores legítimos
        legitimate_browsers = ['Mozilla', 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera']
        for browser in legitimate_browsers:
            if browser in user_agent:
                return False
        
        # Verificar padrões suspeitos
        for pattern in self.BLOCKED_USER_AGENTS:
            if re.search(pattern, user_agent, re.IGNORECASE):
                return True
        return False
    
    def is_blocked_path(self, path):
        """Verificar caminho suspeito"""
        return any(path.startswith(blocked) for blocked in self.BLOCKED_PATHS)
    
    def is_rate_limited(self, ip):
        """Rate limiting inteligente"""
        current_time = time.time()
        max_requests = self.get_rate_limit(ip)
        
        if ip == "127.0.0.1":
            # Permite muito mais requisições para localhost
            limite = 1000
        else:
            limite = 30  # ou o valor padrão para externos
        
        if ip not in self.REQUEST_COUNTS:
            self.REQUEST_COUNTS[ip] = []
        
        # Limpar requests antigos
        self.REQUEST_COUNTS[ip] = [
            req_time for req_time in self.REQUEST_COUNTS[ip]
            if current_time - req_time < 60
        ]
        
        # Adicionar request atual
        self.REQUEST_COUNTS[ip].append(current_time)
        
        return len(self.REQUEST_COUNTS[ip]) > limite
    
    def is_sql_injection_attempt(self, request):
        """Detectar SQL Injection"""
        suspicious_patterns = [
            r'union\s+select', r'drop\s+table', r'insert\s+into',
            r'delete\s+from', r'update\s+set', r'<script',
            r'javascript:', r'eval\s*\(', r'1=1', r'or\s+1=1'
        ]
        
        # Verificar query string e body
        content = f"{request.META.get('QUERY_STRING', '')} "
        
        if hasattr(request, 'body'):
            try:
                content += request.body.decode('utf-8', errors='ignore')
            except:
                pass
        
        content = content.lower()
        return any(re.search(pattern, content, re.IGNORECASE) for pattern in suspicious_patterns)