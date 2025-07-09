# backend/PrinceSistemas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.empresas.views import EmpresaViewSet
from apps.socios.views import SocioViewSet
from apps.laudos.views import LaudoViewSet
from apps.parcelamentos.views import ParcelamentoViewSet
from .views_mensal import ParcelamentosMensalView
from .views import AvisosParcelamentosView
from .views_valores import valores_campo_parcelamentos

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'socios', SocioViewSet)
router.register(r'laudos', LaudoViewSet)
router.register(r'parcelamentos', ParcelamentoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('avisos-parcelamentos/', AvisosParcelamentosView.as_view(), name='avisos-parcelamentos'),
    path('parcelamentos-mensal/', ParcelamentosMensalView.as_view(), name='parcelamentos-mensal'),
    path('parcelamentos/valores/<str:campo>/', valores_campo_parcelamentos),
]