from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import viewsets
from .models import Sites  # Corrigido: Site → Sites
from .serializers import SiteSerializer
from rest_framework.permissions import AllowAny

# Corrigido para usar o nome correto dos modelos
from ..BrasilEstados.models import BrasilEstados
from ..BrasilMunicipios.models import BrasilMunicipios
from ..BrasilDistritos.models import BrasilDistritos
import unicodedata
import re

class SiteViewSet(viewsets.ModelViewSet):
    queryset = Sites.objects.all()  # Corrigido: Site → Sites
    serializer_class = SiteSerializer
    permission_classes = [AllowAny]  # Permitir acesso anônimo apenas para Sites

@api_view(['GET'])
def search_localizacoes(request):
    """
    Endpoint para busca rápida de estados, municípios e distritos.
    """
    query = request.query_params.get('q', '').strip()
    if len(query) < 2:
        return Response({'results': []})
    
    # Normalizar a consulta para ignorar acentos e maiúsculas/minúsculas
    query_norm = normalize_string(query)
    print(f"Termo de busca: '{query}' (normalizado: '{query_norm}')")
    
    results = []
    max_results_per_type = 7  # Limite de resultados por tipo
    
    try:
        # Primeira etapa: buscar na tabela Sites (prioridade)
        sites_results = Sites.objects.filter(
            Q(cidade__icontains=query) | 
            Q(estado__icontains=query) |
            Q(distrito__icontains=query) |
            Q(estado_sigla__icontains=query)
        )[:max_results_per_type]
        
        print(f"Sites encontrados: {sites_results.count()}")
        
        # Adicionar resultados de Sites à lista de resultados
        for site in sites_results:
            result_type = 'distrito' if site.distrito else 'cidade'
            display_text = f"{site.cidade} / {site.estado} ({site.estado_sigla})"
            if site.distrito:
                display_text += f" / {site.distrito}"
                
            results.append({
                'type': result_type,
                'value': site.distrito if site.distrito else site.cidade,
                'display': display_text,
                'codigo_uf': None,
                'codigo_ibge': None,
                'estado': site.estado,
                'cidade': site.cidade,
                'distrito': site.distrito,
                'uf': site.estado_sigla,
                'has_site_info': True,
                'id_sites': site.id_sites
            })
        
        # Segunda etapa: buscar estados, municípios e distritos nas tabelas Brasil*
        # Aqui estamos buscando registros que não estão em Sites
        
        # Buscar estados
        estados = BrasilEstados.objects.filter(
            Q(nome__icontains=query) | Q(uf__icontains=query)
        )[:max_results_per_type]
        
        print(f"Estados encontrados: {estados.count()}")
        
        # Buscar municípios
        municipios = BrasilMunicipios.objects.filter(
            Q(nome__icontains=query)
        )[:max_results_per_type]
        
        print(f"Municípios encontrados: {municipios.count()}")
        
        # Buscar distritos - IMPORTANTE: incluir esta busca
        distritos = BrasilDistritos.objects.filter(
            Q(nome__icontains=query)
        )[:max_results_per_type]
        
        print(f"Distritos encontrados: {distritos.count()}")
        
        # Adicionar estados que não estão em results
        for estado in estados:
            if not any(r['type'] == 'estado' and r['uf'] == estado.uf for r in results):
                # Verificar se existe em Sites
                has_site = Sites.objects.filter(estado_sigla=estado.uf).exists()
                
                results.append({
                    'type': 'estado',
                    'value': estado.nome,
                    'display': f"{estado.nome} ({estado.uf})",
                    'codigo_uf': estado.codigo_uf,
                    'uf': estado.uf,
                    'estado': estado.nome,
                    'cidade': None,
                    'distrito': None,
                    'has_site_info': has_site
                })
        
        # Adicionar municípios que não estão em results
        for municipio in municipios:
            estado = BrasilEstados.objects.get(codigo_uf=municipio.codigo_uf)
            
            if not any(r['type'] == 'cidade' and 
                      r['cidade'] == municipio.nome and 
                      r['uf'] == estado.uf for r in results):
                
                # Verificar se existe em Sites
                has_site = Sites.objects.filter(
                    cidade__iexact=municipio.nome,
                    estado_sigla=estado.uf,
                    distrito__isnull=True
                ).exists()
                
                results.append({
                    'type': 'cidade',
                    'value': municipio.nome,
                    'display': f"{municipio.nome} / {estado.nome} ({estado.uf})",
                    'codigo_uf': municipio.codigo_uf,
                    'codigo_ibge': municipio.codigo_ibge,
                    'estado': estado.nome,
                    'cidade': municipio.nome,
                    'distrito': None,
                    'uf': estado.uf,
                    'has_site_info': has_site
                })
        
        # Adicionar distritos que não estão em results
        for distrito in distritos:
            try:
                municipio = BrasilMunicipios.objects.get(codigo_ibge=distrito.id_municipio)
                estado = BrasilEstados.objects.get(codigo_uf=municipio.codigo_uf)
                
                if not any(r['type'] == 'distrito' and 
                          r['distrito'] == distrito.nome and
                          r['cidade'] == municipio.nome and
                          r['uf'] == estado.uf for r in results):
                    
                    # Verificar se existe em Sites
                    has_site = Sites.objects.filter(
                        cidade__iexact=municipio.nome,
                        estado_sigla=estado.uf,
                        distrito__iexact=distrito.nome
                    ).exists()
                    
                    results.append({
                        'type': 'distrito',
                        'value': distrito.nome,
                        'display': f"{municipio.nome} / {estado.nome} ({estado.uf}) / {distrito.nome}",
                        'codigo_uf': municipio.codigo_uf,
                        'codigo_ibge': municipio.codigo_ibge,
                        'estado': estado.nome,
                        'cidade': municipio.nome,
                        'distrito': distrito.nome,
                        'uf': estado.uf,
                        'has_site_info': has_site
                    })
            except Exception as e:
                print(f"Erro ao processar distrito {distrito.nome}: {str(e)}")
        
        # Ordenação dos resultados
        results.sort(key=lambda x: (
            0 if x.get('has_site_info', False) else 1,  # Prioriza os que têm info
            0 if x['type'] == 'cidade' else 1 if x['type'] == 'distrito' else 2,  # Prioriza cidades, depois distritos, depois estados
            0 if query.lower() in x['value'].lower() else 1,  # Prioriza correspondência no nome
            x['value'].lower()  # Ordem alfabética
        ))
        
    except Exception as e:
        print(f"Erro na busca: {str(e)}")
        import traceback
        traceback.print_exc()
        return Response({'results': [], 'error': str(e)}, status=500)
    
    return Response({'results': results[:15]})

def normalize_string(s):
    """
    Remove acentos, converte para minúsculas e padroniza o texto para busca.
    """
    if not s:
        return ''
    
    try:
        # Normalização NFD para separar caracteres base de seus acentos
        normalized = unicodedata.normalize('NFD', s)
        # Remover todos os acentos (marcas diacríticas)
        normalized = ''.join(c for c in normalized if not unicodedata.combining(c))
        # Converter para minúsculas
        normalized = normalized.lower()
        # Remover caracteres especiais e espaços extras
        normalized = re.sub(r'[^\w\s]', '', normalized)
        # Substituir múltiplos espaços por um único
        normalized = re.sub(r'\s+', ' ', normalized).strip()
        
        return normalized
    except Exception as e:
        print(f"Erro na normalização: {str(e)}")
        return s.lower()  # Fallback simples