from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.empresas.views import EmpresaViewSet
from apps.socios.views import SocioViewSet
from apps.laudos.views import LaudoViewSet
from apps.parcelamentos.views import ParcelamentoViewSet
from .views import AvisosDiaView
from apps.laudos import views

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'socios', SocioViewSet)
router.register(r'laudos', LaudoViewSet, basename='laudos')
router.register(r'parcelamentos', ParcelamentoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('avisos-dia/', AvisosDiaView.as_view(), name='avisos-dia'),
    path('laudos/<int:laudo_id>/declaracao-extravio/', views.declaracao_extravio_pdf, name='declaracao_extravio_pdf')
]