from django.db import models

class BrasilEstados(models.Model):
    codigo_uf = models.IntegerField(primary_key=True)
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    regiao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'BrasilEstado'
        managed = False