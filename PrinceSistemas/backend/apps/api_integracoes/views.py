from django.shortcuts import render
from django.http import JsonResponse
import requests
from datetime import datetime, timedelta
import logging

# Cache simples para armazenar respostas de CNPJs
cnpj_cache = {}

logger = logging.getLogger(__name__)

def consulta_cnpj(request, cnpj):
    """Endpoint global para consulta de CNPJ via ReceitaWS"""
    logger.info(f"Consultando CNPJ: {cnpj}")
    
    # Verifica se o CNPJ está no cache e se é recente (menos de 30 dias)
    if cnpj in cnpj_cache:
        cache_time = cnpj_cache[cnpj]['timestamp']
        if datetime.now() - cache_time < timedelta(days=30):
            return JsonResponse(cnpj_cache[cnpj]['data'])
    
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        logger.info(f"Fazendo requisição para: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        logger.info(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            logger.info("Requisição bem-sucedida")
            
            # Armazena no cache
            cnpj_cache[cnpj] = {
                'data': data,
                'timestamp': datetime.now()
            }
            
            return JsonResponse(data)
        else:
            logger.error(f"Erro na API: {response.status_code} - {response.text}")
            return JsonResponse({
                "erro": f"Erro na API: {response.status_code}",
                "mensagem": "Não foi possível consultar o CNPJ na Receita Federal."
            }, status=response.status_code)
    except Exception as e:
        logger.exception(f"Exceção ao consultar CNPJ: {str(e)}")
        return JsonResponse({
            "erro": str(e),
            "mensagem": "Erro ao processar a requisição."
        }, status=500)
