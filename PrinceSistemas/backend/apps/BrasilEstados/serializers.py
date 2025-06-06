from rest_framework import serializers
from .models import BrasilEstados

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrasilEstados
        fields = ['codigo_uf', 'uf', 'nome']