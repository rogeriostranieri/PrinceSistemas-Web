# api_integracoes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cnpj/<str:cnpj>/', views.consulta_cnpj, name='consulta_cnpj'),
]