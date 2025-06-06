from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Contato
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def listar_contatos(request):
    """Lista todos os contatos"""
    contatos = Contato.objects.all().values(
        "ID_Contatos", "Nome", "Sobrenome", "Telefone_Residencial", 
        "Telefone_Trabalho", "Telefone_Celular_Particular", 
        "Telefone_Celular_Contato", "email", "End_CEP", 
        "End_Rua", "End_Numero", "End_Comp", "End_Bairro", 
        "End_Cidade", "End_Estado", "End_Pais", 
        "Outras_Informacoes", "Data"
    )
    return JsonResponse(list(contatos), safe=False)

@csrf_exempt
def detalhe_contato(request, id):
    """Manipula operações em um contato específico"""
    contato = get_object_or_404(Contato, ID_Contatos=id)
    
    if request.method == 'GET':
        data = {
            "ID_Contatos": contato.ID_Contatos,
            "Nome": contato.Nome,
            "Sobrenome": contato.Sobrenome,
            "Telefone_Residencial": contato.Telefone_Residencial,
            "Telefone_Trabalho": contato.Telefone_Trabalho,
            "Telefone_Celular_Particular": contato.Telefone_Celular_Particular,
            "Telefone_Celular_Contato": contato.Telefone_Celular_Contato,
            "email": contato.email,
            "End_CEP": contato.End_CEP,
            "End_Rua": contato.End_Rua,
            "End_Numero": contato.End_Numero,
            "End_Comp": contato.End_Comp,
            "End_Bairro": contato.End_Bairro,
            "End_Cidade": contato.End_Cidade,
            "End_Estado": contato.End_Estado,
            "End_Pais": contato.End_Pais,
            "Outras_Informacoes": contato.Outras_Informacoes,
            "Data": contato.Data,
            # Campos calculados
            "nome_completo": contato.nome_completo(),
            "endereco_completo": contato.endereco_completo()
        }
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            
            # Atualizar os campos do contato
            for field in ['Nome', 'Sobrenome', 'Telefone_Residencial', 'Telefone_Trabalho', 
                         'Telefone_Celular_Particular', 'Telefone_Celular_Contato', 'email',
                         'End_CEP', 'End_Rua', 'End_Numero', 'End_Comp', 'End_Bairro',
                         'End_Cidade', 'End_Estado', 'End_Pais', 'Outras_Informacoes', 'Data']:
                if field in data:
                    setattr(contato, field, data[field])
            
            # Salvar as alterações
            contato.save()
            
            return JsonResponse({
                'message': 'Contato atualizado com sucesso',
                'contato': {
                    'ID_Contatos': contato.ID_Contatos,
                    'Nome': contato.Nome,
                    'Sobrenome': contato.Sobrenome
                }
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == 'DELETE':
        try:
            contato.delete()
            return JsonResponse({'message': 'Contato excluído com sucesso'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def criar_contato(request):
    """Cria um novo contato"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validar dados mínimos
            if 'Nome' not in data:
                return JsonResponse({'error': 'O campo Nome é obrigatório'}, status=400)
            
            # Criar novo contato
            novo_contato = Contato(
                Nome=data.get('Nome'),
                Sobrenome=data.get('Sobrenome'),
                Telefone_Residencial=data.get('Telefone_Residencial'),
                Telefone_Trabalho=data.get('Telefone_Trabalho'),
                Telefone_Celular_Particular=data.get('Telefone_Celular_Particular'),
                Telefone_Celular_Contato=data.get('Telefone_Celular_Contato'),
                email=data.get('email'),
                End_CEP=data.get('End_CEP'),
                End_Rua=data.get('End_Rua'),
                End_Numero=data.get('End_Numero'),
                End_Comp=data.get('End_Comp'),
                End_Bairro=data.get('End_Bairro'),
                End_Cidade=data.get('End_Cidade'),
                End_Estado=data.get('End_Estado'),
                End_Pais=data.get('End_Pais'),
                Outras_Informacoes=data.get('Outras_Informacoes'),
                Data=data.get('Data')
            )
            novo_contato.save()
            
            return JsonResponse({
                'message': 'Contato criado com sucesso',
                'contato': {
                    'ID_Contatos': novo_contato.ID_Contatos,
                    'Nome': novo_contato.Nome,
                    'Sobrenome': novo_contato.Sobrenome
                }
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)