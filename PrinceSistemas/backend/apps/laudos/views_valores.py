from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Laudo

@api_view(['GET'])
@permission_classes([AllowAny])
def valores_campo_laudos(request, campo):
    q = request.GET.get('q', '')
    campos_permitidos = {
        'cidade': 'endcidade',
        'razaosocial': 'razaosocial',
        'cnpj': 'cnpj',
        'situacao': 'situacao',
        # adicione outros campos conforme necessário
    }
    if campo not in campos_permitidos:
        return Response([])
    lookup = campos_permitidos[campo]
    filtro = {f'{lookup}__icontains': q} if q else {}
    valores = Laudo.objects.filter(**filtro).values_list(lookup, flat=True).distinct().order_by(lookup)
    return Response([v for v in valores if v])
