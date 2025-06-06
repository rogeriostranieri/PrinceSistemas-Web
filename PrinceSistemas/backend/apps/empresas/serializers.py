from rest_framework import serializers
from .models import Empresa
from datetime import datetime
import re
from django.utils import timezone
import base64
import logging

logger = logging.getLogger(__name__)

class FlexibleDateField(serializers.Field):
    # Regex para detectar formatos válidos
    DATE_PATTERN = r'^\d{2}/\d{2}/\d{4}$'  # DD/MM/YYYY
    DATE_TIME_PATTERN = r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$'  # DD/MM/YYYY HH:MM
    ISO_DATE_PATTERN = r'^\d{4}-\d{2}-\d{2}$'  # YYYY-MM-DD
    ISO_DATE_TIME_PATTERN = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'  # YYYY-MM-DD HH:MM:SS
    ISO_8601_PATTERN = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$'  # YYYY-MM-DDTHH:MM:SS.sssZ
    HTML5_DATETIME_PATTERN = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$'
    HTML5_DATETIME_PATTERN_SEC = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'
    
    # Lista de valores que devem ser tratados como data vazia
    EMPTY_VALUES = {
        '  /  /', 
        '  /  /    ',
        '  /  /  :  ',
        '/',
        '//',
        '///',
        '    /  /  ',
        '  /    /  ',
        '  /  /    ',
        None,
        '',
        'None',
        'null'
    }

    def to_representation(self, value):
        """
        Converte datetime para DD/MM/YYYY HH:MM.
        """
        if not value or str(value).strip() in self.EMPTY_VALUES:
            return None

        # Se for string, tenta limpar e validar
        if isinstance(value, str):
            value = value.strip()
            if value in self.EMPTY_VALUES:
                return None
                
            # Verifica se é uma data/hora válida no formato DD/MM/YYYY HH:MM
            if re.match(r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$', value):
                return value  # já está no formato correto

            # Verifica se é uma data válida no formato DD/MM/YYYY
            if re.match(r'^\d{2}/\d{2}/\d{4}$', value):
                return value

            # Verifica se é uma data válida no formato YYYY-MM-DD
            if re.match(r'^\d{4}-\d{2}-\d{2}$', value):
                try:
                    year, month, day = value.split('-')
                    return f"{day}/{month}/{year} 00:00"
                except:
                    return None

            # Verifica se é uma data/hora válida no formato YYYY-MM-DD HH:MM:SS
            if re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', value):
                try:
                    date_part, time_part = value.split(' ')
                    year, month, day = date_part.split('-')
                    hour, minute, _ = time_part.split(':')
                    return f"{day}/{month}/{year} {hour}:{minute}"
                except:
                    return None

        # Se for datetime/date
        try:
            return value.strftime('%d/%m/%Y %H:%M')
        except:
            try:
                value_str = str(value).strip()
                if value_str in self.EMPTY_VALUES:
                    return None
                return value_str
            except:
                return None

    def to_internal_value(self, data):
        """
        Converte entrada para datetime com fuso horário.
        """
        if not data or str(data).strip() in [
            '  /  /', '  /  /    ', '  /  /  :  ', '/', '//', '///', '', 'None', 'null', '00/00/0000'
        ]:
            return None

        # Limpa a string e verifica se é um valor vazio
        if isinstance(data, str):
            data = data.strip()
            if data in self.EMPTY_VALUES:
                return None

        try:
            if re.match(self.DATE_PATTERN, data):
                dt = datetime.strptime(data, '%d/%m/%Y').replace(hour=0, minute=0, second=0)
                return timezone.make_aware(dt)
            elif re.match(self.DATE_TIME_PATTERN, data):
                dt = datetime.strptime(data, '%d/%m/%Y %H:%M')
                return timezone.make_aware(dt)
            elif re.match(self.HTML5_DATETIME_PATTERN, data):
                dt = datetime.strptime(data, '%Y-%m-%dT%H:%M')
                return timezone.make_aware(dt)
            elif re.match(self.HTML5_DATETIME_PATTERN_SEC, data):
                dt = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S')
                return timezone.make_aware(dt)
            elif re.match(self.ISO_DATE_PATTERN, data):
                dt = datetime.strptime(data, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
                return timezone.make_aware(dt)
            elif re.match(self.ISO_DATE_TIME_PATTERN, data):
                dt = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
                return timezone.make_aware(dt)
            elif re.match(self.ISO_8601_PATTERN, data):
                dt = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%fZ')
                return dt.replace(tzinfo=timezone.utc)
            else:
                return None
        except ValueError as e:
            logger.warning(f"Erro ao converter data '{data}': {e}")
            return None
        except Exception as e:
            logger.error(f"Erro inesperado ao processar data '{data}': {e}")
            return None

class EmpresaSerializer(serializers.ModelSerializer):
    avisarempresa = serializers.CharField(required=False, allow_null=True)
    lembrete = serializers.CharField(required=False, allow_null=True)
    prioridade = serializers.CharField(required=False, allow_null=True)
    # ...outros campos...

    class Meta:
        model = Empresa
        fields = '__all__'

    # Campos de data
    avisardia = FlexibleDateField(allow_null=True)
    prazosimples = FlexibleDateField(allow_null=True)
    empinicioatividade = FlexibleDateField(allow_null=True)
    empcriado = FlexibleDateField(allow_null=True)
    dataprotredesim = FlexibleDateField(allow_null=True)
    dataprotjuntacomercial = FlexibleDateField(allow_null=True)
    datapedidoie = FlexibleDateField(allow_null=True)
    dataregistroalt = FlexibleDateField(allow_null=True)
    datamotivo = FlexibleDateField(allow_null=True)
    ieinicioatividade = FlexibleDateField(allow_null=True)
    ievencpedido = FlexibleDateField(allow_null=True)
    datasimples = FlexibleDateField(allow_null=True)
    dataultdefsimples = FlexibleDateField(allow_null=True)
    dataexcsocial = FlexibleDateField(allow_null=True)
    cnhdataexp = FlexibleDateField(allow_null=True)
    respdatanasc = FlexibleDateField(allow_null=True)
    procuracaodata = FlexibleDateField(allow_null=True)
    nireregistrodata = FlexibleDateField(allow_null=True)
    iedataaltsolicitado = FlexibleDateField(allow_null=True)
    niredata = FlexibleDateField(allow_null=True)
    dbedata = FlexibleDateField(allow_null=True)
    protjuntafinal = FlexibleDateField(allow_null=True)

    # Campo de arquivo
    doccontratos = serializers.SerializerMethodField()
    doccontratos_upload = serializers.CharField(write_only=True, required=False, allow_null=True)

    def validate(self, data):
        """
        Limpa campos de data inválidos e loga dados recebidos.
        """
        logger.debug(f"Dados recebidos para validação: {data}")
        date_fields = [
            'avisardia', 'prazosimples', 'empinicioatividade', 'empcriado',
            'dataprotredesim', 'dataprotjuntacomercial', 'datapedidoie',
            'dataregistroalt', 'datamotivo', 'ieinicioatividade',
            'ievencpedido', 'datasimples', 'dataultdefsimples',
            'dataexcsocial', 'cnhdataexp', 'respdatanasc', 
            'procuracaodata', 'nireregistrodata', 'iedataaltsolicitado',
            'niredata', 'dbedata', 'protjuntafinal'
        ]
        for field in date_fields:
            val = data.get(field)
            if isinstance(val, str) and val.strip() in [
                '  /  /', '  /  /    ', '  /  /  :  ', '/', '//', '///', '', 'None', 'null', '00/00/0000'
            ]:
                data[field] = None
        return data

    def get_doccontratos(self, obj):
        """
        Converte BinaryField para base64.
        """
        if obj.doccontratos:
            try:
                return base64.b64encode(obj.doccontratos).decode('utf-8')
            except Exception as e:
                logger.error(f"Erro ao codificar doccontratos: {e}")
                return None
        return None

    def validate_doccontratos_upload(self, value):
        """
        Valida e decodifica base64 para BinaryField.
        """
        if value:
            try:
                decoded = base64.b64decode(value, validate=True)
                if len(decoded) > 10 * 1024 * 1024:  # 10 MB
                    raise serializers.ValidationError("Arquivo muito grande. Máximo 10 MB.")
                return decoded
            except Exception as e:
                logger.error(f"Erro ao decodificar doccontratos_upload: {e}")
                raise serializers.ValidationError(f"Arquivo inválido: {str(e)}")
        return None

    def update(self, instance, validated_data):
        """
        Atualiza doccontratos a partir de doccontratos_upload.
        """
        if 'doccontratos_upload' in validated_data:
            instance.doccontratos = validated_data.pop('doccontratos_upload')
        return super().update(instance, validated_data)

    def to_internal_value(self, data):
        """
        Converte 'Sim'/'Não' para boolean para os campos lembrete, prioridade e avisarempresa.
        """
        for field in ['lembrete', 'prioridade', 'avisarempresa']:
            if field in data:
                valor = data[field]
                if isinstance(valor, bool):
                    data[field] = 'Sim' if valor else 'Não'
                elif isinstance(valor, str):
                    v = valor.strip().lower()
                    if v in ['sim', 'true', '1', 'checked', 'on']:
                        data[field] = 'Sim'
                    elif v in ['nao', 'não', 'false', '0', 'unchecked', 'off']:
                        data[field] = 'Não'
                    elif v in [None, '', 'null']:
                        data[field] = None
        return super().to_internal_value(data)

    def get_lembrete(self, obj):
        valor = getattr(obj, 'lembrete', '')
        return str(valor).strip().lower() in ['true', '1', 'sim', 'checked', 'on']

    def get_prioridade(self, obj):
        valor = getattr(obj, 'prioridade', '')
        return str(valor).strip().lower() in ['true', '1', 'sim', 'checked', 'on']

    def get_avisarempresa(self, obj):
        valor = obj.avisarempresa or ''
        return str(valor).strip().lower() in ['true', '1', 'sim', 'checked', 'on']

    def validate_lembrete(self, value):
        if isinstance(value, str):
            return value.strip().lower() in ['checked', 'sim', 'true', '1', 't']
        return bool(value)

    def validate_prioridade(self, value):
        if isinstance(value, str):
            return value.strip().lower() in ['checked', 'sim', 'true', '1', 't']
        return bool(value)

    def validate_avisarempresa(self, value):
        """
        Converte valores booleanos para string ao salvar.
        """
        if isinstance(value, bool):
            return 'Sim' if value else 'Não'
        v = str(value).strip().lower()
        return 'Sim' if v in ['true', '1', 'sim', 'checked', 'on'] else 'Não'

    def validate_data_fundacao(self, value):
        if value in ["", " / /", None]:
            return None
        return value

    def validate_avisardia(self, value):
        # Aceita None normalmente
        if value in ["  /  /", "", "null", "None"]:
            return None
        return value