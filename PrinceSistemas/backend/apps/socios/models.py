from django.db import models

class Socio(models.Model):
    id_socios = models.AutoField(primary_key=True, db_column='ID_Socios')
    cpf = models.CharField(max_length=50, db_column='CPF')
    nomecompleto = models.CharField(max_length=255, db_column='NomeCompleto')
    nomemae = models.CharField(max_length=255, blank=True, null=True, db_column='NomeMae')
    nomepai = models.CharField(max_length=255, blank=True, null=True, db_column='NomePai')
    datadenasc = models.DateField(blank=True, null=True, db_column='DatadeNasc')
    rg = models.CharField(max_length=50, blank=True, null=True, db_column='RG')
    orgaorg = models.CharField(max_length=50, blank=True, null=True, db_column='OrgaoRG')
    estadorg = models.CharField(max_length=50, blank=True, null=True, db_column='EstadoRG')
    titulodeeleitor = models.CharField(max_length=50, blank=True, null=True, db_column='TituloDeEleitor')
    senhagov = models.CharField(max_length=255, blank=True, null=True, db_column='SenhaGOV')
    cnh = models.CharField(max_length=50, blank=True, null=True, db_column='CNH')
    cnhexpedicao = models.DateField(blank=True, null=True, db_column='CNHExpedicao')
    cnhdataexp = models.DateField(blank=True, null=True, db_column='CNHDataExp')
    civil = models.CharField(max_length=50, blank=True, null=True, db_column='Civil')
    cep = models.CharField(max_length=20, blank=True, null=True, db_column='CEP')
    rua = models.CharField(max_length=255, blank=True, null=True, db_column='RUA')
    num = models.CharField(max_length=50, blank=True, null=True, db_column='Num')
    bairro = models.CharField(max_length=100, blank=True, null=True, db_column='Bairro')
    complemento = models.CharField(max_length=255, blank=True, null=True, db_column='Complemento')
    cidade = models.CharField(max_length=100, blank=True, null=True, db_column='Cidade')
    estado = models.CharField(max_length=100, blank=True, null=True, db_column='Estado')
    pais = models.CharField(max_length=100, blank=True, null=True, db_column='País')
    telefone1 = models.CharField(max_length=50, blank=True, null=True, db_column='Telefone1')
    telefone2 = models.CharField(max_length=50, blank=True, null=True, db_column='Telefone2')
    email = models.EmailField(blank=True, null=True, db_column='eMail')
    genero = models.CharField(max_length=20, blank=True, null=True, db_column='Genero')
    cpfdoconjuge = models.CharField(max_length=50, blank=True, null=True, db_column='CPFdoCONJUGE')
    nomedoconjuge = models.CharField(max_length=255, blank=True, null=True, db_column='NOMEdoCONJUGE')
    profissao = models.CharField(max_length=100, blank=True, null=True, db_column='Profissão')
    outrosdados = models.TextField(blank=True, null=True, db_column='OutrosDados')
    menoridade = models.CharField(max_length=50, blank=True, null=True, db_column='MenorIdade')
    registroorgao = models.CharField(max_length=50, blank=True, null=True, db_column='RegistroOrgao')
    registroestado = models.CharField(max_length=50, blank=True, null=True, db_column='RegistroEstado')
    registronumero = models.CharField(max_length=50, blank=True, null=True, db_column='RegistroNumero')
    registrodata = models.DateField(blank=True, null=True, db_column='RegistroData')
    
    # Novos campos para capacidade civil
    capacidade_civil = models.CharField(max_length=255, blank=True, null=True, db_column='capacidade_civil')
    requisitos_legais = models.CharField(max_length=255, blank=True, null=True, db_column='requisitos_legais')
    representante_legal = models.CharField(max_length=255, blank=True, null=True, db_column='representante_legal')
    autorizacao_judicial = models.BooleanField(default=False, blank=True, null=True, db_column='autorizacao_judicial')
    numero_processo = models.CharField(max_length=255, blank=True, null=True, db_column='numero_processo')
    data_autorizacao = models.DateField(blank=True, null=True, db_column='data_autorizacao')
    tipo_emancipacao = models.CharField(max_length=255, blank=True, null=True, db_column='tipo_emancipacao')
    data_emancipacao = models.DateField(blank=True, null=True, db_column='data_emancipacao')
    registro_emancipacao = models.CharField(max_length=255, blank=True, null=True, db_column='registro_emancipacao')

    class Meta:
        db_table = "Socios"
        managed = False  # Mantido como False, pois a tabela já existe
        ordering = ['nomecompleto']

    def __str__(self):
        return self.nomecompleto