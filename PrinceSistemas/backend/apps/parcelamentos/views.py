from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from django.db.models import Q
from .models import Parcelamento
from .serializers import ParcelamentoSerializer
from django.db.models.functions import Cast
from django.db.models import DateField
from datetime import datetime
import re  # Importação do módulo re para expressões regulares
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import make_aware

# Dicionário de meses em português
MESES_PT_BR = {
    "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
    "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
    "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
}

class ParcelamentoFilter(FilterSet):
    datalembrete = CharFilter(field_name='data_lembrete', method='filter_data_lembrete')
    mes_nao_finalizado = CharFilter(method='filter_mes_nao_finalizado')
    para_fazer = CharFilter(method='filter_para_fazer')

    class Meta:
        model = Parcelamento
        fields = ['datalembrete', 'mes_nao_finalizado']

    def filter_data_lembrete(self, queryset, name, value):
        print(f"Valor recebido em filter_data_lembrete: '{value}'")

        # Ignora valores nulos, vazios ou inválidos como "  /  /       :"
        if not value or not value.strip() or value.strip() == "  /  /       :":
            print("Valor nulo, vazio ou inválido ('  /  /       :'), ignorando filtro")
            return queryset

        # Verifica se o valor recebido contém um formato de data válido (ex.: DD/MM/YYYY)
        if not re.search(r'\d{2}/\d{2}/\d{4}', value):
            print("Valor não contém formato de data válido, ignorando filtro")
            return queryset

        # Formata a data recebida
        value_clean = value.strip()
        try:
            data_str = value_clean.split(" ")[0]  # Pega apenas DD/MM/YYYY, ignorando HH:MM se presente
            data_formatada = datetime.strptime(data_str, "%d/%m/%Y").date()
            print(f"Data formatada com sucesso: {data_formatada}")
        except ValueError as e:
            print(f"Erro ao converter data: {e}")
            return queryset

        # Filtra registros com formato de data válido antes do Cast
        queryset = queryset.filter(data_lembrete__regex=r'\d{2}/\d{2}/\d{4}')

        # Aplica o Cast e o filtro de data
        try:
            queryset = queryset.annotate(data_lembrete_date=Cast('data_lembrete', DateField()))
            return queryset.filter(data_lembrete_date=data_formatada)
        except Exception as e:
            print(f"Erro ao aplicar filtro no banco de dados: {e}")
            return queryset  # Retorna o queryset filtrado por regex se houver erro

    def filter_mes_nao_finalizado(self, queryset, name, value):
        value = value.strip()
        if not value:
            return queryset
        # Retorna registros onde FinalizadoEmpresa é "Não" e FinalizadoMesGeral é diferente do mês escolhido (case-insensitive)
        return queryset.filter(finalizado_empresa="Não").exclude(finalizado_mes_geral__iexact=value)

    def filter_para_fazer(self, queryset, name, value):
        """
        Filtra parcelamentos marcados como 'Para Fazer'
        """
        if value.lower() in ['true', '1', 'sim', 'checked']:
            return queryset.filter(para_fazer='Checked')
        return queryset

class ParcelamentoViewSet(viewsets.ModelViewSet):
    queryset = Parcelamento.objects.all()
    serializer_class = ParcelamentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParcelamentoFilter

    def get_queryset(self):
        queryset = Parcelamento.objects.all()
        query = self.request.query_params.get('q', None)
        if query:
            print(f"Filtro aplicado em Parcelamentos: q={query}")
            queryset = queryset.filter(
                Q(razao_social__icontains=query) | Q(cnpj__icontains=query)
            )
            print(f"Resultados encontrados em Parcelamentos: {queryset.count()}")
        return queryset

class AvisosParcelamentosView(APIView):
    def get(self, request, *args, **kwargs):
        avisar_dia = request.query_params.get('avisardia')
        if not avisar_dia or not re.match(r'^\d{4}-\d{2}-\d{2}$', avisar_dia):
            return Response(
                {"error": "Data inválida. Use o formato YYYY-MM-DD"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data_referencia = datetime.strptime(avisar_dia, '%Y-%m-%d').date()
            
            # Converte a data para o formato do banco de dados: dd/mm/yyyy
            data_formatada = data_referencia.strftime('%d/%m/%Y')
            
            # Filtra parcelamentos que têm a data de lembrete igual à data informada
            # OU que estão marcados como "Para Fazer"
            parcelamentos = (
                Parcelamento.objects
                .filter(Q(data_lembrete__startswith=data_formatada) | Q(para_fazer='Checked'))
                .values('id_parcel', 'razao_social', 'cnpj', 'data_lembrete')
            )
            
            resultados = [{"tipo": "parcelamento", **parcelamento} for parcelamento in parcelamentos]
            return Response(resultados, status=status.HTTP_200_OK)
            
        except ValueError as e:
            return Response(
                {"error": f"Erro na conversão da data: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )