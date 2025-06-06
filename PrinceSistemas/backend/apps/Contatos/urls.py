from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_contatos, name='contato-list'),
    path('<int:id>/', views.detalhe_contato, name='contato-detail'),
]