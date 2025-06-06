from rest_framework import serializers
from .models import NaturezaJuridica

class NaturezaJuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturezaJuridica
        fields = ['ID_Naturezajuridica', 'Descricao']