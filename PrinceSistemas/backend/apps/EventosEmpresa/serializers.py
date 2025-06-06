from rest_framework import serializers
from .models import EventosEmpresa

class EventosEmpresaSerializer(serializers.ModelSerializer):
    empresa_facil = serializers.SerializerMethodField()
    receita_federal = serializers.SerializerMethodField()
    receita_estadual = serializers.SerializerMethodField()
    prefeitura_municipal = serializers.SerializerMethodField()

    def get_empresa_facil(self, obj):
        return str(obj.empresa_facil).lower() in ["checked", "sim", "true", "1"]

    def get_receita_federal(self, obj):
        return str(obj.receita_federal).lower() in ["checked", "sim", "true", "1"]

    def get_receita_estadual(self, obj):
        return str(obj.receita_estadual).lower() in ["checked", "sim", "true", "1"]

    def get_prefeitura_municipal(self, obj):
        return str(obj.prefeitura_municipal).lower() in ["checked", "sim", "true", "1"]

    def to_internal_value(self, data):
        data = data.copy()
        def parse_bool(val):
            return str(val).lower() in ["checked", "sim", "true", "1"]
        data['empresa_facil'] = parse_bool(data.get('empresa_facil', False))
        data['receita_federal'] = parse_bool(data.get('receita_federal', False))
        data['receita_estadual'] = parse_bool(data.get('receita_estadual', False))
        data['prefeitura_municipal'] = parse_bool(data.get('prefeitura_municipal', False))
        return super().to_internal_value(data)

    class Meta:
        model = EventosEmpresa
        fields = '__all__'