from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (EmpresaViewSet, empresas_reminders, exportar_empresa_resumida_pdf,
                   gerar_contrato_word, gerar_contrato_word_multiplos_socios)
from .views_valores import valores_campo_empresas

router = DefaultRouter()
router.register(r'', EmpresaViewSet, basename='Empresa')

urlpatterns = [
    path('', include(router.urls)),  # Rotas CRUD: /api/empresas/
    path('reminders/', empresas_reminders, name='empresa-reminders'),
    path('<int:empresa_id>/exportar-resumida/', exportar_empresa_resumida_pdf, name='exportar_empresa_resumida_pdf'),
    path('gerar-contrato-word/<int:empresa_id>/', gerar_contrato_word, name='gerar_contrato_word'),
    path('gerar-contrato-multiplos-socios/<int:empresa_id>/', gerar_contrato_word_multiplos_socios, name='gerar_contrato_multiplos_socios'),
    path('valores/<str:campo>/', valores_campo_empresas),
]
