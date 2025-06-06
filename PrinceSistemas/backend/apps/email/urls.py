from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailViewSet, EmailCaixaDeSaidaViewSet

router = DefaultRouter()
router.register(r'emails', EmailViewSet)
router.register(r'caixa_saida', EmailCaixaDeSaidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]