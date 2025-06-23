from django.db import models

class Contador(models.Model):
    ID_Contador = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=255, blank=True, null=True)
    CPF = models.CharField(max_length=20, blank=True, null=True)
    CRC = models.CharField(max_length=50, blank=True, null=True)
    ExpedicaoCRC = models.CharField(max_length=50, blank=True, null=True)
    RG = models.CharField(max_length=50, blank=True, null=True)
    RazaoSocial = models.TextField(blank=True, null=True)
    CNPJ = models.CharField(max_length=20, blank=True, null=True)
    Telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    CMC = models.CharField(max_length=50, blank=True, null=True)
    Endereco = models.TextField(blank=True, null=True)
    EndNum = models.CharField(max_length=20, blank=True, null=True)
    EndComp = models.TextField(blank=True, null=True)
    EndBairro = models.TextField(blank=True, null=True)
    EndCidade = models.CharField(max_length=100, blank=True, null=True)
    EndEstado = models.CharField(max_length=50, blank=True, null=True)
    EndCEP = models.CharField(max_length=20, blank=True, null=True)
    RGSigla = models.CharField(max_length=10, blank=True, null=True)
    EstadoCivil = models.TextField(blank=True, null=True)
    EstadoCivilDesc = models.TextField(blank=True, null=True)
    DataNasc = models.CharField(max_length=20, blank=True, null=True)
    Genero = models.TextField(blank=True, null=True)
    Profissao = models.TextField(blank=True, null=True)
    NomePai = models.TextField(blank=True, null=True)
    NomeMae = models.TextField(blank=True, null=True)
    email1 = models.TextField(blank=True, null=True)
    email2 = models.TextField(blank=True, null=True)
    Anotacoes = models.TextField(blank=True, null=True)
    IEescritorio = models.TextField(blank=True, null=True)

    class Meta:
        db_table = '"Contador"'
        managed = False
        ordering = ['ID_Contador']

    def __str__(self):
        return self.Nome or ''