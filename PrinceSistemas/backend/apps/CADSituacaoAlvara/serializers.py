from rest_framework import serializers
from .models import CADSituacaoAlvara

class CADSituacaoAlvaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CADSituacaoAlvara
        fields = ['ID_CADSituacaoAlv', 'Descricao']