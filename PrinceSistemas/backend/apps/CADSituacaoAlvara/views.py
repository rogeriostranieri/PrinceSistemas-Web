from django.shortcuts import render
from rest_framework import viewsets
from .models import CADSituacaoAlvara
from .serializers import CADSituacaoAlvaraSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class CADSituacaoAlvaraViewSet(viewsets.ModelViewSet):
    queryset = CADSituacaoAlvara.objects.all()
    serializer_class = CADSituacaoAlvaraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['ID_CADSituacaoAlv', 'Descricao']
    search_fields = ['Descricao']
    ordering_fields = ['ID_CADSituacaoAlv', 'Descricao']

# Create your views here.
