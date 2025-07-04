# serializers.py para bombeirosCNAE
from rest_framework import serializers
from .models import BombeiroCNAE

class BombeiroCNAESerializer(serializers.ModelSerializer):
    class Meta:
        model = BombeiroCNAE
        fields = '__all__'
