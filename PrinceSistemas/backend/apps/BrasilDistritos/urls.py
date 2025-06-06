from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DistritoViewSet

router = DefaultRouter()
router.register(r'', DistritoViewSet, basename='brasil-distritos')

urlpatterns = [
    path('', include(router.urls)),
]