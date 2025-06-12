from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.db.models import Q, F
from .models import Laudo
from .serializers import LaudoSerializer
from rest_framework.serializers import ValidationError
import logging
from django.utils.timezone import make_aware
from datetime import datetime, date
from django.db.models.functions import Cast
from django.db.models import DateField
import re
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from apps.empresas.models import Empresa
from apps.parcelamentos.models import Parcelamento
import django_filters
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)

class LaudoFilter(django_filters.FilterSet):
    avisardia = django_filters.CharFilter(method='filter_avisardia')

    class Meta:
        model = Laudo
        fields = ['avisardia']

    def filter_avisardia(self, queryset, name, value):
        if not value or value.strip() in ['  /  /', '  /  /    ', '  /  /  :  ', '/', '//', '///', '', 'None', 'null', '00/00/0000']:
            return queryset.none()
        date_pattern = r'^\d{2}/\d{2}/\d{4}$'
        iso_date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        try:
            if re.match(date_pattern, value):
                day, month, year = value.split('/')
                value = f"{year}-{month}-{day}"
            elif re.match(iso_date_pattern, value):
                pass
            else:
                return queryset.none()
            return queryset.exclude(avisardia__in=['  /  /', '  /  /    ', '  /  /  :  ', '/', '//', '///', '', 'None', 'null', '00/00/0000']) \
                           .annotate(avisardia_date=Cast('avisardia', DateField())) \
                           .filter(avisardia_date=value)
        except Exception:
            return queryset.none()

class LaudoViewSet(viewsets.ModelViewSet):
    queryset = Laudo.objects.all()
    serializer_class = LaudoSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['lembrete', 'prioridade']
    search_fields = ['razaosocial', 'cnpj']
    ordering_fields = ['razaosocial', 'avisardia', 'id_laudos']
    filterset_class = LaudoFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        lembrete = self.request.query_params.get('lembrete')
        prioridade = self.request.query_params.get('prioridade')

        valores_verdadeiros = ['true', '1', 'sim', 'checked', 'on']
        if lembrete is not None:
            if str(lembrete).strip().lower() in valores_verdadeiros:
                queryset = queryset.filter(
                    lembrete__iregex=r'^(true|1|sim|checked|on)$'
                )
            else:
                queryset = queryset.exclude(
                    lembrete__iregex=r'^(true|1|sim|checked|on)$'
                )

        if prioridade is not None:
            if str(prioridade).strip().lower() in valores_verdadeiros:
                queryset = queryset.filter(
                    prioridade__iregex=r'^(true|1|sim|checked|on)$'
                )
            else:
                queryset = queryset.exclude(
                    prioridade__iregex=r'^(true|1|sim|checked|on)$'
                )

        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter(
                Q(razaosocial__icontains=query) | Q(cnpj__icontains=query)
            )
        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        for campo in [
            'avisardia', 'bombeiros_venc', 'ambiental_venc', 'viabilidade_vec',
            'sanitario_venc', 'setran_venc', 'bombeiro_data_provisorio',
            'ambiental_data_provisorio', 'viabilidade_data_provisorio',
            'sanitario_data_provisorio', 'setran_data_provisorio',
            'bombeiro_data_ped_processo', 'bombeiro_data_multa',
            'bombeiro_provisorio_data', 'ambiental_provisorio_data',
            'viabilidade_provisorio_data', 'sanitario_provisorio_data',
            'setran_provisorio_data', 'data_criado', 'data_entrada'
        ]:
            valor = request.data.get(campo)
            if valor in ["", "  /  /", None, "null", "None", "00/00/0000"]:
                request.data[campo] = None
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except ValidationError as e:
            logger.error(f"Validation error during update: {e.detail}")
            return Response({"error": "Falha na validação", "details": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        for campo in [
            'avisardia', 'bombeiros_venc', 'ambiental_venc', 'viabilidade_vec',
            'sanitario_venc', 'setran_venc', 'bombeiro_data_provisorio',
            'ambiental_data_provisorio', 'viabilidade_data_provisorio',
            'sanitario_data_provisorio', 'setran_data_provisorio',
            'bombeiro_data_ped_processo', 'bombeiro_data_multa',
            'bombeiro_provisorio_data', 'ambiental_provisorio_data',
            'viabilidade_provisorio_data', 'sanitario_provisorio_data',
            'setran_provisorio_data', 'data_criado', 'data_entrada'
        ]:
            valor = request.data.get(campo)
            if valor in ["", "  /  /", None, "null", "None", "00/00/0000"]:
                request.data[campo] = None
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            logger.error(f"Validation error during create: {e.detail}")
            return Response({"error": "Falha na validação", "details": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='importar-empresa')
    def importar_empresa(self, request):
        """
        Importa os dados de uma empresa para criar ou atualizar um laudo.
        
        Parâmetros:
        - empresa_id: ID da empresa a ser importada
        - atualizar: (opcional) Se True, atualiza o laudo existente se houver
        """
        empresa_id = request.data.get('empresa_id')
        atualizar = request.data.get('atualizar', True)
        
        if not empresa_id:
            return Response(
                {"error": "ID da empresa é obrigatório"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Busca a empresa pelo ID
        try:
            empresa = get_object_or_404(Empresa, id_empresas=empresa_id)
        except Empresa.DoesNotExist:
            return Response(
                {"error": f"Empresa com ID {empresa_id} não encontrada"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Normaliza o CNPJ (remove caracteres não numéricos)
        cnpj_normalizado = ''.join(filter(str.isdigit, empresa.cnpj)) if empresa.cnpj else None
        
        # Adicione estes logs para debug
        print(f"CNPJ normalizado: '{cnpj_normalizado}'")

        # Verifica se já existe um laudo com o mesmo CNPJ (usando normalização dupla)
        laudo_existente = None
        try:
            # Busca mais robusta - normaliza os CNPJs já existentes também
            laudos_existentes = Laudo.objects.all()
            for laudo in laudos_existentes:
                laudo_cnpj = ''.join(filter(str.isdigit, laudo.cnpj)) if laudo.cnpj else ''
                print(f"Comparando CNPJ normalizado '{cnpj_normalizado}' com laudo CNPJ '{laudo_cnpj}'")
                if laudo_cnpj == cnpj_normalizado and laudo_cnpj:
                    laudo_existente = laudo
                    print(f"Encontrado laudo existente com ID: {laudo.id_laudos}")
                    break
            
            # Se não encontrou com a busca manual, tenta a busca direta
            if not laudo_existente:
                laudo_existente = Laudo.objects.filter(cnpj=cnpj_normalizado).first()
                if laudo_existente:
                    print(f"Encontrado laudo com busca direta, ID: {laudo_existente.id_laudos}")
        except Exception as e:
            print(f"Erro ao verificar laudos existentes: {str(e)}")
            return Response(
                {"error": f"Erro ao verificar laudos existentes: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Monta os dados para o laudo - tratando todos os campos de forma segura
        dados_laudo = {}
        
        # Campos de texto simples
        campos_texto = [
            'razaosocial', 'endereco', 'endnum', 'endcomp', 'enddata', 'endquadra', 
            'endzona', 'telefone', 'cnae', 'cnae_primario', 'requerente', 'rg_requerente',
            'orgao_rg_requerente', 'estado_orgao_rg_requerente', 'endbairro', 'endcidade',
            'endestado', 'ramodeatividade', 'area', 'area2', 'ponto_ref', 'cad_imob',
            'observacao', 'situacao', 'natureza_pedido', 'end_requerente', 'email_requerente',
            'fone_requerente'
        ]
        
        for campo in campos_texto:
            valor = getattr(empresa, campo, None)
            if valor not in [None, '', 'None']:
                dados_laudo[campo] = valor
        
        # Campos com tratamento especial
        dados_laudo['cnpj'] = cnpj_normalizado
        dados_laudo['cnpj_requerente'] = cnpj_normalizado
        
        # NOVOS MAPEAMENTOS: Dados do requerente (sócio responsável)
        dados_laudo['requerente'] = empresa.nomeresponsavel
        dados_laudo['rg_requerente'] = empresa.resprg
        dados_laudo['orgao_rg_requerente'] = empresa.responsavelorgaorg
        dados_laudo['estado_orgao_rg_requerente'] = empresa.responsavelestadoorgaorg
        
        # NOVOS MAPEAMENTOS: CNAEs
        dados_laudo['cnae_primario'] = empresa.cnaeprincipal
        dados_laudo['cnae'] = empresa.cnaesecundario
        
        # NOVOS MAPEAMENTOS: Endereço
        dados_laudo['endzona'] = empresa.endzona
        dados_laudo['endquadra'] = empresa.endquadra
        dados_laudo['enddata'] = empresa.enddata
        dados_laudo['endnum'] = empresa.endnumero
        dados_laudo['endcomp'] = empresa.endcomplemento
        
        # NOVO MAPEAMENTO: Protocolo da Empresa Fácil como Número do Laudo
        dados_laudo['nlaudo'] = empresa.protocolojuntacomercial
        
        # Trata campos numéricos
        if empresa.endcep:
            dados_laudo['endcep'] = ''.join(filter(str.isdigit, empresa.endcep))
        
        if empresa.cpfresponsavel:
            dados_laudo['cpf_requerente'] = ''.join(filter(str.isdigit, empresa.cpfresponsavel))
        
        # Campos booleanos (como valores booleanos True/False)
        dados_laudo['matriz'] = 'Sim' if empresa.sede == 'Matriz' else 'Não'  # True se for Matriz, False caso contrário
        dados_laudo['lembrete'] = False  # Valor padrão
        dados_laudo['prioridade'] = empresa.prioridade in [True, 'Sim']  # True se for True ou 'Sim', False caso contrário
        
        # Campos de data
        dados_laudo['data_criado'] = datetime.now().strftime('%Y-%m-%d')
        
        if hasattr(empresa, 'empinicioatividade') and empresa.empinicioatividade:
            try:
                if isinstance(empresa.empinicioatividade, datetime):
                    dados_laudo['data_entrada'] = empresa.empinicioatividade.strftime('%d/%m/%Y')
                elif isinstance(empresa.empinicioatividade, str):
                    # Tenta diversos formatos
                    for fmt in ['%d/%m/%Y', '%Y-%m-%d']:
                        try:
                            data = datetime.strptime(empresa.empinicioatividade, fmt)
                            dados_laudo['data_entrada'] = data.strftime('%d/%m/%Y')
                            break
                        except ValueError:
                            continue
            except Exception as e:
                print(f"Erro ao processar data de início: {e}")
        
        # Adiciona referência à empresa de origem
        dados_laudo['empresa_id'] = empresa.id_empresas
        
        # Não precisamos fornecer id_laudos, ele será gerado automaticamente pelo modelo
        # para novos registros, ou será mantido no caso de atualizações
        
        # Resolve o problema do id_laudos sendo obrigatório
        if not laudo_existente:  # Só para novos laudos
            try:
                ultimo_id = Laudo.objects.all().order_by('-id_laudos').first()
                proximo_id = 1 if not ultimo_id else ultimo_id.id_laudos + 1
                dados_laudo['id_laudos'] = proximo_id
            except Exception as e:
                print(f"Erro ao determinar próximo ID: {e}")
        
        # Se existe laudo e quer atualizar
        if laudo_existente and atualizar:
            serializer = self.get_serializer(laudo_existente, data=dados_laudo, partial=True)
            message = "Laudo atualizado com sucesso!"
            action = "atualizado"
        # Se existe laudo mas não quer atualizar    
        elif laudo_existente and not atualizar:
            return Response({
                "message": "Laudo já existe",
                "id_laudos": laudo_existente.id_laudos,
                "razaosocial": laudo_existente.razaosocial,
                "cnpj": laudo_existente.cnpj,
                "action": "existente"
            })
        # Caso não exista, cria um novo
        else:
            serializer = self.get_serializer(data=dados_laudo)
            message = "Novo laudo criado com sucesso!"
            action = "criado"
        
        # Valida e salva os dados
        try:
            serializer.is_valid(raise_exception=True)
            laudo = serializer.save()
            
            return Response({
                "message": message,
                "id_laudos": laudo.id_laudos,
                "razaosocial": laudo.razaosocial,
                "cnpj": laudo.cnpj,
                "empresa_id": empresa.id_empresas,
                "action": action
            })
        except Exception as e:
            return Response(
                {
                    "error": f"Erro ao {action} laudo: {str(e)}", 
                    "details": serializer.errors if hasattr(serializer, 'errors') else None
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['get'], url_path='cnpj/(?P<cnpj>[0-9]+)')
    def get_by_cnpj(self, request, cnpj=None):
        """
        Retorna um laudo pelo CNPJ da empresa.
        O CNPJ deve ser informado apenas com números.
        """
        if not cnpj:
            return Response(
                {"error": "CNPJ não informado"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Normaliza o CNPJ (remove caracteres não numéricos)
        cnpj_normalizado = ''.join(filter(str.isdigit, cnpj))
        
        # Busca o laudo pelo CNPJ
        try:
            laudo = Laudo.objects.filter(cnpj=cnpj_normalizado).first()
            if laudo:
                serializer = self.get_serializer(laudo)
                return Response(serializer.data)
            else:
                return Response(
                    {"error": f"Nenhum laudo encontrado com o CNPJ {cnpj}"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {"error": f"Erro ao buscar laudo por CNPJ: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class AvisosDiaView(APIView):
    def get(self, request, *args, **kwargs):
        avisar_dia = request.query_params.get('avisardia')
        if not avisar_dia or not re.match(r'^\d{4}-\d{2}-\d{2}$', avisar_dia):
            return Response({"error": "A data 'avisardia' é obrigatória e deve estar no formato YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            avisar_dia_date = datetime.strptime(avisar_dia, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Formato de data inválido. Use 'YYYY-MM-DD'."}, status=status.HTTP_400_BAD_REQUEST)

        # Adicione filtro para ignorar datas inválidas
        invalid_dates = ["  /  /", "  /  /    ", "  /  /  :  ", "/", "//", "///", "", "None", "null", "00/00/0000", None]
        empresas = Empresa.objects.exclude(avisardia__in=invalid_dates) \
            .annotate(avisardia_date=Cast('avisardia', DateField())) \
            .filter(avisardia_date=avisar_dia_date) \
            .values('id_empresas', 'razaosocial', 'cnpj', 'avisardia')
        laudos = Laudo.objects.exclude(avisardia__in=invalid_dates) \
            .annotate(avisardia_date=Cast('avisardia', DateField())) \
            .filter(avisardia_date=avisar_dia_date)
        parcelamentos = Parcelamento.objects.exclude(avisardia__in=invalid_dates) \
            .annotate(avisardia_date=Cast('avisardia', DateField())) \
            .filter(avisardia_date=avisar_dia_date) \
            .values('id_parcel', 'razaosocial', 'cnpj', 'avisardia')

        resultados = []
        for empresa in empresas:
            resultados.append({**empresa, 'tipo': 'empresa'})
        for laudo in laudos:
            resultados.append({**laudo, 'tipo': 'laudo'})
        for parcelamento in parcelamentos:
            resultados.append({**parcelamento, 'tipo': 'parcelamento'})

        return Response(resultados, status=status.HTTP_200_OK)

class AvisosLaudosView(APIView):
    def get(self, request, *args, **kwargs):
        avisar_dia = request.query_params.get('avisardia')
        if not avisar_dia or not re.match(r'^\d{4}-\d{2}-\d{2}$', avisar_dia):
            return Response(
                {"error": "A data 'avisardia' é obrigatória e deve estar no formato YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data_referencia = datetime.strptime(avisar_dia, '%Y-%m-%d').date()
        except ValueError as e:
            return Response(
                {"error": f"Erro na conversão da data: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Lista de datas inválidas conhecidas
        datas_invalidas = ["  /  /", "  /  /    ", "  /  /  :  ", "/", "//", "///", "", "None", "null", "00/00/0000", None]

        # Excluir laudos com datas inválidas antes da conversão
        laudos_queryset = (
            Laudo.objects.exclude(avisardia__in=datas_invalidas)
            .annotate(data_valida=Cast('avisardia', DateField()))
            .filter(data_valida=data_referencia)
            .values('id_laudos', 'razaosocial', 'cnpj', 'avisardia', 'lembrete', 'prioridade')
        )

        resultados = []
        for laudo in laudos_queryset:
            try:
                resultados.append({"tipo": "laudo", **laudo})
            except Exception as e:
                # Opcional: logar erro
                continue

        return Response(resultados, status=status.HTTP_200_OK)

def declaracao_extravio_pdf(request, laudo_id):
    """
    Função substituída que não usa weasyprint.
    """
    from .models import Laudo
    laudo = Laudo.objects.get(pk=laudo_id)
    
    return HttpResponse(
        f"A funcionalidade de exportação para PDF do laudo '{laudo.razaosocial}' foi desativada "
        f"pois dependia da biblioteca weasyprint. "
        f"Por favor, use as opções de exportação para Word disponíveis.",
        content_type='text/plain'
    )