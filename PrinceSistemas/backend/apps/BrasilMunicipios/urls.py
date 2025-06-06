from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MunicipioViewSet

router = DefaultRouter()
router.register(r'', MunicipioViewSet, basename='brasil-municipios')

urlpatterns = [
    path('', include(router.urls)),
]