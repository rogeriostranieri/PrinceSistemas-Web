from django.contrib import admin
from .models import Telefone

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('ID_Telefones', 'Nome', 'Telefone1', 'TelefoneOutros', 'Obs', 'CEP', 'Endereço', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'Estado', 'email', 'site', 'OrgaoEstado', 'OrgaoCidade')
    search_fields = ('Nome', 'Telefone1', 'Cidade', 'Estado')

admin.site.register(Telefone, TelefoneAdmin)