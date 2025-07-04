from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.empresas.views import EmpresaViewSet, AvisosEmpresasView
from apps.socios.views import SocioViewSet
from apps.parcelamentos.views import ParcelamentoViewSet, AvisosParcelamentosView
from apps.laudos.views import LaudoViewSet, AvisosLaudosView
from apps.EventosEmpresa.views import EventosEmpresaViewSet
from apps.NaturezaJuridica.views import NaturezaJuridicaViewSet
from apps.cadastro_status.views import CADstatusViewSet
from apps.BrasilEstados.views import EstadoViewSet  # Corrigido
from apps.BrasilMunicipios.views import MunicipioViewSet  # Corrigido
from apps.BrasilDistritos.views import DistritoViewSet  # Corrigido
from apps.Sites.views import SiteViewSet
from apps.login.views import LoginViewSet, login_view  # Adicionado para a view de login
from .views import backup_database
from apps.Anotacoes.views import AnotacoesViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'socios', SocioViewSet)
router.register(r'parcelamentos', ParcelamentoViewSet)
router.register(r'laudos', LaudoViewSet)
router.register(r'eventosempresa', EventosEmpresaViewSet)
router.register(r'naturezasjuridicas', NaturezaJuridicaViewSet)
router.register(r'cadastro-status', CADstatusViewSet)
router.register(r'estados', EstadoViewSet)  # Corrigido
router.register(r'municipios', MunicipioViewSet)  # Corrigido
router.register(r'distritos', DistritoViewSet)  # Corrigido
router.register(r'sites', SiteViewSet)
router.register(r'login', LoginViewSet)  # Adicionado para o LoginViewSet
router.register(r'anotacoes', AnotacoesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/login/', login_view, name='login_view'),  # Adicionado para acesso direto à view de login
    path('api/auth/', include('apps.login.urls')),
    path('api/cadastro-status/', include('apps.cadastro_status.urls')),
    path('api/avisos-empresas/', AvisosEmpresasView.as_view(), name='avisos-empresas'),
    path('api/avisos-laudos/', AvisosLaudosView.as_view(), name='avisos-laudos'),
    path('api/avisos-parcelamentos/', AvisosParcelamentosView.as_view(), name='avisos-parcelamentos'),
    path('api/', include('apps.laudos.urls')),  # Inclua as URLs do aplicativo 'laudos'
    path('api/', include('apps.parcelamentos.urls')),
    path('', include('apps.CNAE.urls')),  # <-- Adicione esta linha
    path('api/', include('apps.bombeirosCNAE.urls')),
    path('api/integracoes/', include('apps.api_integracoes.urls')),
    path('api/empresas/', include('apps.empresas.urls')),
    # contador
    path('api/contadores/', include('apps.contadores.urls')),
    path('api/email/', include('apps.email.urls')),
    path('api/contatos/', include('apps.Contatos.urls')),
    path('api/telefoneorgaopublico/', include('apps.TelefoneOrgaoPublico.urls')),
    path('api/', include('apps.CADSituacaoAlvara.urls')),
    path('api/backup/', backup_database, name='backup_database'),
    path('api/', include('apps.Anotacoes.urls')),
]