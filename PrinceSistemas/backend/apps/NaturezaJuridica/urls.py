from django.urls import path
from .views import NaturezaJuridicaList

urlpatterns = [
    path('', NaturezaJuridicaList.as_view(), name='natureza-juridica-list'),
]