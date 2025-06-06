from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='telefone_orgao_publico_index'),
    path('telefones/', views.listar_telefones, name='telefone_list'),
    path('telefones/<int:id>/', views.telefone_detail, name='telefone_detail'),
]