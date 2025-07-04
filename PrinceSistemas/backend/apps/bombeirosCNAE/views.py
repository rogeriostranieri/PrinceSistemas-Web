# views.py para bombeirosCNAE
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import BombeiroCNAE
import json
import logging
import traceback

logger = logging.getLogger(__name__)

@csrf_exempt
def lista_bombeiros_cnae(request):
    """Endpoint para consulta de CNAEs relacionados a bombeiros."""
    
    # Permitir CORS para desenvolvimento
    if request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
        
    # Adicionar cabeçalhos CORS à resposta
    def cors_response(data, status=200):
        response = JsonResponse(data, safe=False, status=status)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    if request.method == 'POST':
        try:
            # Log da requisição recebida
            logger.info(f"Recebendo POST em /bombeiros-cnae/")
            
            # Processar o corpo da requisição
            body = request.body.decode('utf-8')
            logger.info(f"Corpo da requisição: {body}")
            
            # Parse do JSON
            data = json.loads(body)
            cnaes = data.get('cnaes', [])
            
            # Validação do formato
            if not isinstance(cnaes, list):
                return cors_response({'erro': 'Campo cnaes deve ser uma lista.'}, status=400)
            
            # Caso lista vazia
            if not cnaes:
                return cors_response([], status=200)
                
            # Log dos CNAEs recebidos
            logger.info(f"CNAEs para buscar: {cnaes}")
            
            # Normalização dos CNAEs para busca
            import re
            logger.info(f"CNAEs brutos recebidos: {cnaes}")
            
            # Busca flexível: normaliza para comparação (remove espaços, pontos, hífen e barras)
            cnaes_normalizados = []
            for c in cnaes:
                # Limpa e normaliza o CNAE
                c_strip = c.strip()
                c_norm = c_strip.replace(' ', '').replace('.', '').lower()
                cnaes_normalizados.append(c_norm)
                # Também adicionamos versão sem hífen e barra para maior flexibilidade
                cnaes_normalizados.append(c_norm.replace('-', '').replace('/', ''))
            
            logger.info(f"CNAEs normalizados para busca: {cnaes_normalizados}")
            
            # Consulta ao banco
            try:
                # Primeiro verificamos se a tabela tem registros
                count = BombeiroCNAE.objects.count()
                logger.info(f"Quantidade de registros na tabela: {count}")
                
                # Realizamos a busca
                qs = BombeiroCNAE.objects.all()
                resultado = []
                
                # Processamos cada registro
                for obj in qs:
                    # Pegar o CNAE do banco e normalizar também
                    cnae_original = obj.cnae or ''
                    if not cnae_original:
                        continue
                    
                    # Normalização do CNAE do banco para comparação
                    cnae_norm = cnae_original.strip().replace(' ', '').replace('.', '').lower()
                    cnae_sem_pontuacao = cnae_norm.replace('-', '').replace('/', '')
                    
                    # Fazer a comparação com todas as normalizações
                    match_encontrado = False
                    for c_norm in cnaes_normalizados:
                        if cnae_norm == c_norm or cnae_sem_pontuacao == c_norm:
                            match_encontrado = True
                            logger.info(f"Match encontrado: '{c_norm}' corresponde a '{cnae_original}'")
                            break
                    
                    if match_encontrado:
                        resultado.append({
                            'ocupacao': obj.ocupacao,
                            'descricao': obj.descricao,
                            'divisao': obj.divisao,
                            'cnae': obj.cnae,
                            'carga_de_incendio': obj.carga_de_incendio
                        })
                
                # Log do resultado
                logger.info(f"Registros encontrados: {len(resultado)}")
                return cors_response(resultado)
                
            except Exception as db_error:
                # Log de erro específico do banco de dados
                logger.error(f"Erro de banco de dados: {str(db_error)}")
                return cors_response({
                    'erro': 'Erro ao consultar o banco de dados',
                    'detalhe': str(db_error),
                    'traceback': traceback.format_exc()
                }, status=400)
                
        except json.JSONDecodeError as json_error:
            # Erro de parsing do JSON
            logger.error(f"Erro ao decodificar JSON: {str(json_error)}")
            return cors_response({
                'erro': 'Formato JSON inválido', 
                'detalhe': str(json_error),
                'body': request.body.decode('utf-8')
            }, status=400)
            
        except Exception as e:
            # Erro genérico
            logger.error(f"Erro não esperado: {str(e)}")
            return cors_response({
                'erro': str(e), 
                'traceback': traceback.format_exc(), 
                'body': request.body.decode('utf-8')
            }, status=400)
            
    elif request.method == 'GET':
        # Retorna todos os registros para visualização rápida no navegador
        try:
            qs = BombeiroCNAE.objects.all()
            resultado = list(qs.values('ocupacao', 'descricao', 'divisao', 'cnae', 'carga_de_incendio'))
            return cors_response(resultado)
        except Exception as e:
            logger.error(f"Erro ao obter todos os registros: {str(e)}")
            return cors_response({
                'erro': str(e), 
                'traceback': traceback.format_exc()
            }, status=400)
            
    # Método não permitido
    return cors_response({'erro': 'Método não permitido'}, status=405)
