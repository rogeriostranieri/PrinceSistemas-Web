from django.urls import path, include
from rest_framework import routers
from apps.contadores.views import ContadorViewSet

router = routers.DefaultRouter()
router.register(r'', ContadorViewSet)  # Rota vazia para /api/contadores/

urlpatterns = router.urls