from rest_framework import serializers
from .models import Socio
from datetime import datetime, date

class SocioSerializer(serializers.ModelSerializer):
    data_nascimento = serializers.SerializerMethodField()
    menoridade_tipo = serializers.SerializerMethodField()
    
    class Meta:
        model = Socio
        fields = '__all__'  # Isso capturará automaticamente todos os campos, incluindo os novos

    def get_data_nascimento(self, obj):
        data = obj.datadenasc
        if not data:
            return None
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%Y-%m-%d").date()
            except Exception:
                return data
        return data.strftime('%d/%m/%Y')

    def get_menoridade(self, obj):
        data_nasc = obj.datadenasc
        if not data_nasc:
            return None
        # Se for string, converte para date
        if isinstance(data_nasc, str):
            try:
                data_nasc = datetime.strptime(data_nasc, "%Y-%m-%d").date()
            except Exception:
                return None
        hoje = date.today()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        if idade < 0:
            return None
        if idade < 16:
            return "menor impúbere"
        elif idade < 18:
            return "menor púbere"
        else:
            return "maior de idade"

    def get_menoridade_tipo(self, obj):
        """Sugere o tipo de menoridade baseado na idade, mas não sobrescreve o campo salvo."""
        data_nasc = obj.datadenasc
        if not data_nasc:
            return None
        if isinstance(data_nasc, str):
            try:
                data_nasc = datetime.strptime(data_nasc, "%Y-%m-%d").date()
            except Exception:
                return None
        hoje = date.today()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        if idade < 0:
            return None
        if idade < 16:
            return "menor impúbere"
        elif idade < 18:
            return "menor púbere"
        else:
            return None  # maior de idade não precisa sugestão
