from rest_framework import serializers
from .models import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['id_login', 'usuario', 'senha', 'nome_completo', 'email', 'tema', 'datanascimento', 'nivel_acesso']
        extra_kwargs = {
            'senha': {'write_only': True, 'required': False}
        }