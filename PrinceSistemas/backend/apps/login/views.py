import json
import logging
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Login
from .serializers import LoginSerializer
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password, check_password
import uuid  # Importar uuid para geração de token

logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["POST"])
def login_view(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        logger.info(f"Tentativa de login para usuário: {username}")

        if not username or not password:
            return JsonResponse({"error": "Campos 'username' e 'password' são obrigatórios."}, status=400)
        
        try:
            user = Login.objects.get(usuario=username)
        except Login.DoesNotExist:
            logger.info("Usuário não encontrado")
            return JsonResponse({"error": "Usuário não encontrado."}, status=404)
        
        if user.senha != password:
            logger.info(f"Senha incorreta para o usuário {username}")
            return JsonResponse({"error": "Senha incorreta."}, status=401)
        
        # Gerar um token simples (em produção use JWT)
        token = str(uuid.uuid4())
        
        # Retorne o nome completo e mais informações
        fullName = user.nome_completo or user.usuario
        return JsonResponse({
            "success": True,
            "message": f"Bem-vindo, {fullName}!",
            "token": token,
            "id_login": user.id_login,
            "usuario": user.usuario,
            "nome_completo": fullName,
            "email": user.email,
            "nivel_acesso": user.nivel_acesso
        })
    
    except Exception as e:
        logger.exception("Erro durante a autenticação")
        return JsonResponse({"error": "Erro no servidor: " + str(e)}, status=500)

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        try:
            data = request.data
            username = data.get('username')
            password = data.get('password')
            logger.info(f"Tentativa de login para usuário: {username}")

            if not username or not password:
                return Response({"error": "Campos 'username' e 'password' são obrigatórios."}, status=400)
            
            try:
                user = Login.objects.get(usuario=username)
            except Login.DoesNotExist:
                logger.info("Usuário não encontrado")
                return Response({"error": "Usuário não encontrado."}, status=404)
            
            if user.senha != password:
                logger.info(f"Senha incorreta para o usuário {username}")
                return Response({"error": "Senha incorreta."}, status=401)
            
            # Retorne o nome completo (ou o usuário, se não houver nome_completo)
            fullName = user.nome_completo or user.usuario
            return Response({
                "message": f"Bem-vindo, {fullName}!",
                "nome_completo": fullName,
                "nivel_acesso": user.nivel_acesso  # Incluir nível de acesso
            })
        
        except Exception as e:
            logger.exception("Erro durante a autenticação")
            return Response({"error": "Erro no servidor: " + str(e)}, status=500)
