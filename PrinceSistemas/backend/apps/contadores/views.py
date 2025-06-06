from rest_framework import viewsets
from .models import Contador
from .serializers import ContadorSerializer

class ContadorViewSet(viewsets.ModelViewSet):
    queryset = Contador.objects.all()
    serializer_class = ContadorSerializer