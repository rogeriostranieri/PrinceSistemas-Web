from django.db import models


class BombeiroCNAE(models.Model):
    ocupacao = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    divisao = models.TextField(blank=True, null=True)
    cnae = models.TextField(primary_key=True)
    carga_de_incendio = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'bombeirocnae'
        managed = False
        verbose_name = 'CNAE Bombeiro'
        verbose_name_plural = 'CNAEs Bombeiro'
    
    def __str__(self):
        return f"{self.cnae} - {self.descricao}"
