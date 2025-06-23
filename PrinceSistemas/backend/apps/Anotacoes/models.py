from django.db import models


class Anotacoes(models.Model):
    ID_Anotacoes = models.AutoField(primary_key=True)
    Usuario = models.CharField(max_length=255, null=True, blank=True)
    Federal = models.TextField(null=True, blank=True)
    Estadual = models.TextField(null=True, blank=True)
    Municipal = models.TextField(null=True, blank=True)
    Inicial = models.TextField(null=True, blank=True)
    Demais = models.TextField(null=True, blank=True)
    Legalizacao = models.TextField(null=True, blank=True)
    Anexos = models.TextField(null=True, blank=True)
    Anexo1 = models.TextField(null=True, blank=True)
    Anexo2 = models.TextField(null=True, blank=True)
    Anexo3 = models.TextField(null=True, blank=True)
    Anexo4 = models.TextField(null=True, blank=True)
    Anexo5 = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['ID_Anotacoes']
        db_table = "Anotacoes"
        verbose_name = "Anotação"
        verbose_name_plural = "Anotações"
        managed = False  # Importante para indicar que a tabela já existe

    def __str__(self):
        return f"Anotação {self.ID_Anotacoes} - {self.Usuario}"