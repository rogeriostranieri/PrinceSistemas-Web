from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Telefone
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
    """Vista para a página inicial do app TelefoneOrgaoPublico"""
    return JsonResponse({"message": "API de Telefones de Órgãos Públicos"})

@csrf_exempt
def listar_telefones(request):
    """Lista todos os telefones de órgãos públicos"""
    telefones = Telefone.objects.all().values(
        'ID_Telefones', 'Nome', 'Telefone1', 'TelefoneOutros', 'Obs', 
        'CEP', 'Endereço', 'Numero', 'Complemento', 'Bairro', 
        'Cidade', 'Estado', 'email', 'site', 
        'OrgaoEstado', 'OrgaoCidade', 'OrgaoFederal'  # Use maiúsculas como no modelo
    )
    return JsonResponse(list(telefones), safe=False)

@csrf_exempt
def telefone_detail(request, id):
    """Detalhe de um telefone específico"""
    telefone = get_object_or_404(Telefone, ID_Telefones=id)
    
    if request.method == 'GET':
        data = {
            'ID_Telefones': telefone.ID_Telefones,
            'Nome': telefone.Nome,
            'Telefone1': telefone.Telefone1,
            'TelefoneOutros': telefone.TelefoneOutros,
            'Obs': telefone.Obs,
            'CEP': telefone.CEP,
            'Endereço': telefone.Endereço,
            'Numero': telefone.Numero,
            'Complemento': telefone.Complemento,
            'Bairro': telefone.Bairro,
            'Cidade': telefone.Cidade,
            'Estado': telefone.Estado,
            'email': telefone.email,
            'site': telefone.site,
            'OrgaoEstado': telefone.OrgaoEstado,
            'OrgaoCidade': telefone.OrgaoCidade,
            'OrgaoFederal': telefone.OrgaoFederal
        }
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        # Decodificar o corpo da requisição JSON
        try:
            data = json.loads(request.body)
            
            # Atualizar os campos do telefone
            if 'Nome' in data:
                telefone.Nome = data['Nome']
            if 'Telefone1' in data:
                telefone.Telefone1 = data['Telefone1']
            if 'TelefoneOutros' in data:
                telefone.TelefoneOutros = data['TelefoneOutros']
            if 'Obs' in data:
                telefone.Obs = data['Obs']
            if 'CEP' in data:
                telefone.CEP = data['CEP']
            if 'Endereço' in data:
                telefone.Endereço = data['Endereço']
            if 'Numero' in data:
                telefone.Numero = data['Numero']
            if 'Complemento' in data:
                telefone.Complemento = data['Complemento']
            if 'Bairro' in data:
                telefone.Bairro = data['Bairro']
            if 'Cidade' in data:
                telefone.Cidade = data['Cidade']
            if 'Estado' in data:
                telefone.Estado = data['Estado']
            if 'email' in data:
                telefone.email = data['email']
            if 'site' in data:
                telefone.site = data['site']
            if 'OrgaoEstado' in data:
                telefone.OrgaoEstado = str(data['OrgaoEstado']).lower()  # Acesse com O maiúsculo
            if 'OrgaoCidade' in data:
                telefone.OrgaoCidade = str(data['OrgaoCidade']).lower()  # Acesse com O maiúsculo
            if 'OrgaoFederal' in data:
                telefone.OrgaoFederal = str(data['OrgaoFederal']).lower()  # Acesse com O maiúsculo
            
            # Salvar as alterações
            telefone.save()
            
            # Retornar os dados atualizados
            return JsonResponse({
                'message': 'Telefone atualizado com sucesso',
                'telefone': {
                    'ID_Telefones': telefone.ID_Telefones,
                    'Nome': telefone.Nome,
                    'Telefone1': telefone.Telefone1,
                    # ... outros campos
                }
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == 'DELETE':
        try:
            telefone.delete()
            return JsonResponse({'message': 'Telefone excluído com sucesso'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    # Se o método não for GET, PUT ou DELETE
    return JsonResponse({'error': 'Método não permitido'}, status=405)