from rest_framework import serializers
from .models import Anotacoes


class AnotacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anotacoes
        fields = '__all__'