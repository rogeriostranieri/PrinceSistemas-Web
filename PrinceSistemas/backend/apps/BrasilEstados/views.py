from rest_framework import viewsets
from .models import BrasilEstados
from .serializers import EstadoSerializer

class EstadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BrasilEstados.objects.all()
    serializer_class = EstadoSerializer