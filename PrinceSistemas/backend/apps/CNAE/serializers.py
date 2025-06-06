from rest_framework import serializers
from .models import CNAE

class CNAESerializer(serializers.ModelSerializer):
    class Meta:
        model = CNAE
        fields = ['secao', 'divisao', 'grupo', 'classe', 'subclasse', 'descricao']