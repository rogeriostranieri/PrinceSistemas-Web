from django.contrib import admin
from .models import Anotacoes


@admin.register(Anotacoes)
class AnotacoesAdmin(admin.ModelAdmin):
    list_display = ('ID_Anotacoes', 'Usuario')
    search_fields = ('Usuario',)