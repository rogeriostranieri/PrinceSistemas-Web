from rest_framework import serializers
from .models import Sites

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = '__all__'