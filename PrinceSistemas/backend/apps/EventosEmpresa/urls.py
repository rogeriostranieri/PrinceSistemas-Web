from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventosEmpresaViewSet

router = DefaultRouter()
router.register(r'eventosempresa', EventosEmpresaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]