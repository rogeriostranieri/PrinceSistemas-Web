from django.shortcuts import render
from rest_framework import generics
from .models import CNAE
from .serializers import CNAESerializer

# Create your views here.

class CNAEListView(generics.ListAPIView):
    queryset = CNAE.objects.all()
    serializer_class = CNAESerializer
