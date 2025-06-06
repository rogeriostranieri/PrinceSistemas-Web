from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import EventosEmpresa
from .serializers import EventosEmpresaSerializer

class EventosEmpresaViewSet(viewsets.ModelViewSet):
    queryset = EventosEmpresa.objects.all()
    serializer_class = EventosEmpresaSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Adicione os campos abaixo conforme sua necessidade:
    # filterset_fields = ['campo1', 'campo2']
    # search_fields = ['campo1', 'campo2']
    # ordering_fields = ['campo1', 'campo2']