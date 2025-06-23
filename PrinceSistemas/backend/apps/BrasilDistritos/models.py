from django.db import models

class BrasilDistritos(models.Model):
    id = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField()
    id_microrregiao = models.IntegerField()
    id_mesorregiao = models.IntegerField()
    id_estado = models.IntegerField()
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['id']
        db_table = 'BrasilDistritos'
        managed = False  # Django não gerencia esta tabela