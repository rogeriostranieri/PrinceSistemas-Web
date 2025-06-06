from rest_framework import viewsets
from .models import BrasilMunicipios
from .serializers import MunicipioSerializer
from django_filters.rest_framework import DjangoFilterBackend

class MunicipioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BrasilMunicipios.objects.all()
    serializer_class = MunicipioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['codigo_uf']