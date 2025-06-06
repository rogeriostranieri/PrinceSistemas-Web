from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnotacoesViewSet

router = DefaultRouter()
router.register(r'anotacoes', AnotacoesViewSet, basename='anotacoes')

urlpatterns = [
    path('api/', include(router.urls)),
]