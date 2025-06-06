from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Anotacoes
from .serializers import AnotacoesSerializer


class AnotacoesViewSet(viewsets.ModelViewSet):
    queryset = Anotacoes.objects.all().order_by('ID_Anotacoes')
    serializer_class = AnotacoesSerializer

    def get_queryset(self):
        queryset = Anotacoes.objects.all()
        usuario = self.request.query_params.get('usuario', None)
        if usuario:
            queryset = queryset.filter(Usuario__icontains=usuario)
        return queryset