from rest_framework import serializers
from .models import CADstatus

class CADstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CADstatus
        fields = ['ID_CADstatus', 'Descricao']