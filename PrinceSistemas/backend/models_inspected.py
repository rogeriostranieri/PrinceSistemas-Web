# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ajudaempresafacil(models.Model):
    id_ajudaempresafacil = models.AutoField(db_column='ID_AjudaEmpresaFacil', primary_key=True)  # Field name made lowercase.
    empresafaciltipounidade = models.TextField(db_column='EmpresaFacilTipoUnidade', blank=True, null=True)  # Field name made lowercase.
    empresafacilformaatuacao = models.TextField(db_column='EmpresaFacilFormaAtuacao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AjudaEmpresaFacil'


class Alvarasistema(models.Model):
    id_sistema = models.AutoField(db_column='ID_Sistema', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlvaraSistema'


class Anotacoes(models.Model):
    id_anotacoes = models.AutoField(db_column='ID_Anotacoes', primary_key=True)  # Field name made lowercase.
    usuario = models.TextField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    federal = models.TextField(db_column='Federal', blank=True, null=True)  # Field name made lowercase.
    estadual = models.TextField(db_column='Estadual', blank=True, null=True)  # Field name made lowercase.
    municipal = models.TextField(db_column='Municipal', blank=True, null=True)  # Field name made lowercase.
    inicial = models.TextField(db_column='Inicial', blank=True, null=True)  # Field name made lowercase.
    demais = models.TextField(db_column='Demais', blank=True, null=True)  # Field name made lowercase.
    legalizacao = models.TextField(db_column='Legalizacao', blank=True, null=True)  # Field name made lowercase.
    anexos = models.BinaryField(db_column='Anexos', blank=True, null=True)  # Field name made lowercase.
    anexo1 = models.BinaryField(db_column='Anexo1', blank=True, null=True)  # Field name made lowercase.
    anexo2 = models.BinaryField(db_column='Anexo2', blank=True, null=True)  # Field name made lowercase.
    anexo3 = models.BinaryField(db_column='Anexo3', blank=True, null=True)  # Field name made lowercase.
    anexo4 = models.BinaryField(db_column='Anexo4', blank=True, null=True)  # Field name made lowercase.
    anexo5 = models.BinaryField(db_column='Anexo5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anotacoes'


class Avisos(models.Model):
    id_avisos = models.AutoField(db_column='ID_Avisos', primary_key=True)  # Field name made lowercase.
    avisar = models.CharField(db_column='Avisar', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dataaviso = models.DateTimeField(db_column='DataAviso', blank=True, null=True)  # Field name made lowercase.
    textoaviso = models.TextField(db_column='TextoAviso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Avisos'


class Bombeirosituacao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BombeiroSituacao'


class Brasildistritos(models.Model):
    id = models.IntegerField(primary_key=True)
    id_municipio = models.IntegerField(blank=True, null=True)
    id_microrregiao = models.IntegerField(blank=True, null=True)
    id_mesorregiao = models.IntegerField(blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BrasilDistritos'


class Brasilestado(models.Model):
    codigo_uf = models.IntegerField(primary_key=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    regiao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BrasilEstado'


class Brasilmunicipios(models.Model):
    codigo_ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    capital = models.BooleanField(blank=True, null=True)
    codigo_uf = models.IntegerField(blank=True, null=True)
    siafi_id = models.IntegerField(blank=True, null=True)
    ddd = models.IntegerField(blank=True, null=True)
    fuso_horario = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BrasilMunicipios'


class Cadsituacaoalvara(models.Model):
    id_cadsituacaoalv = models.AutoField(db_column='ID_CADSituacaoAlv', primary_key=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CADSituacaoAlvara'


class Cadstatus(models.Model):
    id_cadstatus = models.AutoField(db_column='ID_CADstatus', primary_key=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CADstatus'


class Cnae(models.Model):
    id_cnae = models.SmallAutoField(db_column='ID_CNAE', primary_key=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase.
    seþÒo = models.TextField(db_column='SeþÒo', blank=True, null=True)  # Field name made lowercase.
    divisÒo = models.IntegerField(db_column='DivisÒo', blank=True, null=True)  # Field name made lowercase.
    grupo = models.FloatField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    classe = models.TextField(db_column='Classe', blank=True, null=True)  # Field name made lowercase.
    denominaþÒo = models.TextField(db_column='DenominaþÒo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CNAE'


class Cnae20Classes(models.Model):
    seþÒo = models.CharField(db_column='SeþÒo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    divisÒo = models.CharField(db_column='DivisÒo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classe = models.CharField(db_column='Classe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    denominaþÒo = models.CharField(db_column='DenominaþÒo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CNAE 2.0 Classes'


class Cnaesubclasses23(models.Model):
    seþÒo = models.TextField(db_column='SeþÒo', blank=True, null=True)  # Field name made lowercase.
    divisÒo = models.TextField(db_column='DivisÒo', blank=True, null=True)  # Field name made lowercase.
    grupo = models.TextField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    classe = models.TextField(db_column='Classe', blank=True, null=True)  # Field name made lowercase.
    subclasse = models.TextField(db_column='Subclasse', blank=True, null=True)  # Field name made lowercase.
    descriþÒo = models.TextField(db_column='DescriþÒo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CNAESubclasses23'


class Cnaeprefmaringapr(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cnae = models.TextField(db_column='CNAE', blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase.
    grauderisco = models.TextField(db_column='GrauDeRisco', blank=True, null=True)  # Field name made lowercase.
    condicionante = models.TextField(db_column='Condicionante', blank=True, null=True)  # Field name made lowercase.
    grauriscodesenq = models.TextField(db_column='GrauRiscoDesenq', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CNAEprefMaringaPR'


class Contador(models.Model):
    id_contador = models.SmallAutoField(db_column='ID_Contador', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crc = models.CharField(db_column='CRC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expedicaocrc = models.CharField(db_column='ExpedicaoCRC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razaosocial = models.TextField(db_column='RazaoSocial', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(blank=True, null=True)
    cmc = models.CharField(db_column='CMC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endereco = models.TextField(db_column='Endereco', blank=True, null=True)  # Field name made lowercase.
    endnum = models.CharField(db_column='EndNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endcomp = models.TextField(db_column='EndComp', blank=True, null=True)  # Field name made lowercase.
    endbairro = models.TextField(db_column='EndBairro', blank=True, null=True)  # Field name made lowercase.
    endcidade = models.CharField(db_column='EndCidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endestado = models.CharField(db_column='EndEstado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endcep = models.CharField(db_column='EndCEP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rgsigla = models.CharField(db_column='RGSigla', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estadocivil = models.TextField(db_column='EstadoCivil', blank=True, null=True)  # Field name made lowercase.
    estadocivildesc = models.TextField(db_column='EstadoCivilDesc', blank=True, null=True)  # Field name made lowercase.
    datanasc = models.CharField(db_column='DataNasc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    genero = models.TextField(db_column='Genero', blank=True, null=True)  # Field name made lowercase.
    profissao = models.TextField(db_column='Profissao', blank=True, null=True)  # Field name made lowercase.
    nomepai = models.TextField(db_column='NomePai', blank=True, null=True)  # Field name made lowercase.
    nomemae = models.TextField(db_column='NomeMae', blank=True, null=True)  # Field name made lowercase.
    email1 = models.TextField(blank=True, null=True)
    email2 = models.TextField(blank=True, null=True)
    anotacoes = models.TextField(db_column='Anotacoes', blank=True, null=True)  # Field name made lowercase.
    ieescritorio = models.TextField(db_column='IEescritorio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contador'


class Contatos(models.Model):
    id_contatos = models.SmallAutoField(db_column='ID_Contatos', primary_key=True)  # Field name made lowercase.
    nome = models.TextField(db_column='Nome', blank=True, null=True)  # Field name made lowercase.
    sobrenome = models.TextField(db_column='Sobrenome', blank=True, null=True)  # Field name made lowercase.
    telefone_residencial = models.TextField(db_column='Telefone_Residencial', blank=True, null=True)  # Field name made lowercase.
    telefone_trabalho = models.TextField(db_column='Telefone_Trabalho', blank=True, null=True)  # Field name made lowercase.
    telefone_celular_particular = models.TextField(db_column='Telefone_Celular_Particular', blank=True, null=True)  # Field name made lowercase.
    telefone_celular_contato = models.TextField(db_column='Telefone_Celular_Contato', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(blank=True, null=True)
    end_cep = models.TextField(db_column='End_CEP', blank=True, null=True)  # Field name made lowercase.
    end_rua = models.TextField(db_column='End_Rua', blank=True, null=True)  # Field name made lowercase.
    end_numero = models.TextField(db_column='End_Numero', blank=True, null=True)  # Field name made lowercase.
    end_comp = models.TextField(db_column='End_Comp', blank=True, null=True)  # Field name made lowercase.
    end_bairro = models.TextField(db_column='End_Bairro', blank=True, null=True)  # Field name made lowercase.
    end_cidade = models.TextField(db_column='End_Cidade', blank=True, null=True)  # Field name made lowercase.
    end_estado = models.TextField(db_column='End_Estado', blank=True, null=True)  # Field name made lowercase.
    end_pais = models.TextField(db_column='End_Pais', blank=True, null=True)  # Field name made lowercase.
    outras_informacoes = models.TextField(db_column='Outras_Informacoes', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contatos'


class Empresas(models.Model):
    id_empresas = models.SmallAutoField(db_column='ID_Empresas', primary_key=True)  # Field name made lowercase.
    razaosocial = models.TextField(db_column='RazaoSocial', blank=True, null=True)  # Field name made lowercase.
    nomefantasia = models.TextField(db_column='NomeFantasia', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.TextField(db_column='CNPJ', blank=True, null=True)  # Field name made lowercase.
    endereco = models.TextField(db_column='Endereco', blank=True, null=True)  # Field name made lowercase.
    endnumero = models.TextField(db_column='EndNumero', blank=True, null=True)  # Field name made lowercase.
    endbairro = models.TextField(db_column='EndBairro', blank=True, null=True)  # Field name made lowercase.
    endcomplemento = models.TextField(db_column='EndComplemento', blank=True, null=True)  # Field name made lowercase.
    endcep = models.TextField(db_column='EndCEP', blank=True, null=True)  # Field name made lowercase.
    endcidade = models.TextField(db_column='EndCidade', blank=True, null=True)  # Field name made lowercase.
    endestado = models.TextField(db_column='EndEstado', blank=True, null=True)  # Field name made lowercase.
    endpais = models.TextField(db_column='EndPais', blank=True, null=True)  # Field name made lowercase.
    emptel1 = models.TextField(db_column='EmpTel1', blank=True, null=True)  # Field name made lowercase.
    emptel2 = models.TextField(db_column='EmpTel2', blank=True, null=True)  # Field name made lowercase.
    empemail = models.TextField(db_column='EmpEmail', blank=True, null=True)  # Field name made lowercase.
    paginaweb = models.TextField(db_column='PaginaWeb', blank=True, null=True)  # Field name made lowercase.
    ie = models.TextField(db_column='IE', blank=True, null=True)  # Field name made lowercase.
    im = models.TextField(db_column='IM', blank=True, null=True)  # Field name made lowercase.
    naturezajuridica = models.TextField(db_column='NaturezaJuridica', blank=True, null=True)  # Field name made lowercase.
    empinicioatividade = models.DateTimeField(db_column='EmpInicioAtividade', blank=True, null=True)  # Field name made lowercase.
    empcriado = models.DateTimeField(db_column='EmpCriado', blank=True, null=True)  # Field name made lowercase.
    processo = models.TextField(db_column='Processo', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    nire = models.TextField(db_column='NIRE', blank=True, null=True)  # Field name made lowercase.
    cnaeprincipal = models.TextField(db_column='CNAEPrincipal', blank=True, null=True)  # Field name made lowercase.
    cnaesecundario = models.TextField(db_column='CNAESecundario', blank=True, null=True)  # Field name made lowercase.
    ramodeatividade = models.TextField(db_column='RamoDeAtividade', blank=True, null=True)  # Field name made lowercase.
    responsavelcpf = models.TextField(db_column='ResponsavelCPF', blank=True, null=True)  # Field name made lowercase.
    responsavelnome = models.TextField(db_column='ResponsavelNome', blank=True, null=True)  # Field name made lowercase.
    protocolojuntacomercial = models.TextField(db_column='ProtocoloJuntaComercial', blank=True, null=True)  # Field name made lowercase.
    geral = models.TextField(db_column='Geral', blank=True, null=True)  # Field name made lowercase.
    lembrete = models.BooleanField(db_column='Lembrete', blank=True, null=True)  # Field name made lowercase.
    protocoloredesim = models.TextField(db_column='ProtocoloREDESIM', blank=True, null=True)  # Field name made lowercase.
    dataprotredesim = models.DateTimeField(db_column='DataProtREDESIM', blank=True, null=True)  # Field name made lowercase.
    dataprotjuntacomercial = models.DateTimeField(db_column='DataProtJuntaComercial', blank=True, null=True)  # Field name made lowercase.
    datapedidoie = models.DateTimeField(db_column='DataPedidoIE', blank=True, null=True)  # Field name made lowercase.
    avisardia = models.DateTimeField(db_column='AvisarDia', blank=True, null=True)  # Field name made lowercase.
    prazosimples = models.DateTimeField(db_column='PrazoSimples', blank=True, null=True)  # Field name made lowercase.
    nirealt = models.TextField(db_column='NireAlt', blank=True, null=True)  # Field name made lowercase.
    juntaobs = models.TextField(db_column='JuntaObs', blank=True, null=True)  # Field name made lowercase.
    nregistroalt = models.TextField(db_column='NRegistroAlt', blank=True, null=True)  # Field name made lowercase.
    dataregistroalt = models.DateTimeField(db_column='DataRegistroAlt', blank=True, null=True)  # Field name made lowercase.
    nireantigos = models.TextField(db_column='NireAntigos', blank=True, null=True)  # Field name made lowercase.
    nalteracao = models.TextField(db_column='NAlteracao', blank=True, null=True)  # Field name made lowercase.
    redesimobs = models.TextField(db_column='RedeSimObs', blank=True, null=True)  # Field name made lowercase.
    estadualobs = models.TextField(db_column='EstadualObs', blank=True, null=True)  # Field name made lowercase.
    prefeituraobs = models.TextField(db_column='PrefeituraObs', blank=True, null=True)  # Field name made lowercase.
    codigosimples = models.TextField(db_column='CodigoSimples', blank=True, null=True)  # Field name made lowercase.
    cpfresponsavel = models.TextField(db_column='CPFResponsavel', blank=True, null=True)  # Field name made lowercase.
    nomeresponsavel = models.TextField(db_column='NomeResponsavel', blank=True, null=True)  # Field name made lowercase.
    arquivocontrato = models.TextField(db_column='ArquivoContrato', blank=True, null=True)  # Field name made lowercase.
    procedimento = models.TextField(db_column='Procedimento', blank=True, null=True)  # Field name made lowercase.
    prioridade = models.BooleanField(db_column='Prioridade', blank=True, null=True)  # Field name made lowercase.
    regimefederal = models.TextField(db_column='RegimeFederal', blank=True, null=True)  # Field name made lowercase.
    portedaempresa = models.TextField(db_column='PorteDaEmpresa', blank=True, null=True)  # Field name made lowercase.
    tipodeempresa = models.TextField(db_column='TipoDeEmpresa', blank=True, null=True)  # Field name made lowercase.
    altconsolidada = models.TextField(db_column='AltConsolidada', blank=True, null=True)  # Field name made lowercase.
    motivo = models.TextField(db_column='Motivo', blank=True, null=True)  # Field name made lowercase.
    datamotivo = models.DateTimeField(db_column='DataMotivo', blank=True, null=True)  # Field name made lowercase.
    iecomprovante = models.TextField(db_column='IEComprovante', blank=True, null=True)  # Field name made lowercase.
    ieinicioatividade = models.DateTimeField(db_column='IEInicioAtividade', blank=True, null=True)  # Field name made lowercase.
    ievencpedido = models.DateTimeField(db_column='IEVencPedido', blank=True, null=True)  # Field name made lowercase.
    bombeirojunta = models.TextField(db_column='BombeiroJunta', blank=True, null=True)  # Field name made lowercase.
    iejunta = models.TextField(db_column='IEjunta', blank=True, null=True)  # Field name made lowercase.
    protjuntafinal = models.DateTimeField(db_column='ProtJuntaFinal', blank=True, null=True)  # Field name made lowercase.
    tituloeleitor = models.TextField(db_column='Tituloeleitor', blank=True, null=True)  # Field name made lowercase.
    area = models.TextField(blank=True, null=True)
    area2 = models.TextField(blank=True, null=True)
    obssimples = models.TextField(db_column='ObsSimples', blank=True, null=True)  # Field name made lowercase.
    datasimples = models.DateTimeField(db_column='DataSimples', blank=True, null=True)  # Field name made lowercase.
    dataultdefsimples = models.DateTimeField(db_column='DataUltdefSimples', blank=True, null=True)  # Field name made lowercase.
    orgÒopedsimples = models.TextField(db_column='OrgÒoPedSimples', blank=True, null=True)  # Field name made lowercase.
    pastadocumentos = models.TextField(db_column='PastaDocumentos', blank=True, null=True)  # Field name made lowercase.
    resprg = models.TextField(db_column='RespRG', blank=True, null=True)  # Field name made lowercase.
    historico = models.TextField(db_column='Historico', blank=True, null=True)  # Field name made lowercase.
    altprot = models.TextField(db_column='AltProt', blank=True, null=True)  # Field name made lowercase.
    capitals = models.TextField(db_column='CapitalS', blank=True, null=True)  # Field name made lowercase.
    capitali = models.TextField(db_column='CapitalI', blank=True, null=True)  # Field name made lowercase.
    dataexcsocial = models.DateTimeField(db_column='DataExcSocial', blank=True, null=True)  # Field name made lowercase.
    cnhnumero = models.TextField(db_column='CNHnumero', blank=True, null=True)  # Field name made lowercase.
    cnhexp = models.TextField(db_column='CNHexp', blank=True, null=True)  # Field name made lowercase.
    cnhdataexp = models.DateTimeField(db_column='CNHdataexp', blank=True, null=True)  # Field name made lowercase.
    respmae = models.TextField(db_column='RespMae', blank=True, null=True)  # Field name made lowercase.
    respdatanasc = models.DateTimeField(db_column='RespDataNasc', blank=True, null=True)  # Field name made lowercase.
    cadimob = models.TextField(db_column='CadImob', blank=True, null=True)  # Field name made lowercase.
    endzona = models.TextField(db_column='EndZona', blank=True, null=True)  # Field name made lowercase.
    endquadra = models.TextField(db_column='EndQuadra', blank=True, null=True)  # Field name made lowercase.
    enddata = models.DateTimeField(db_column='EndData', blank=True, null=True)  # Field name made lowercase.
    resprgsigla = models.TextField(db_column='RespRgSigla', blank=True, null=True)  # Field name made lowercase.
    procuracao = models.TextField(db_column='Procuracao', blank=True, null=True)  # Field name made lowercase.
    procuracaon = models.TextField(db_column='ProcuracaoN', blank=True, null=True)  # Field name made lowercase.
    procuracaodata = models.DateTimeField(db_column='ProcuracaoData', blank=True, null=True)  # Field name made lowercase.
    novarazaosocial1 = models.TextField(db_column='NovaRazaoSocial1', blank=True, null=True)  # Field name made lowercase.
    novarazaosocial2 = models.TextField(db_column='NovaRazaoSocial2', blank=True, null=True)  # Field name made lowercase.
    novarazaosocial3 = models.TextField(db_column='NovaRazaoSocial3', blank=True, null=True)  # Field name made lowercase.
    novarazaosocial = models.TextField(db_column='NovaRazaoSocial', blank=True, null=True)  # Field name made lowercase.
    eventos = models.TextField(db_column='Eventos', blank=True, null=True)  # Field name made lowercase.
    senhagov = models.TextField(db_column='SenhaGov', blank=True, null=True)  # Field name made lowercase.
    resppai = models.TextField(db_column='RespPai', blank=True, null=True)  # Field name made lowercase.
    nireregistro = models.TextField(db_column='NIRERegistro', blank=True, null=True)  # Field name made lowercase.
    nireregistrodata = models.DateTimeField(db_column='NIRERegistroData', blank=True, null=True)  # Field name made lowercase.
    novarazaosocialfinal = models.TextField(db_column='NovaRazaoSocialFinal', blank=True, null=True)  # Field name made lowercase.
    ieonline = models.TextField(db_column='IEOnline', blank=True, null=True)  # Field name made lowercase.
    ietipo = models.TextField(db_column='IETipo', blank=True, null=True)  # Field name made lowercase.
    ieeprocnum = models.TextField(db_column='IEeProcNum', blank=True, null=True)  # Field name made lowercase.
    iedataaltsolicitado = models.DateTimeField(db_column='IEDataAltSolicitado', blank=True, null=True)  # Field name made lowercase.
    sistemaexterno = models.TextField(db_column='SistemaExterno', blank=True, null=True)  # Field name made lowercase.
    niredata = models.DateTimeField(db_column='NireData', blank=True, null=True)  # Field name made lowercase.
    dadossocios = models.TextField(db_column='DadosSocios', blank=True, null=True)  # Field name made lowercase.
    quantidadesocios = models.TextField(db_column='QuantidadeSocios', blank=True, null=True)  # Field name made lowercase.
    doccontratos = models.BinaryField(db_column='DocContratos', blank=True, null=True)  # Field name made lowercase.
    razaosocialantiga = models.TextField(db_column='RazaoSocialAntiga', blank=True, null=True)  # Field name made lowercase.
    situacaocadastral = models.TextField(db_column='SituacaoCadastral', blank=True, null=True)  # Field name made lowercase.
    divisaocapitalsocios = models.TextField(db_column='DivisaoCapitalSocios', blank=True, null=True)  # Field name made lowercase.
    capitalquotavalor = models.TextField(db_column='CapitalQuotaValor', blank=True, null=True)  # Field name made lowercase.
    capitaquotatotal = models.TextField(db_column='CapitaQuotaTotal', blank=True, null=True)  # Field name made lowercase.
    cpfdoconjuge = models.TextField(db_column='CPFdoCONJUGE', blank=True, null=True)  # Field name made lowercase.
    nomedoconjuge = models.TextField(db_column='NOMEdoCONJUGE', blank=True, null=True)  # Field name made lowercase.
    responsavelorgaorg = models.TextField(db_column='ResponsavelOrgaoRG', blank=True, null=True)  # Field name made lowercase.
    responsavelestadoorgaorg = models.TextField(db_column='ResponsavelEstadoOrgaoRG', blank=True, null=True)  # Field name made lowercase.
    numeroprocesso = models.TextField(db_column='NumeroProcesso', blank=True, null=True)  # Field name made lowercase.
    reciboprocesso = models.TextField(db_column='ReciboProcesso', blank=True, null=True)  # Field name made lowercase.
    sede = models.TextField(db_column='SEDE', blank=True, null=True)  # Field name made lowercase.
    pontodereferencia = models.TextField(db_column='PontoDeReferencia', blank=True, null=True)  # Field name made lowercase.
    tipounidadeprodutiva = models.TextField(db_column='TipoUnidadeProdutiva', blank=True, null=True)  # Field name made lowercase.
    formadeatuacao = models.TextField(db_column='FormaDeAtuacao', blank=True, null=True)  # Field name made lowercase.
    dadoscomplestabelecimento = models.TextField(db_column='DadosComplEstabelecimento', blank=True, null=True)  # Field name made lowercase.
    dadoscomplatividade = models.TextField(db_column='DadosComplAtividade', blank=True, null=True)  # Field name made lowercase.
    dadoscomplpavimentos = models.TextField(db_column='DadosComplPavimentos', blank=True, null=True)  # Field name made lowercase.
    dadoscomplpessoas = models.TextField(db_column='DadosComplPessoas', blank=True, null=True)  # Field name made lowercase.
    dadoscomplsubsolo = models.TextField(db_column='DadosComplSubsolo', blank=True, null=True)  # Field name made lowercase.
    dadoscomplliquido = models.TextField(db_column='DadosComplLiquido', blank=True, null=True)  # Field name made lowercase.
    dadoscomplglp = models.TextField(db_column='DadosComplGLP', blank=True, null=True)  # Field name made lowercase.
    ajudatipodeunidade = models.TextField(db_column='AjudaTipodeUnidade', blank=True, null=True)  # Field name made lowercase.
    dbeprotocolo = models.TextField(db_column='DBEProtocolo', blank=True, null=True)  # Field name made lowercase.
    dbedata = models.DateTimeField(db_column='DBEData', blank=True, null=True)  # Field name made lowercase.
    federalprotocolo = models.TextField(db_column='FederalProtocolo', blank=True, null=True)  # Field name made lowercase.
    senhasdeacesso = models.TextField(db_column='SenhasDeAcesso', blank=True, null=True)  # Field name made lowercase.
    capitalsocialantigo = models.TextField(db_column='CapitalSocialAntigo', blank=True, null=True)  # Field name made lowercase.
    capitalantigomudou = models.TextField(db_column='CapitalAntigoMudou', blank=True, null=True)  # Field name made lowercase.
    cnaeatividadenolocal = models.TextField(db_column='CNAEAtividadeNoLocal', blank=True, null=True)  # Field name made lowercase.
    cnaeatvlocalprincipal = models.TextField(db_column='CNAEAtvLocalPrincipal', blank=True, null=True)  # Field name made lowercase.
    cnaeatvlocalsecundarios = models.TextField(db_column='CNAEAtvLocalSEcundarios', blank=True, null=True)  # Field name made lowercase.
    bombeiroatvadm = models.TextField(db_column='BombeiroAtvAdm', blank=True, null=True)  # Field name made lowercase.
    bombeiroatvresidencia = models.TextField(db_column='BombeiroAtvresidencia', blank=True, null=True)  # Field name made lowercase.
    cnaedescricaooficial = models.TextField(db_column='CNAEdescricaoOficial', blank=True, null=True)  # Field name made lowercase.
    objetodoestabelecimento = models.TextField(db_column='ObjetoDOEstabelecimento', blank=True, null=True)  # Field name made lowercase.
    simplesecac = models.TextField(db_column='SimplesEcac', blank=True, null=True)  # Field name made lowercase.
    avisarempresa = models.BooleanField(db_column='AvisarEmpresa', blank=True, null=True)  # Field name made lowercase.
    avisarempresatexto = models.TextField(db_column='AvisarEmpresaTexto', blank=True, null=True)  # Field name made lowercase.
    temenderecoantigoemp = models.TextField(db_column='TemEnderecoAntigoEmp', blank=True, null=True)  # Field name made lowercase.
    enderecoantigoemp = models.TextField(db_column='EnderecoAntigoEmp', blank=True, null=True)  # Field name made lowercase.
    codsistemaexterno = models.TextField(db_column='CodSistemaExterno', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empresas'


class Eventosempresa(models.Model):
    id_eventosempresa = models.AutoField(db_column='ID_EventosEmpresa', primary_key=True)  # Field name made lowercase.
    eventos = models.TextField(db_column='Eventos', blank=True, null=True)  # Field name made lowercase.
    empresafacil = models.TextField(db_column='EmpresaFacil', blank=True, null=True)  # Field name made lowercase.
    receitafederal = models.TextField(db_column='ReceitaFederal', blank=True, null=True)  # Field name made lowercase.
    receitaestadual = models.TextField(db_column='ReceitaEstadual', blank=True, null=True)  # Field name made lowercase.
    prefeituramunicipal = models.TextField(db_column='PrefeituraMunicipal', blank=True, null=True)  # Field name made lowercase.
    eventosdescriþÒotitulo = models.TextField(db_column='EventosDescriþÒoTitulo', blank=True, null=True)  # Field name made lowercase.
    eventosdescriþÒo = models.TextField(db_column='EventosDescriþÒo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventosEmpresa'


class Laudos(models.Model):
    id_laudos = models.SmallAutoField(db_column='ID_Laudos', primary_key=True)  # Field name made lowercase.
    razaosocial = models.TextField(db_column='RazaoSocial', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    endnum = models.CharField(db_column='EndNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endcomp = models.CharField(db_column='EndComp', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    enddata = models.CharField(db_column='EndData', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endquadra = models.CharField(db_column='EndQuadra', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endzona = models.CharField(db_column='EndZona', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endcep = models.CharField(db_column='EndCEP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cnae = models.TextField(db_column='CNAE', blank=True, null=True)  # Field name made lowercase.
    naturezadopedido = models.TextField(db_column='NaturezaDoPedido', blank=True, null=True)  # Field name made lowercase.
    naturezadopedidoobs = models.TextField(db_column='NaturezaDoPedidoOBS', blank=True, null=True)  # Field name made lowercase.
    requerente = models.TextField(db_column='Requerente', blank=True, null=True)  # Field name made lowercase.
    cpfrequerente = models.CharField(db_column='CPFRequerente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endrequerente = models.TextField(db_column='EndRequerente', blank=True, null=True)  # Field name made lowercase.
    fonerequerente = models.CharField(db_column='FoneRequerente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailrequerente = models.TextField(db_column='EmailRequerente', blank=True, null=True)  # Field name made lowercase.
    cnpjrequerente = models.CharField(db_column='CNPJRequerente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rgrequerente = models.CharField(db_column='RGRequerente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ramodeatividade = models.TextField(db_column='Ramodeatividade', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(max_length=50, blank=True, null=True)
    resptecnico = models.TextField(db_column='Resptecnico', blank=True, null=True)  # Field name made lowercase.
    resptecniconumero = models.CharField(db_column='ResptecnicoNumero', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lembrete = models.CharField(db_column='Lembrete', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endbairro = models.CharField(db_column='EndBairro', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    endcidade = models.CharField(db_column='EndCidade', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    endestado = models.CharField(db_column='EndEstado', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    bombeiros = models.CharField(db_column='Bombeiros', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bombeirossituacao = models.CharField(db_column='BombeirosSituacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bombeirosvenc = models.CharField(db_column='BombeirosVenc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ambiental = models.CharField(db_column='Ambiental', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ambientalsituacao = models.CharField(db_column='AmbientalSituacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ambientalvenc = models.CharField(db_column='AmbientalVenc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    viabilidade = models.CharField(db_column='Viabilidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    viabilidadesituacao = models.CharField(db_column='ViabilidadeSituacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    viabilidadevec = models.CharField(db_column='ViabilidadeVec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanitario = models.CharField(db_column='Sanitario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanitariosituacao = models.CharField(db_column='SanitarioSituacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanitariovenc = models.CharField(db_column='SanitarioVenc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    setran = models.CharField(db_column='Setran', max_length=50, blank=True, null=True)  # Field name made lowercase.
    setransituacao = models.CharField(db_column='SetranSituacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    setranvenc = models.CharField(db_column='SetranVenc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bombeiroexigencia = models.TextField(db_column='BombeiroExigencia', blank=True, null=True)  # Field name made lowercase.
    ambientalexigencia = models.TextField(db_column='AmbientalExigencia', blank=True, null=True)  # Field name made lowercase.
    viabilidadeexigencia = models.TextField(db_column='ViabilidadeExigencia', blank=True, null=True)  # Field name made lowercase.
    sanitarioexigencia = models.TextField(db_column='SanitarioExigencia', blank=True, null=True)  # Field name made lowercase.
    setranexigencia = models.TextField(db_column='SetranExigencia', blank=True, null=True)  # Field name made lowercase.
    bombeirodataprovisorio = models.CharField(db_column='BombeiroDataProvisorio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ambientaldataprovisorio = models.CharField(db_column='AmbientalDataProvisorio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    viabilidadedataprovisorio = models.CharField(db_column='ViabilidadeDataProvisorio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanitariodataprovisorio = models.CharField(db_column='SanitarioDataProvisorio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    setrandataprovisorio = models.CharField(db_column='SetranDataProvisorio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bombeironprocesso = models.CharField(db_column='BombeiroNProcesso', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bombeirodatapedprocesso = models.CharField(db_column='BombeiroDataPedProcesso', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nlaudo = models.CharField(db_column='Nlaudo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datacriado = models.CharField(db_column='DataCriado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dataentrada = models.CharField(db_column='DataEntrada', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pendencia = models.CharField(db_column='Pendencia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modelosistema = models.CharField(db_column='ModeloSistema', max_length=50, blank=True, null=True)  # Field name made lowercase.
    avisardia = models.CharField(db_column='AvisarDia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cadimob = models.CharField(db_column='CadImob', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cmc = models.CharField(db_column='CMC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area2 = models.TextField(blank=True, null=True)
    pontoref = models.CharField(db_column='PontoRef', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    sanitariocontrole1 = models.CharField(db_column='Sanitariocontrole1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanitariocontrole2 = models.CharField(db_column='Sanitariocontrole2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanitariocontrole3 = models.CharField(db_column='Sanitariocontrole3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.
    protocolotipo = models.TextField(db_column='ProtocoloTipo', blank=True, null=True)  # Field name made lowercase.
    protocolon = models.TextField(db_column='ProtocoloN', blank=True, null=True)  # Field name made lowercase.
    protocoloano = models.TextField(db_column='ProtocoloAno', blank=True, null=True)  # Field name made lowercase.
    protocolosenha = models.TextField(db_column='ProtocoloSenha', blank=True, null=True)  # Field name made lowercase.
    historico = models.TextField(db_column='Historico', blank=True, null=True)  # Field name made lowercase.
    bombeirosituacao = models.TextField(db_column='BombeiroSituacao', blank=True, null=True)  # Field name made lowercase.
    bombeiroprovisoriodata = models.DateTimeField(db_column='BombeiroProvisorioDATA', blank=True, null=True)  # Field name made lowercase.
    ambientalprovisoriodata = models.DateTimeField(db_column='AmbientalProvisorioDATA', blank=True, null=True)  # Field name made lowercase.
    viabilidadeprovisoriodata = models.DateTimeField(db_column='ViabilidadeProvisorioDATA', blank=True, null=True)  # Field name made lowercase.
    sanitarioprovisoriodata = models.DateTimeField(db_column='SanitarioProvisorioDATA', blank=True, null=True)  # Field name made lowercase.
    setranprovisoriodata = models.DateTimeField(db_column='SetranProvisorioDATA', blank=True, null=True)  # Field name made lowercase.
    orgaorgrequerente = models.TextField(db_column='OrgaoRGRequerente', blank=True, null=True)  # Field name made lowercase.
    estadoorgaorgrequerente = models.TextField(db_column='EstadoOrgaoRGRequerente', blank=True, null=True)  # Field name made lowercase.
    numeroprocesso = models.TextField(db_column='NumeroProcesso', blank=True, null=True)  # Field name made lowercase.
    reciboprocesso = models.TextField(db_column='ReciboProcesso', blank=True, null=True)  # Field name made lowercase.
    prioridade = models.TextField(db_column='Prioridade', blank=True, null=True)  # Field name made lowercase.
    matriz = models.TextField(db_column='Matriz', blank=True, null=True)  # Field name made lowercase.
    bombeirodatamulta = models.TextField(db_column='BombeiroDataMulta', blank=True, null=True)  # Field name made lowercase.
    nlaudosecundario = models.CharField(db_column='NlaudoSecundario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cnaeprimario = models.TextField(db_column='CNAEPrimario', blank=True, null=True)  # Field name made lowercase.
    alvara = models.TextField(db_column='Alvara', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Laudos'


class Login(models.Model):
    id_login = models.SmallIntegerField()
    usuario = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    nomecompleto = models.CharField(max_length=500, blank=True, null=True)
    tema = models.CharField(max_length=200, blank=True, null=True)
    datanascimento = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Login'


class Municipio(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    uf = models.CharField(db_column='Uf', max_length=2)  # Field name made lowercase.
    procedimento = models.TextField(db_column='Procedimento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Municipio'


class Naturezajuridica(models.Model):
    id_naturezajuridica = models.SmallAutoField(db_column='ID_Naturezajuridica', primary_key=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Naturezajuridica'


class Parcelamentos(models.Model):
    razaosocial = models.TextField(db_column='RazaoSocial', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.TextField(db_column='CNPJ', blank=True, null=True)  # Field name made lowercase.
    formadeenvio = models.TextField(db_column='FormaDeEnvio', blank=True, null=True)  # Field name made lowercase.
    responsavel = models.TextField(db_column='Responsavel', blank=True, null=True)  # Field name made lowercase.
    whatsapp = models.TextField(db_column='Whatsapp', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    socio = models.TextField(db_column='Socio', blank=True, null=True)  # Field name made lowercase.
    cpf = models.TextField(db_column='CPF', blank=True, null=True)  # Field name made lowercase.
    senhagov = models.TextField(db_column='SenhaGov', blank=True, null=True)  # Field name made lowercase.
    datacriacao = models.TextField(db_column='DataCriacao', blank=True, null=True)  # Field name made lowercase.
    datalembrete = models.TextField(db_column='DataLembrete', blank=True, null=True)  # Field name made lowercase.
    datafinalizado = models.TextField(db_column='DataFinalizado', blank=True, null=True)  # Field name made lowercase.
    mei = models.TextField(db_column='MEI', blank=True, null=True)  # Field name made lowercase.
    inssantigo = models.TextField(db_column='InssAntigo', blank=True, null=True)  # Field name made lowercase.
    inssnovo = models.TextField(db_column='InssNovo', blank=True, null=True)  # Field name made lowercase.
    inssprocur = models.TextField(db_column='InssProcur', blank=True, null=True)  # Field name made lowercase.
    datasolicmei = models.TextField(db_column='DataSolicMEI', blank=True, null=True)  # Field name made lowercase.
    dataenviamei = models.TextField(db_column='DataEnviaMEI', blank=True, null=True)  # Field name made lowercase.
    datafinalmei = models.TextField(db_column='DataFinalMEI', blank=True, null=True)  # Field name made lowercase.
    motivomei = models.TextField(db_column='MotivoMEI', blank=True, null=True)  # Field name made lowercase.
    protmei = models.TextField(db_column='ProtMEI', blank=True, null=True)  # Field name made lowercase.
    totalparcmei = models.TextField(db_column='TotalParcMEI', blank=True, null=True)  # Field name made lowercase.
    enviaparcmei = models.TextField(db_column='EnviaParcMEI', blank=True, null=True)  # Field name made lowercase.
    datasolicantigo = models.TextField(db_column='DataSolicAntigo', blank=True, null=True)  # Field name made lowercase.
    dataenviaantigo = models.TextField(db_column='DataEnviaAntigo', blank=True, null=True)  # Field name made lowercase.
    datafinalantigo = models.TextField(db_column='DataFinalAntigo', blank=True, null=True)  # Field name made lowercase.
    motivoantigo = models.TextField(db_column='MotivoAntigo', blank=True, null=True)  # Field name made lowercase.
    protantigo = models.TextField(db_column='ProtAntigo', blank=True, null=True)  # Field name made lowercase.
    totalparcantigo = models.TextField(db_column='TotalParcAntigo', blank=True, null=True)  # Field name made lowercase.
    enviaparcantigo = models.TextField(db_column='EnviaParcAntigo', blank=True, null=True)  # Field name made lowercase.
    datasolicnovo = models.TextField(db_column='DataSolicNovo', blank=True, null=True)  # Field name made lowercase.
    dataenvionovo = models.TextField(db_column='DataEnvioNovo', blank=True, null=True)  # Field name made lowercase.
    datafinalnovo = models.TextField(db_column='DataFinalNovo', blank=True, null=True)  # Field name made lowercase.
    motivonovo = models.TextField(db_column='MotivoNovo', blank=True, null=True)  # Field name made lowercase.
    protnovo = models.TextField(db_column='ProtNovo', blank=True, null=True)  # Field name made lowercase.
    totalparcnovo = models.TextField(db_column='TotalParcNovo', blank=True, null=True)  # Field name made lowercase.
    enviaparcnovo = models.TextField(db_column='EnviaParcNovo', blank=True, null=True)  # Field name made lowercase.
    datasolicproc = models.TextField(db_column='DataSolicProc', blank=True, null=True)  # Field name made lowercase.
    dataenviaproc = models.TextField(db_column='DataEnviaProc', blank=True, null=True)  # Field name made lowercase.
    datafinalproc = models.TextField(db_column='DataFinalProc', blank=True, null=True)  # Field name made lowercase.
    motivoproc = models.TextField(db_column='MotivoProc', blank=True, null=True)  # Field name made lowercase.
    protproc = models.TextField(db_column='Protproc', blank=True, null=True)  # Field name made lowercase.
    totalparcproc = models.TextField(db_column='TotalParcProc', blank=True, null=True)  # Field name made lowercase.
    enviaparcproc = models.TextField(db_column='EnviaParcProc', blank=True, null=True)  # Field name made lowercase.
    id_parcel = models.AutoField(db_column='ID_Parcel', primary_key=True)  # Field name made lowercase.
    parcelenvmei = models.TextField(db_column='ParcelEnvMEI', blank=True, null=True)  # Field name made lowercase.
    parcelenvinssant = models.TextField(db_column='ParcelEnvINSSAnt', blank=True, null=True)  # Field name made lowercase.
    parcelenvinssnov = models.TextField(db_column='ParcelEnvINSSNov', blank=True, null=True)  # Field name made lowercase.
    parcelenvinssproc = models.TextField(db_column='ParcelEnvINSSProc', blank=True, null=True)  # Field name made lowercase.
    finalizadoempresa = models.TextField(db_column='FinalizadoEmpresa', blank=True, null=True)  # Field name made lowercase.
    finalizadomei = models.TextField(db_column='FinalizadoMEI', blank=True, null=True)  # Field name made lowercase.
    finalizadoinssant = models.TextField(db_column='FinalizadoINSSAnt', blank=True, null=True)  # Field name made lowercase.
    finalizadoinssnov = models.TextField(db_column='FinalizadoINSSNov', blank=True, null=True)  # Field name made lowercase.
    finalizadoinssproc = models.TextField(db_column='FinalizadoINSSProc', blank=True, null=True)  # Field name made lowercase.
    finalizadomesgeral = models.TextField(db_column='FinalizadoMesGeral', blank=True, null=True)  # Field name made lowercase.
    geral = models.TextField(db_column='Geral', blank=True, null=True)  # Field name made lowercase.
    parafazer = models.TextField(db_column='ParaFazer', blank=True, null=True)  # Field name made lowercase.
    atrasoparcelamei = models.TextField(db_column='AtrasoParcelaMEI', blank=True, null=True)  # Field name made lowercase.
    atrasoparcelainssantigo = models.TextField(db_column='AtrasoParcelaINSSAntigo', blank=True, null=True)  # Field name made lowercase.
    atrasoparcelainssnovo = models.TextField(db_column='AtrasoParcelaINSSNovo', blank=True, null=True)  # Field name made lowercase.
    atrasoparcelainssprocu = models.TextField(db_column='AtrasoParcelaINSSProcu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parcelamentos'


class Parcelamentosaviso(models.Model):
    idparcelamentoaviso = models.AutoField(db_column='IDParcelamentoAviso', primary_key=True)  # Field name made lowercase.
    mesrealizado = models.CharField(db_column='MesRealizado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(db_column='Ano', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ParcelamentosAviso'


class Registroprofissional(models.Model):
    id_registroprofissional = models.SmallAutoField(db_column='ID_RegistroProfissional', primary_key=True)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=10)  # Field name made lowercase.
    extenso = models.CharField(db_column='Extenso', max_length=255)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegistroProfissional'


class Sites(models.Model):
    id_sites = models.AutoField(db_column='ID_Sites', primary_key=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    cidade = models.TextField(db_column='Cidade', blank=True, null=True)  # Field name made lowercase.
    siteestado = models.TextField(db_column='SiteEstado', blank=True, null=True)  # Field name made lowercase.
    sitecidade = models.TextField(db_column='SiteCidade', blank=True, null=True)  # Field name made lowercase.
    sitejuntaunificada = models.TextField(db_column='SiteJuntaUnificada', blank=True, null=True)  # Field name made lowercase.
    sitejuntaantiga = models.TextField(db_column='SiteJuntaAntiga', blank=True, null=True)  # Field name made lowercase.
    sitealvara1 = models.TextField(db_column='SiteAlvara1', blank=True, null=True)  # Field name made lowercase.
    sitealvara2 = models.TextField(db_column='SiteAlvara2', blank=True, null=True)  # Field name made lowercase.
    distrito = models.TextField(db_column='Distrito', blank=True, null=True)  # Field name made lowercase.
    estadosigla = models.TextField(db_column='EstadoSigla', blank=True, null=True)  # Field name made lowercase.
    sitealvarapedido1 = models.TextField(db_column='SiteAlvaraPedido1', blank=True, null=True)  # Field name made lowercase.
    sitealvarapedido2 = models.TextField(db_column='SiteAlvaraPedido2', blank=True, null=True)  # Field name made lowercase.
    siteprefprotocolo = models.TextField(db_column='SitePrefProtocolo', blank=True, null=True)  # Field name made lowercase.
    observacoes = models.TextField(db_column='Observacoes', blank=True, null=True)  # Field name made lowercase.
    siteredesimprotocolo = models.TextField(db_column='SiteREDESIMProtocolo', blank=True, null=True)  # Field name made lowercase.
    siteredesimconsultacnpj = models.TextField(db_column='SiteREDESIMConsultaCNPJ', blank=True, null=True)  # Field name made lowercase.
    siteredesimabrircnpj = models.TextField(db_column='SiteREDESIMAbrirCNPJ', blank=True, null=True)  # Field name made lowercase.
    siteredesimmeucnpj = models.TextField(db_column='SiteREDESIMMeuCNPJ', blank=True, null=True)  # Field name made lowercase.
    bombeiroconsulta = models.TextField(db_column='BombeiroConsulta', blank=True, null=True)  # Field name made lowercase.
    bombeirosolicita = models.TextField(db_column='BombeiroSolicita', blank=True, null=True)  # Field name made lowercase.
    bombeirounificado = models.TextField(db_column='BombeiroUnificado', blank=True, null=True)  # Field name made lowercase.
    bombeiroredesim = models.TextField(db_column='BombeiroREDESIM', blank=True, null=True)  # Field name made lowercase.
    federalecac = models.TextField(db_column='FederalECAC', blank=True, null=True)  # Field name made lowercase.
    federalparcproc = models.TextField(db_column='FederalParcProc', blank=True, null=True)  # Field name made lowercase.
    federalprocuradoria = models.TextField(db_column='FederalProcuradoria', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sites'


class Socios(models.Model):
    id_socios = models.AutoField(db_column='ID_Socios', primary_key=True)  # Field name made lowercase.
    cpf = models.TextField(db_column='CPF', blank=True, null=True)  # Field name made lowercase.
    nomecompleto = models.TextField(db_column='NomeCompleto', blank=True, null=True)  # Field name made lowercase.
    nomemae = models.TextField(db_column='NomeMae', blank=True, null=True)  # Field name made lowercase.
    nomepai = models.TextField(db_column='NomePai', blank=True, null=True)  # Field name made lowercase.
    datadenasc = models.TextField(db_column='DatadeNasc', blank=True, null=True)  # Field name made lowercase.
    rg = models.TextField(db_column='RG', blank=True, null=True)  # Field name made lowercase.
    orgaorg = models.TextField(db_column='OrgaoRG', blank=True, null=True)  # Field name made lowercase.
    estadorg = models.TextField(db_column='EstadoRG', blank=True, null=True)  # Field name made lowercase.
    titulodeeleitor = models.TextField(db_column='TituloDeEleitor', blank=True, null=True)  # Field name made lowercase.
    senhagov = models.TextField(db_column='SenhaGOV', blank=True, null=True)  # Field name made lowercase.
    cnh = models.TextField(db_column='CNH', blank=True, null=True)  # Field name made lowercase.
    cnhexpedicao = models.TextField(db_column='CNHExpedicao', blank=True, null=True)  # Field name made lowercase.
    cnhdataexp = models.TextField(db_column='CNHDataExp', blank=True, null=True)  # Field name made lowercase.
    civil = models.TextField(db_column='Civil', blank=True, null=True)  # Field name made lowercase.
    cep = models.TextField(db_column='CEP', blank=True, null=True)  # Field name made lowercase.
    rua = models.TextField(db_column='RUA', blank=True, null=True)  # Field name made lowercase.
    num = models.TextField(db_column='Num', blank=True, null=True)  # Field name made lowercase.
    bairro = models.TextField(db_column='Bairro', blank=True, null=True)  # Field name made lowercase.
    complemento = models.TextField(db_column='Complemento', blank=True, null=True)  # Field name made lowercase.
    cidade = models.TextField(db_column='Cidade', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    paÝs = models.TextField(db_column='PaÝs', blank=True, null=True)  # Field name made lowercase.
    telefone1 = models.TextField(db_column='Telefone1', blank=True, null=True)  # Field name made lowercase.
    telefone2 = models.TextField(db_column='Telefone2', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='eMail', blank=True, null=True)  # Field name made lowercase.
    genero = models.TextField(db_column='Genero', blank=True, null=True)  # Field name made lowercase.
    cpfdoconjuge = models.TextField(db_column='CPFdoCONJUGE', blank=True, null=True)  # Field name made lowercase.
    nomedoconjuge = models.TextField(db_column='NOMEdoCONJUGE', blank=True, null=True)  # Field name made lowercase.
    profissÒo = models.TextField(db_column='ProfissÒo', blank=True, null=True)  # Field name made lowercase.
    outrosdados = models.TextField(db_column='OutrosDados', blank=True, null=True)  # Field name made lowercase.
    menoridade = models.TextField(db_column='MenorIdade', blank=True, null=True)  # Field name made lowercase.
    registroorgao = models.TextField(db_column='RegistroOrgao', blank=True, null=True)  # Field name made lowercase.
    registroestado = models.TextField(db_column='RegistroEstado', blank=True, null=True)  # Field name made lowercase.
    registronumero = models.TextField(db_column='RegistroNumero', blank=True, null=True)  # Field name made lowercase.
    registrodata = models.TextField(db_column='RegistroData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Socios'


class Telefones(models.Model):
    id_telefones = models.SmallAutoField(db_column='ID_Telefones', primary_key=True)  # Field name made lowercase.
    nome = models.TextField(db_column='Nome', blank=True, null=True)  # Field name made lowercase.
    telefone1 = models.CharField(db_column='Telefone1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefoneoutros = models.CharField(db_column='TelefoneOutros', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endereþo = models.TextField(db_column='Endereþo', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=50, blank=True, null=True)  # Field name made lowercase.
    complemento = models.TextField(db_column='Complemento', blank=True, null=True)  # Field name made lowercase.
    bairro = models.TextField(db_column='Bairro', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    orgaoestado = models.TextField(db_column='OrgaoEstado', blank=True, null=True)  # Field name made lowercase.
    orgaocidade = models.TextField(db_column='OrgaoCidade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Telefones'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Email(models.Model):
    id_email = models.AutoField(db_column='ID_eMail', primary_key=True)  # Field name made lowercase.
    email = models.TextField(db_column='eMail', blank=True, null=True)  # Field name made lowercase.
    senhaemail = models.TextField(db_column='SenhaEmail', blank=True, null=True)  # Field name made lowercase.
    smtpclient = models.TextField(db_column='SmtpClient', blank=True, null=True)  # Field name made lowercase.
    smtpport = models.TextField(db_column='SmtpPort', blank=True, null=True)  # Field name made lowercase.
    clientssl = models.TextField(db_column='clientSsl', blank=True, null=True)  # Field name made lowercase.
    caixadesaida = models.TextField(db_column='CaixaDeSaida', blank=True, null=True)  # Field name made lowercase.
    parageral = models.TextField(db_column='ParaGeral', blank=True, null=True)  # Field name made lowercase.
    habilitassl = models.TextField(db_column='HabilitaSsl', blank=True, null=True)  # Field name made lowercase.
    credencial = models.TextField(db_column='Credencial', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eMail'


class Emailcaixadesaida(models.Model):
    id_emailcaixadesaida = models.AutoField(db_column='ID_eMailCaixaDeSaida', primary_key=True)  # Field name made lowercase.
    idemailprincipal = models.TextField(db_column='IDeMailPrincipal', blank=True, null=True)  # Field name made lowercase.
    emailprincipal = models.TextField(db_column='eMailPrincipal', blank=True, null=True)  # Field name made lowercase.
    emaildestino = models.TextField(db_column='eMailDestino', blank=True, null=True)  # Field name made lowercase.
    assunto = models.TextField(db_column='Assunto', blank=True, null=True)  # Field name made lowercase.
    caixadesaidatexto = models.TextField(db_column='CaixaDeSaidaTexto', blank=True, null=True)  # Field name made lowercase.
    dataenviado = models.DateTimeField(db_column='DataEnviado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eMailCaixaDeSaida'


class TesteTb(models.Model):
    cod = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teste_tb'
