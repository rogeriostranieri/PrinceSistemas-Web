from django.urls import path, include
from rest_framework import routers
from .views import SocioViewSet

router = routers.DefaultRouter()
router.register(r'', SocioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
