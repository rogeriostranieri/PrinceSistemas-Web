# urls.py
from django.urls import path
from .views import CNAEListView

urlpatterns = [
    path('api/cnae/', CNAEListView.as_view(), name='cnae-list'),
]