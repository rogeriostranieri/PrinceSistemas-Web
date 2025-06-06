from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CADstatusViewSet

router = DefaultRouter()
router.register(r'cadastro-status', CADstatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]