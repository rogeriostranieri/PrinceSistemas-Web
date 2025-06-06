from django.db import models

class CADSituacaoAlvara(models.Model):
    ID_CADSituacaoAlv = models.AutoField(primary_key=True)
    Descricao = models.TextField()

    def __str__(self):
        return self.Descricao

    class Meta:
        managed = False  # Django não vai tentar criar ou alterar a tabela
        db_table = 'CADSituacaoAlvara'
        verbose_name = 'Situação do Alvará'
        verbose_name_plural = 'Situações dos Alvarás'