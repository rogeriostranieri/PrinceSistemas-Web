from django.urls import path
from . import views

urlpatterns = [
    path('bombeiros-cnae/', views.lista_bombeiros_cnae, name='lista_bombeiros_cnae'),
]
