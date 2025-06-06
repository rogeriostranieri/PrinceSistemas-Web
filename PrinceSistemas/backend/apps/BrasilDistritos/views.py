from rest_framework import viewsets
from .models import BrasilDistritos
from .serializers import DistritoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class DistritoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BrasilDistritos.objects.all()
    serializer_class = DistritoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_municipio']