from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q
from django_filters import rest_framework as django_filters
from .models import Empresa
from .serializers import EmpresaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from datetime import datetime
import re
from django.utils import timezone
import logging
from rest_framework.views import APIView
from rest_framework import status
from django.utils.timezone import make_aware
from django.db.models.functions import Cast
from django.db.models import DateField
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
from docxtpl import DocxTemplate
from io import BytesIO
import os
from apps.socios.models import Socio  # Adicione o import do modelo Socio

logger = logging.getLogger(__name__)

class EmpresaFilter(django_filters.FilterSet):
    avisardia = django_filters.CharFilter(method='filter_avisardia')

    class Meta:
        model = Empresa
        fields = ['razaosocial', 'cnpj', 'status', 'avisardia']

    def filter_avisardia(self, queryset, name, value):
        # Trate valores inválidos
        if not value or value.strip() in ['  /  /', '  /  /    ', '  /  /  :  ', '/', '//', '///', '', 'None', 'null', '00/00/0000']:
            return queryset.none()
        # Aqui você pode adicionar lógica para aceitar tanto DD/MM/YYYY quanto YYYY-MM-DD
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

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EmpresaFilter
    search_fields = ['razaosocial', 'cnpj', 'nomefantasia']
    ordering_fields = ['razaosocial', 'avisardia', 'id_empresas']

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
            logger.debug(f"Filtro aplicado: q={query}")
            queryset = queryset.filter(
                Q(razaosocial__icontains=query) | Q(cnpj__icontains=query)
            )
            logger.debug(f"Resultados encontrados: {queryset.count()}")
        return queryset

    def update(self, request, *args, **kwargs):
        """
        Personaliza update para erros detalhados.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        logger.debug(f"Recebido PATCH/PUT para empresa {instance.pk}: {request.data}")
        
        for campo in [
            'avisardia', 'prazosimples', 'empinicioatividade', 'empcriado',
            'dataprotredesim', 'dataprotjuntacomercial', 'datapedidoie',
            'dataregistroalt', 'datamotivo', 'ieinicioatividade',
            'ievencpedido', 'datasimples', 'dataultdefsimples',
            'dataexcsocial', 'cnhdataexp', 'respdatanasc',
            'procuracaodata', 'nireregistrodata', 'iedataaltsolicitado',
            'niredata', 'dbedata', 'protjuntafinal'
        ]:
            valor = request.data.get(campo)
            if valor in ["", "  /  /", None, "null", "None", "00/00/0000"]:
                request.data[campo] = None

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            logger.debug(f"Empresa {instance.pk} atualizada com sucesso")
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Erro no PATCH/PUT /api/empresas/{instance.pk}/: {str(e)}")
            logger.error(f"Dados enviados: {request.data}")
            logger.error(f"Erros de validação: {serializer.errors}")
            return Response(
                {"error": "Falha na validação", "details": serializer.errors},
                status=400
            )

    def create(self, request, *args, **kwargs):
        """
        Personaliza create para erros detalhados.
        """
        logger.debug(f"Recebido POST para nova empresa: {request.data}")
        
        for campo in [
            'avisardia', 'prazosimples', 'empinicioatividade', 'empcriado',
            'dataprotredesim', 'dataprotjuntacomercial', 'datapedidoie',
            'dataregistroalt', 'datamotivo', 'ieinicioatividade',
            'ievencpedido', 'datasimples', 'dataultdefsimples',
            'dataexcsocial', 'cnhdataexp', 'respdatanasc', 'enddata',
            'procuracaodata', 'nireregistrodata', 'iedataaltsolicitado',
            'niredata', 'dbedata', 'protjuntafinal'
        ]:
            valor = request.data.get(campo)
            if valor in ["", "  /  /", None, "null", "None", "00/00/0000"]:
                request.data[campo] = None

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            logger.debug(f"Empresa criada: {serializer.data['id_empresas']}")
            return Response(serializer.data, status=201)
        except Exception as e:
            logger.error(f"Erro no POST /api/empresas/: {str(e)}")
            logger.error(f"Dados enviados: {request.data}")
            logger.error(f"Erros de validação: {serializer.errors}")
            return Response(
                {"error": "Falha na validação", "details": serializer.errors},
                status=400
            )

    @action(detail=False, methods=['get'], url_path='cnpj/(?P<cnpj>[0-9]+)')
    def get_by_cnpj(self, request, cnpj=None):
        """
        Retorna uma empresa pelo CNPJ.
        O CNPJ deve ser informado apenas com números.
        """
        if not cnpj:
            return Response(
                {"error": "CNPJ não informado"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Normaliza o CNPJ (remove caracteres não numéricos)
        cnpj_normalizado = ''.join(filter(str.isdigit, cnpj))
        
        # Busca a empresa pelo CNPJ
        try:
            # Busca mais robusta - normaliza os CNPJs
            empresas = Empresa.objects.all()
            empresa_encontrada = None
            
            for empresa in empresas:
                empresa_cnpj = ''.join(filter(str.isdigit, empresa.cnpj)) if empresa.cnpj else ''
                if empresa_cnpj == cnpj_normalizado and empresa_cnpj:
                    empresa_encontrada = empresa
                    break
            
            # Se não encontrou com a busca manual, tenta a busca direta
            if not empresa_encontrada:
                empresa_encontrada = Empresa.objects.filter(cnpj=cnpj_normalizado).first()
            
            if empresa_encontrada:
                serializer = self.get_serializer(empresa_encontrada)
                return Response(serializer.data)
            else:
                return Response(
                    {"error": f"Nenhuma empresa encontrada com o CNPJ {cnpj}"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {"error": f"Erro ao buscar empresa por CNPJ: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

@api_view(['GET'])
@permission_classes([AllowAny])
def empresas_reminders(request):
    """
    Retorna empresas com avisardia na data fornecida (dd/MM/yyyy).
    """
    date_str = request.GET.get('date', '').strip()
    
    try:
        day, month, year = date_str.split('/')
        formatted_date = f"{day.zfill(2)}/{month.zfill(2)}/{year}"
        formatted_date_obj = datetime.strptime(formatted_date, "%d/%m/%Y").date()
    except ValueError:
        logger.error(f"Formato de data inválido em empresas_reminders: {date_str}")
        return Response({"error": "Formato inválido. Use dd/MM/yyyy."}, status=400)

    reminders = Empresa.objects.filter(avisardia__date=formatted_date_obj)
    
    if not reminders.exists():
        logger.debug(f"Nenhuma empresa encontrada para avisardia: {formatted_date_obj}")
        return Response({"message": "Nenhuma empresa com data de aviso encontrada."}, status=404)
    
    serializer = EmpresaSerializer(reminders, many=True)
    return Response(serializer.data)

class AvisosEmpresasView(APIView):
    def get(self, request, *args, **kwargs):
        avisar_dia = request.query_params.get('avisardia')
        if avisar_dia and re.match(r'^\d{2}/\d{2}/\d{4}$', avisar_dia):
            # Converte para YYYY-MM-DD
            day, month, year = avisar_dia.split('/')
            avisar_dia = f"{year}-{month}-{day}"
        if not avisar_dia or not re.match(r'^\d{4}-\d{2}-\d{2}$', avisar_dia):
            return Response(
                {"error": "A data 'avisardia' é obrigatória e deve estar no formato YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            avisar_dia = datetime.strptime(avisar_dia, '%Y-%m-%d').date()
        except ValueError:
            return Response(
                {"error": "Formato de data inválido. Use 'YYYY-MM-DD'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        empresas = Empresa.objects.annotate(avisardia_date=Cast('avisardia', DateField())) \
            .filter(avisardia_date=avisar_dia) \
            .values('id_empresas', 'razaosocial', 'cnpj', 'avisardia', 'lembrete', 'prioridade')
        resultados = [{"tipo": "empresa", **empresa} for empresa in empresas]

        return Response(resultados, status=status.HTTP_200_OK)

def exportar_empresa_resumida_pdf(request, empresa_id):
    empresa = Empresa.objects.get(pk=empresa_id)
    socio_nome = empresa.nomeresponsavel or ''
    socio_cpf = empresa.cpfresponsavel or ''
    socio_rg = empresa.resprg or ''
    socio_orgao = empresa.responsavelorgaorg or ''
    socio_estado = empresa.responsavelestadoorgaorg or ''
    # Corrigido para aceitar string ou date
    socio_nasc = ''
    if empresa.respdatanasc:
        if hasattr(empresa.respdatanasc, 'strftime'):
            socio_nasc = empresa.respdatanasc.strftime('%d de %B de %Y')
        else:
            try:
                data = datetime.strptime(empresa.respdatanasc, '%Y-%m-%d')
                socio_nasc = data.strftime('%d de %B de %Y')
            except Exception:
                socio_nasc = empresa.respdatanasc

    socio_nacionalidade = 'brasileira'
    socio_estado_civil = 'casada em regime de comunhão parcial de bens'
    socio_profissao = ''
    socio_endereco = f"{empresa.endereco}, nº {empresa.endnumero}, {empresa.endcomplemento+', ' if empresa.endcomplemento else ''}{empresa.endbairro}, CEP: {empresa.endcep}, na cidade de {empresa.endcidade}-{empresa.endestado}"
    socio_genero = 'feminino'
    portador = 'portadora' if socio_genero == 'feminino' else 'portador'
    domiciliado = 'domiciliada' if socio_genero == 'feminino' else 'domiciliado'
    nascido = 'nascida' if socio_genero == 'feminino' else 'nascido'

    contexto = {
        'socio_texto_principal': f"{socio_nome}, {socio_nacionalidade}, {socio_estado_civil}, {nascido} em {socio_nasc}, residente e {domiciliado} na {socio_endereco}, {portador} da Cédula da Identidade Civil RG n.º {socio_rg}-{socio_orgao}/{socio_estado} e do CPF n.º {socio_cpf}.",
        'razao_social': empresa.razaosocial,
        'endereco_empresa': socio_endereco,
        'data_inicio_atividade_extenso': empresa.empinicioatividade.strftime('%d de %B de %Y') if hasattr(empresa.empinicioatividade, 'strftime') else empresa.empinicioatividade or '',
        'objeto_social': empresa.objetodoestabelecimento or empresa.ramodeatividade or '',
        'capital_social': empresa.capitals or '',
        'capital_social_extenso': 'trinta mil reais',
        'quotas': '30.000',
        'quotas_extenso': 'trinta mil',
        'valor_quota': '1,00',
        'valor_quota_extenso': 'um real',
        'cidade_empresa': empresa.endcidade,
        'data_contrato_extenso': '01 de julho de 2024',
        'nome_socio': socio_nome,
    }
    html_string = render_to_string('Abertura1SocioLTDA.html', contexto)
    pdf_file = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=Contrato_{empresa.razaosocial}.pdf'
    return response

def gerar_contrato_word(request, empresa_id):
    empresa = Empresa.objects.get(id_empresas=empresa_id)

    # Busca o sócio responsável pelo CPF
    socio_genero = 'Masculino'  # padrão
    if empresa.cpfresponsavel:
        socio = Socio.objects.filter(cpf=empresa.cpfresponsavel).first()
        if socio:
            texto_completo = montar_texto_socio(socio)
            nome_socio = socio.nomecompleto
            # Remove o nome do início do texto para usar depois do negrito
            if texto_completo.startswith(nome_socio):
                socio_texto_principal_sem_nome = texto_completo[len(nome_socio):].lstrip(", ")
            else:
                socio_texto_principal_sem_nome = texto_completo
    else:
        nome_socio = empresa.nomeresponsavel or ""
        socio_texto_principal_sem_nome = ""

    # Define os termos conforme o gênero
    if socio_genero.lower().startswith('f'):
        termo_socio = 'sócia'
        termo_socio_maiusculo = 'Sócia'
        termo_administrador = 'administradora'
        termo_administrador_maiusculo = 'Administradora'
        termo_administrador_tudo_maiusculo = 'ADMINISTRADORA'
        artigo_socio = 'a'
        artigo_socio_maiusculo = 'A'
    else:
        termo_socio = 'sócio'
        termo_socio_maiusculo = 'Sócio'
        termo_administrador = 'administrador'
        termo_administrador_maiusculo = 'Administrador'
        termo_administrador_tudo_maiusculo = 'ADMINISTRADOR'
        artigo_socio = 'o'
        artigo_socio_maiusculo = 'O'

    # Extrair texto do sócio principal do campo dadossocios
    socio_texto_principal = ""
    
    # Se tiver dados de sócios, extrai o texto do primeiro/principal
    if empresa.dadossocios:
        blocos = empresa.dadossocios.split('//////////////////////////////////////////////////////////////////////')
        blocos = [b.strip() for b in blocos if b.strip()]
        
        # Procura o sócio administrador primeiro
        socio_admin = None
        for bloco in blocos:
            if 'Sócio-Administrador' in bloco:
                socio_admin = bloco
                break
        
        # Se não achou administrador, usa o primeiro sócio
        if not socio_admin and blocos:
            socio_admin = blocos[0]
        
        # Extrai o texto principal
        if socio_admin:
            socio_texto_principal = extrair_texto_principal_socio(socio_admin)
    
    # Se não tem texto de sócio, usa dados básicos do responsável
    if not socio_texto_principal and empresa.nomeresponsavel:
        socio_texto_principal = f"{empresa.nomeresponsavel}, brasileira, portador(a) do CPF n.º {empresa.cpfresponsavel}"
    
    # Prepara endereço formatado
    logradouro = empresa.endereco.lower() if empresa.endereco else ""
    if logradouro and " " in logradouro:
        partes = logradouro.split(" ")
        logradouro = partes[0].lower() + " " + " ".join(partes[1:])
    
    endereco = f"{logradouro}"
    if empresa.endnumero: endereco += f", nº {empresa.endnumero}"
    if empresa.endcomplemento: endereco += f", {empresa.endcomplemento}"
    if empresa.endbairro: endereco += f", {empresa.endbairro}"
    if empresa.endcep: endereco += f", CEP: {empresa.endcep}"
    if empresa.endcidade: endereco += f", localizado na cidade de {empresa.endcidade}"
    if empresa.endestado: endereco += f"-{empresa.endestado}"
    
    # Converte valor do capital para número para processamento
    capital_valor = 0
    try:
        valor_str = empresa.capitals or "0"
        valor_str = valor_str.replace(".", "").replace(",", ".")
        capital_valor = float(valor_str)
    except ValueError:
        capital_valor = 0
    
    # Converte para extenso
    capital_extenso = numero_por_extenso_real(capital_valor)
    
    context = {
        'razao_social': empresa.razaosocial,
        'nome_socio': empresa.nomeresponsavel,
        'socio_texto_principal': socio_texto_principal,
        'endereco_empresa': endereco,
        'data_inicio_atividade_extenso': format_data_extenso(empresa.empinicioatividade),
        'objeto_social': empresa.objetodoestabelecimento or empresa.ramodeatividade or "",
        'capital_social': f"R$ {capital_valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        'capital_social_extenso': valor_por_extenso_real(capital_valor),
        'quotas': str(int(capital_valor)),
        'quotas_extenso': numero_por_extenso_real(int(capital_valor)),
        'valor_quota': "1,00",
        'valor_quota_extenso': "um real",
        'cidade_empresa': empresa.endcidade or "",
        'data_contrato_extenso': datetime.now().strftime("%d de %B de %Y").lower(),
        'termo_socio': termo_socio,
        'termo_socio_maiusculo': termo_socio_maiusculo,
        'termo_administrador': termo_administrador,
        'termo_administrador_maiusculo': termo_administrador_maiusculo,
        'termo_administrador_tudo_maiusculo': termo_administrador_tudo_maiusculo,
        'artigo_socio': artigo_socio,
        'artigo_socio_maiusculo': artigo_socio_maiusculo,
    }
    
    # Caminho absoluto do template
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'Abertura1SocioLTDA.docx')

    doc = DocxTemplate(template_path)
    doc.render(context)
    
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    
    response = HttpResponse(
        buffer.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = f'attachment; filename="Contrato-{empresa.razaosocial}.docx"'
    
    return response

# Corrigir a função gerar_contrato_word_multiplos_socios
def gerar_contrato_word_multiplos_socios(request, empresa_id):
    empresa = Empresa.objects.get(id_empresas=empresa_id)
    
    # Lista para armazenar todos os sócios
    socios_textos = []
    socios_nomes = []
    
    # Se tiver dados de sócios, extrai o texto de todos eles
    if empresa.dadossocios:
        blocos = empresa.dadossocios.split('//////////////////////////////////////////////////////////////////////')
        blocos = [b.strip() for b in blocos if b.strip()]
        
        # Extrai informações de todos os sócios (no máximo os 3 primeiros)
        for bloco in blocos[:3]:
            if bloco.strip():
                socio_texto = extrair_texto_principal_socio(bloco)
                if socio_texto:
                    socios_textos.append(socio_texto)
                    
                    # Extrai o nome do sócio (primeira parte do texto antes da primeira vírgula)
                    nome_socio = socio_texto.split(',')[0] if ',' in socio_texto else socio_texto
                    socios_nomes.append(nome_socio)
    
    # Verifica se temos pelo menos 2 sócios
    if len(socios_textos) < 2:
        return HttpResponse("Esta empresa não possui múltiplos sócios no cadastro.", status=400)
    
    # Prepara endereço formatado
    logradouro = empresa.endereco.lower() if empresa.endereco else ""
    if logradouro and " " in logradouro:
        partes = logradouro.split(" ")
        logradouro = partes[0].lower() + " " + " ".join(partes[1:])
    
    endereco = f"{logradouro}"
    if empresa.endnumero: endereco += f", nº {empresa.endnumero}"
    if empresa.endcomplemento: endereco += f", {empresa.endcomplemento}"
    if empresa.endbairro: endereco += f", {empresa.endbairro}"
    if empresa.endcep: endereco += f", CEP: {empresa.endcep}"
    if empresa.endcidade: endereco += f", localizado na cidade de {empresa.endcidade}"
    if empresa.endestado: endereco += f"-{empresa.endestado}"
    
    # Processa dados do capital social
    try:
        valor_str = empresa.capitals or "0"
        valor_str = valor_str.replace(".", "").replace(",", ".")
        capital_valor = float(valor_str)
    except ValueError:
        capital_valor = 0
    
    # Divisão de quotas entre sócios
    num_socios = len(socios_textos)
    quotas_por_socio = int(capital_valor) // num_socios
    
    # O primeiro sócio fica com o que sobra da divisão
    resto = int(capital_valor) % num_socios
    
    # Lista de quotas por sócio
    divisao_quotas = []
    for i, nome in enumerate(socios_nomes):
        quotas = quotas_por_socio + (resto if i == 0 else 0)
        valor = quotas * 1.0  # Valor de cada quota é R$ 1,00
        percentual = (quotas / int(capital_valor)) * 100 if capital_valor > 0 else 0
        
        divisao_quotas.append({
            'nome': nome,
            'quotas': str(quotas),
            'quotas_extenso': numero_por_extenso_real(quotas),
            'valor': f"{valor:.2f}".replace(".", ","),
            'valor_extenso': valor_por_extenso_real(valor),
            'percentual': f"{percentual:.2f}"
        })
    
    context = {
        'razao_social': empresa.razaosocial,
        'socios_textos': socios_textos, 
        'socios_nomes': socios_nomes,
        'quantidade_socios': num_socios,
        'divisao_quotas': divisao_quotas,
        'endereco_empresa': endereco,
        'data_inicio_atividade_extenso': format_data_extenso(empresa.empinicioatividade),
        'objeto_social': empresa.objetodoestabelecimento or empresa.ramodeatividade or "",
        'capital_social': f"{capital_valor:.2f}".replace(".", ","),
        'capital_social_extenso': valor_por_extenso_real(capital_valor),
        'quotas': str(int(capital_valor)),
        'quotas_extenso': numero_por_extenso_real(int(capital_valor)),
        'valor_quota': "1,00",
        'valor_quota_extenso': "um real",
        'cidade_empresa': empresa.endcidade or "",
        'uf': empresa.endestado or "",
        'data_contrato_extenso': datetime.now().strftime("%d de %B de %Y").lower(),
    }
    
    # Caminho absoluto do template
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'AberturaSociedadeLTDA.docx')

    doc = DocxTemplate(template_path)
    doc.render(context)
    
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    
    response = HttpResponse(
        buffer.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = f'attachment; filename="Contrato-{empresa.razaosocial}.docx"'
    
    return response

def format_data_extenso(data):
    """
    Recebe uma data (datetime.date, datetime.datetime ou string 'YYYY-MM-DD') e retorna no formato '01 de julho de 2024'.
    """
    import locale
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    except:
        # fallback para sistemas sem locale pt_BR
        pass
    if not data:
        return ""
    if isinstance(data, str):
        try:
            data = datetime.strptime(data, "%Y-%m-%d")
        except Exception:
            try:
                data = datetime.strptime(data, "%d/%m/%Y")
            except Exception:
                return str(data)
    if hasattr(data, 'strftime'):
        return data.strftime("%d de %B de %Y")
    return str(data)

def extrair_texto_principal_socio(socio_texto):
    linhas = socio_texto.split('\n')
    texto_completo = []
    
    # Pula as linhas de cabeçalho
    for i, linha in enumerate(linhas):
        linha_limpa = linha.strip()
        if not linha_limpa:
            continue
        if linha_limpa.startswith('Entrada:') or \
           linha_limpa.startswith('Alteração:') or \
           linha_limpa.startswith('Saída:') or \
           linha_limpa.startswith('Sócio Nº:') or \
           linha_limpa.startswith('Sócio-Administrador'):
            continue
        texto_completo.append(linha_limpa)
    
    return ' '.join(texto_completo)

def valor_por_extenso_real(valor):
    # Implementação básica - utilize uma biblioteca para resultados mais precisos
    valores = {
        0: 'zero',
        1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
        16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
        30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta',
        70: 'setenta', 80: 'oitenta', 90: 'noventa', 100: 'cem',
        1000: 'mil', 1000000: 'milhão', 1000000000: 'bilhão'
    }
    
    if isinstance(valor, str):
        try:
            valor = float(valor.replace(',', '.'))
        except:
            return valor
    
    if valor == 0:
        return 'zero reais'
    
    valor_int = int(valor)
    
    # Implementação simplificada - apenas para alguns casos comuns
    if valor_int == 1:
        return 'um real'
    if valor_int == 1000:
        return 'mil reais'
    if valor_int == 30000:
        return 'trinta mil reais'
    
    # Para outros valores, retorna o valor formatado
    return f"{valor_int} reais"

def numero_por_extenso_real(valor):
    # Implementação básica - utilize uma biblioteca para resultados mais precisos
    if isinstance(valor, str):
        try:
            valor = int(valor.replace(',', '.'))
        except:
            return valor
    
    valor_int = int(valor)
    
    # Implementação simplificada para valores comuns
    if valor_int == 1:
        return 'uma'
    if valor_int == 1000:
        return 'mil'
    if valor_int == 30000:
        return 'trinta mil'
    
    # Para outros valores, retorna o valor formatado
    return f"{valor_int}"

def montar_texto_socio(socio: Socio):
    # Nacionalidade (ajuste conforme seu cadastro)
    nacionalidade = "brasileira" if socio.genero and socio.genero.lower().startswith('f') else "brasileiro"
    # Estado civil (ajuste conforme seu cadastro)
    estado_civil = getattr(socio, 'civil', '') or ""
    # Data de nascimento
    nasc = ""
    if socio.datadenasc:
        if hasattr(socio.datadenasc, 'strftime'):
            nasc = socio.datadenasc.strftime('%d de %B de %Y')
        else:
            try:
                from datetime import datetime
                nasc = datetime.strptime(str(socio.datadenasc), "%Y-%m-%d").strftime('%d de %B de %Y')
            except Exception:
                nasc = str(socio.datadenasc)
    # Endereço
    endereco = ""
    if getattr(socio, 'rua', None):
        endereco += f"{socio.rua}"
    if getattr(socio, 'num', None):
        endereco += f", n.º {socio.num}"
    if getattr(socio, 'complemento', None):
        endereco += f", {socio.complemento}"
    if getattr(socio, 'bairro', None):
        endereco += f", {socio.bairro}"
    if getattr(socio, 'cep', None):
        endereco += f", CEP: {socio.cep}"
    if getattr(socio, 'cidade', None):
        endereco += f", na cidade de {socio.cidade}"
    if getattr(socio, 'estado', None):
        endereco += f"-{socio.estado}"
    # RG
    rg = getattr(socio, 'rg', '') or ""
    orgao = getattr(socio, 'orgaorg', '') or ""
    estado_rg = getattr(socio, 'estadorg', '') or ""
    # CPF
    cpf = getattr(socio, 'cpf', '') or ""
    # Termos flexíveis
    genero = socio.genero.lower() if socio.genero else "masculino"
    portador = "portadora" if genero.startswith("f") else "portador"
    domiciliado = "domiciliada" if genero.startswith("f") else "domiciliado"
    nascido = "nascida" if genero.startswith("f") else "nascido"

    texto = (
        f"{socio.nomecompleto}, {nacionalidade}, {estado_civil}, {nascido} em {nasc}, "
        f"residente e {domiciliado} na {endereco}, {portador} da Cédula da Identidade Civil RG n.º {rg}"
    )
    if orgao or estado_rg:
        texto += f"-{orgao}/{estado_rg}"
    texto += f" e do CPF n.º {cpf}."
    return texto