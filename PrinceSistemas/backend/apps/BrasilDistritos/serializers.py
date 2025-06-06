from rest_framework import serializers
from .models import BrasilDistritos

class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrasilDistritos
        fields = ['id', 'nome', 'id_municipio']