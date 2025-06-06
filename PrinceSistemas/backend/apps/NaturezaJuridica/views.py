from rest_framework import viewsets
from .models import NaturezaJuridica
from .serializers import NaturezaJuridicaSerializer

class NaturezaJuridicaViewSet(viewsets.ModelViewSet):
    queryset = NaturezaJuridica.objects.all()
    serializer_class = NaturezaJuridicaSerializer