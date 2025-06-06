from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Parcelamento
from .serializers import ParcelamentoSerializer

# Dicionário de meses em português
MESES_PT_BR = {
    "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
    "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
    "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
}

class ParcelamentosMensalView(APIView):
    def get(self, request, *args, **kwargs):
        avisardia = request.query_params.get('avisardia')
        finalizames = request.query_params.get('finalizames')

        # Definir data de referência
        if avisardia:
            try:
                data_referencia = datetime.strptime(avisardia, '%Y-%m-%d').date()
            except ValueError as e:
                return Response(
                    {"error": f"Data inválida: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            # Usar data atual quando avisardia não for fornecido
            data_referencia = datetime.now().date()

        # Base da query - parcelamentos não finalizados
        queryset = Parcelamento.objects.filter(
            finalizado_empresa="Não"
        )
        
        # Aplicar filtro de finalizames somente se fornecido
        if finalizames:
            queryset = queryset.exclude(
                finalizado_mes_geral__iexact=finalizames
            )

        serializer = ParcelamentoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)