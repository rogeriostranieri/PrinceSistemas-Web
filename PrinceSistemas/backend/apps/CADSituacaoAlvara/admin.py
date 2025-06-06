from django.contrib import admin
from .models import CADSituacaoAlvara

@admin.register(CADSituacaoAlvara)
class CADSituacaoAlvaraAdmin(admin.ModelAdmin):
    list_display = ('ID_CADSituacaoAlv', 'Descricao')
    search_fields = ('Descricao',)
