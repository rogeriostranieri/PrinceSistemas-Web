from rest_framework import serializers
from .models import BrasilMunicipios

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrasilMunicipios
        fields = ['codigo_ibge', 'nome', 'codigo_uf']