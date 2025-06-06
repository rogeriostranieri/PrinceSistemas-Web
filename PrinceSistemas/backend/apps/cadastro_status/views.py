from rest_framework import viewsets
from .models import CADstatus
from .serializers import CADstatusSerializer

class CADstatusViewSet(viewsets.ModelViewSet):
    queryset = CADstatus.objects.all()
    serializer_class = CADstatusSerializer