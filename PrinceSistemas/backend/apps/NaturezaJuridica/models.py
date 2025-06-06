from django.db import models

class NaturezaJuridica(models.Model):
    ID_Naturezajuridica = models.AutoField(primary_key=True, db_column='ID_Naturezajuridica')
    Descricao = models.TextField(db_column='Descricao')

    def __str__(self):
        return self.Descricao

    class Meta:
        db_table = 'Naturezajuridica'
        managed = False