from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.empresas.models import Empresa
from apps.laudos.models import Laudo
from apps.parcelamentos.models import Parcelamento
from apps.socios.models import Socio

@api_view(['GET'])
@permission_classes([AllowAny])
def check_related_records(request):
    cnpj = request.query_params.get('cnpj', None)
    cpf = request.query_params.get('cpf', None)

    if not cnpj and not cpf:
        return Response({"error": "Forneça pelo menos um CNPJ ou CPF"}, status=400)

    response = {
        "empresas": False,
        "laudos": False,
        "parcelamentos": False,
        "socios": False
    }

    if cnpj:
        response["empresas"] = Empresa.objects.filter(cnpj=cnpj).exists()
        response["laudos"] = Laudo.objects.filter(cnpj=cnpj).exists()
        response["parcelamentos"] = Parcelamento.objects.filter(cnpj=cnpj).exists()
    if cpf:
        response["socios"] = Socio.objects.filter(cpf=cpf).exists()

    return Response(response, status=200)
