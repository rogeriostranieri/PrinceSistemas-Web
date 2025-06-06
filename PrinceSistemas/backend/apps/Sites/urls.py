from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import SiteViewSet

router = DefaultRouter()
router.register(r'', SiteViewSet, basename='sites')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', views.search_localizacoes, name='search_localizacoes'),
]