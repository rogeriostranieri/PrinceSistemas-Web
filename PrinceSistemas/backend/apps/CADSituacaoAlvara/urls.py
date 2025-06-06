from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CADSituacaoAlvaraViewSet

router = DefaultRouter()
# Registre a rota com o nome que você quer acessar (CADSituacaoAlvara em vez de cadsituacaoalvara)
router.register(r'CADSituacaoAlvara', CADSituacaoAlvaraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]