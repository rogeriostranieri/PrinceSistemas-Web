from django.urls import path, include
from rest_framework import routers
from .views import SocioViewSet
from .views_valores import valores_campo_socios

router = routers.DefaultRouter()
router.register(r'', SocioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('valores/<str:campo>/', valores_campo_socios),
]
