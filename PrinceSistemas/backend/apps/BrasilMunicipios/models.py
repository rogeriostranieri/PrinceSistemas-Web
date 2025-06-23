from django.db import models

class BrasilMunicipios(models.Model):
    codigo_ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    capital = models.BooleanField(default=False)
    codigo_uf = models.IntegerField()
    siafi_id = models.CharField(max_length=10)
    ddd = models.CharField(max_length=2)
    fuso_horario = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        db_table = 'BrasilMunicipios'
        managed = False