from django.db import models

class EventosEmpresa(models.Model):
    id_eventos_empresa = models.AutoField(primary_key=True, db_column='ID_EventosEmpresa')
    eventos = models.CharField(max_length=255, db_column='Eventos')
    empresa_facil = models.BooleanField(default=False, db_column='EmpresaFacil')
    receita_federal = models.BooleanField(default=False, db_column='ReceitaFederal')
    receita_estadual = models.BooleanField(default=False, db_column='ReceitaEstadual')
    prefeitura_municipal = models.BooleanField(default=False, db_column='PrefeituraMunicipal')
    eventos_descricao_titulo = models.CharField(max_length=255, db_column='EventosDescriçãoTitulo')
    eventos_descricao = models.TextField(db_column='EventosDescrição')

    def __str__(self):
        return self.eventos_descricao_titulo

    class Meta:
        db_table = 'EventosEmpresa'
        managed = False