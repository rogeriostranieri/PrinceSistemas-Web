from django.db import models

class CNAE(models.Model):
    secao = models.TextField(db_column='Seção')
    divisao = models.TextField(db_column='Divisão')
    grupo = models.TextField(db_column='Grupo')
    classe = models.TextField(db_column='Classe')
    subclasse = models.TextField(db_column='Subclasse', primary_key=True)
    descricao = models.TextField(db_column='Descrição')

    def __str__(self):
        return f"{self.subclasse} - {self.descricao}"

    class Meta:
        db_table = 'CNAESubclasses23'
        managed = False
        ordering = ['secao', 'divisao', 'grupo', 'classe', 'subclasse']