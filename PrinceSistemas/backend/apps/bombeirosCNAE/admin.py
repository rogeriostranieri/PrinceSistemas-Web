# admin.py para bombeirosCNAE
from django.contrib import admin
from .models import BombeiroCNAE

@admin.register(BombeiroCNAE)
class BombeiroCNAEAdmin(admin.ModelAdmin):
    list_display = ('ocupacao', 'descricao', 'divisao', 'cnae', 'carga_de_incendio')
