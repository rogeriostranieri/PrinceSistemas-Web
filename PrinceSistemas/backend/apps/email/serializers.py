from rest_framework import serializers
from .models import Email, Emailcaixadesaida

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class EmailCaixaDeSaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emailcaixadesaida
        fields = '__all__'
        read_only_fields = ['id_emailcaixadesaida']