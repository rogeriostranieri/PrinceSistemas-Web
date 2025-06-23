from django.db import models

class CADstatus(models.Model):
    ID_CADstatus = models.AutoField(primary_key=True)
    Descricao = models.CharField(max_length=100)

    class Meta:
        ordering = ['ID_CADstatus']
        db_table = 'CADstatus'

    def __str__(self):
        return self.Descricao