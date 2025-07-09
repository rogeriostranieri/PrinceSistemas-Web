from rest_framework import serializers
from .models import Laudo
from datetime import datetime, date
import re
import logging

logger = logging.getLogger(__name__)

class FlexibleDateField(serializers.Field):
    # Padrões de data
    DATE_PATTERN = r'^\d{2}/\d{2}/\d{4}$'  # DD/MM/YYYY
    DATE_TIME_PATTERN = r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$'  # DD/MM/YYYY HH:MM
    ISO_DATE_PATTERN = r'^\d{4}-\d{2}-\d{2}$'  # YYYY-MM-DD
    ISO_DATE_TIME_PATTERN = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'  # YYYY-MM-DD HH:MM:SS

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
        'null',
        '00/00/0000'
    }

    def to_representation(self, value):
        if not value or str(value).strip() in self.EMPTY_VALUES:
            return None
        if isinstance(value, (datetime, date)):
            return value.strftime('%d/%m/%Y')
        if isinstance(value, str):
            # Tenta converter string para data
            try:
                if re.match(self.DATE_PATTERN, value):
                    return value
                if re.match(self.ISO_DATE_PATTERN, value):
                    return datetime.strptime(value, '%Y-%m-%d').strftime('%d/%m/%Y')
            except Exception:
                return None
        return None

    def to_internal_value(self, data):
        if not data or str(data).strip() in [
            '  /  /', '  /  /    ', '  /  /  :  ', '/', '//', '///', '', 'None', 'null', '00/00/0000'
        ]:
            return None
        if isinstance(data, (datetime, date)):
            return data
        if isinstance(data, str):
            data = data.strip()
            try:
                if re.match(self.DATE_PATTERN, data):
                    return datetime.strptime(data, '%d/%m/%Y').date()
                if re.match(self.ISO_DATE_PATTERN, data):
                    return datetime.strptime(data, '%Y-%m-%d').date()
            except Exception:
                raise serializers.ValidationError("Formato de data inválido.")
        raise serializers.ValidationError("Formato de data inválido.")


class FlexibleDateTimeField(serializers.Field):
    DATE_TIME_PATTERN = r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$'
    ISO_DATE_TIME_NO_TZ_PATTERN = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    EMPTY_PATTERN = r'^\s*/\s*/\s*(:\s*)?$'

    def to_representation(self, value):
        if not value:
            return None
        if isinstance(value, datetime):
            return value.strftime('%d/%m/%Y %H:%M')
        if isinstance(value, date):  # Caso seja um objeto `date`
            return value.strftime('%d/%m/%Y %H:%M')
        if isinstance(value, str):
            value = value.strip()
            try:
                if re.match(self.DATE_TIME_PATTERN, value):
                    return value
                elif re.match(self.ISO_DATE_TIME_NO_TZ_PATTERN, value):
                    dt = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                    return dt.strftime('%d/%m/%Y %H:%M')
                elif re.match(self.EMPTY_PATTERN, value):
                    return None
                else:
                    return None
            except ValueError:
                return None
        return None  # Retorna None para tipos inesperados

    def to_internal_value(self, data):
        if not data or re.match(self.EMPTY_PATTERN, str(data).strip()):
            return None
        data = str(data).strip()
        try:
            if re.match(self.DATE_TIME_PATTERN, data):
                return datetime.strptime(data, '%d/%m/%Y %H:%M')
            elif re.match(self.ISO_DATE_TIME_NO_TZ_PATTERN, data):
                return datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
            else:
                return None
        except ValueError:
            return None


class LaudoSerializer(serializers.ModelSerializer):
    # Date fields (DD/MM/YYYY)
    avisardia = FlexibleDateField(allow_null=True, required=False)
    bombeiros_venc = FlexibleDateField(allow_null=True, required=False)
    ambiental_venc = FlexibleDateField(allow_null=True, required=False)
    viabilidade_vec = FlexibleDateField(allow_null=True, required=False)
    sanitario_venc = FlexibleDateField(allow_null=True, required=False)
    setran_venc = FlexibleDateField(allow_null=True, required=False)
    bombeiro_data_provisorio = FlexibleDateField(allow_null=True, required=False)
    ambiental_data_provisorio = FlexibleDateField(allow_null=True, required=False)
    viabilidade_data_provisorio = FlexibleDateField(allow_null=True, required=False)
    sanitario_data_provisorio = FlexibleDateField(allow_null=True, required=False)
    setran_data_provisorio = FlexibleDateField(allow_null=True, required=False)
    bombeiro_data_ped_processo = FlexibleDateField(allow_null=True, required=False)
    bombeiro_data_multa = FlexibleDateField(allow_null=True, required=False)
    bombeiro_provisorio_data = FlexibleDateField(allow_null=True, required=False)
    ambiental_provisorio_data = FlexibleDateField(allow_null=True, required=False)
    viabilidade_provisorio_data = FlexibleDateField(allow_null=True, required=False)
    sanitario_provisorio_data = FlexibleDateField(allow_null=True, required=False)
    setran_provisorio_data = FlexibleDateField(allow_null=True, required=False)

    # Date-time fields (DD/MM/YYYY HH:mm)
    data_criado = FlexibleDateTimeField(allow_null=True, required=False)
    data_entrada = FlexibleDateTimeField(allow_null=True, required=False)

    # Explicitly define enddata as a CharField since it's a text field
    enddata = serializers.CharField(allow_null=True, required=False)

    lembrete = serializers.BooleanField(required=False, allow_null=True)
    prioridade = serializers.BooleanField(required=False, allow_null=True)

    def validate_lembrete(self, value):
        if isinstance(value, str):
            return value.strip().lower() in ['checked', 'sim', 'true', '1', 't']
        return bool(value)

    def validate_prioridade(self, value):
        if isinstance(value, str):
            return value.strip().lower() in ['checked', 'sim', 'true', '1', 't']
        return bool(value)

    def validate_avisardia(self, value):
        if value in ["  /  /", "", "null", "None", None]:
            return None  # Aceitar valores vazios retornando None
        return value

    def validate(self, data):
        # Limpa datas inválidas
        date_fields = [
            'avisardia', 'bombeiros_venc', 'ambiental_venc', 'viabilidade_vec',
            'sanitario_venc', 'setran_venc', 'bombeiro_data_provisorio',
            'ambiental_data_provisorio', 'viabilidade_data_provisorio',
            'sanitario_data_provisorio', 'setran_data_provisorio',
            'bombeiro_data_ped_processo', 'bombeiro_data_multa',
            'bombeiro_provisorio_data', 'ambiental_provisorio_data',
            'viabilidade_provisorio_data', 'sanitario_provisorio_data',
            'setran_provisorio_data', 'data_criado', 'data_entrada'
        ]
        for field in date_fields:
            val = data.get(field)
            if isinstance(val, str) and val.strip() in [
                '  /  /', '  /  /    ', '  /  /  :  ', '/', '//', '///', '', 'None', 'null', '00/00/0000'
            ]:
                data[field] = None  # Converte para None
        return data

    class Meta:
        model = Laudo
        fields = '__all__'