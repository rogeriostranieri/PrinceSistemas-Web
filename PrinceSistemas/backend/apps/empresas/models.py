from django.db import models

class Empresa(models.Model):
    id_empresas = models.AutoField(primary_key=True, db_column='ID_Empresas')
    razaosocial = models.CharField(max_length=255, db_column='RazaoSocial')
    nomefantasia = models.CharField(max_length=255, blank=True, null=True, db_column='NomeFantasia')
    cnpj = models.CharField(max_length=50, blank=True, null=True, db_column='CNPJ')
    endereco = models.CharField(max_length=255, blank=True, null=True, db_column='Endereco')
    endnumero = models.CharField(max_length=50, blank=True, null=True, db_column='EndNumero')
    endbairro = models.CharField(max_length=255, blank=True, null=True, db_column='EndBairro')
    endcomplemento = models.CharField(max_length=255, blank=True, null=True, db_column='EndComplemento')
    endcep = models.CharField(max_length=20, blank=True, null=True, db_column='EndCEP')
    endcidade = models.CharField(max_length=255, blank=True, null=True, db_column='EndCidade')
    endestado = models.CharField(max_length=255, blank=True, null=True, db_column='EndEstado')
    endpais = models.CharField(max_length=255, blank=True, null=True, db_column='EndPais')
    emptel1 = models.CharField(max_length=50, blank=True, null=True, db_column='EmpTel1')
    emptel2 = models.CharField(max_length=50, blank=True, null=True, db_column='EmpTel2')
    empemail = models.EmailField(blank=True, null=True, db_column='EmpEmail')
    paginaweb = models.URLField(blank=True, null=True, db_column='PaginaWeb')
    ie = models.CharField(max_length=50, blank=True, null=True, db_column='IE')
    im = models.CharField(max_length=50, blank=True, null=True, db_column='IM')
    naturezajuridica = models.CharField(max_length=255, blank=True, null=True, db_column='NaturezaJuridica')
    
   
    # Campos de data ajustados para DateTimeField
    empinicioatividade = models.DateTimeField(blank=True, null=True, db_column='EmpInicioAtividade')
    empcriado = models.DateTimeField(blank=True, null=True, db_column='EmpCriado')
    dataprotredesim = models.DateTimeField(blank=True, null=True, db_column='DataProtREDESIM')
    dataprotjuntacomercial = models.DateTimeField(blank=True, null=True, db_column='DataProtJuntaComercial')
    datapedidoie = models.DateTimeField(blank=True, null=True, db_column='DataPedidoIE')
    dataregistroalt = models.DateTimeField(blank=True, null=True, db_column='DataRegistroAlt')
    datamotivo = models.DateTimeField(blank=True, null=True, db_column='DataMotivo')
    ieinicioatividade = models.DateTimeField(blank=True, null=True, db_column='IEInicioAtividade')
    ievencpedido = models.DateTimeField(blank=True, null=True, db_column='IEVencPedido')
    datasimples = models.DateTimeField(blank=True, null=True, db_column='DataSimples')
    dataultdefsimples = models.DateTimeField(blank=True, null=True, db_column='DataUltdefSimples')
    dataexcsocial = models.DateTimeField(blank=True, null=True, db_column='DataExcSocial')
    cnhdataexp = models.DateTimeField(blank=True, null=True, db_column='CNHdataexp')
    respdatanasc = models.DateTimeField(blank=True, null=True, db_column='RespDataNasc')
    enddata = models.CharField(max_length=50, blank=True, null=True, db_column='EndData')
    procuracaodata = models.DateTimeField(blank=True, null=True, db_column='ProcuracaoData')
    nireregistrodata = models.DateTimeField(blank=True, null=True, db_column='NIRERegistroData')
    iedataaltsolicitado = models.DateTimeField(blank=True, null=True, db_column='IEDataAltSolicitado')
    niredata = models.DateTimeField(blank=True, null=True, db_column='NireData')
    dbedata = models.DateTimeField(blank=True, null=True, db_column='DBEData')
    protjuntafinal = models.DateTimeField(blank=True, null=True, db_column='ProtJuntaFinal')
    prazosimples = models.DateTimeField(blank=True, null=True, db_column='PrazoSimples')
    avisardia = models.DateTimeField(blank=True, null=True, db_column='AvisarDia')
    

    # Outros campos mantidos como CharField ou TextField
    processo = models.CharField(max_length=255, blank=True, null=True, db_column='Processo')
    status = models.CharField(max_length=50, blank=True, null=True, db_column='Status')
    nire = models.CharField(max_length=50, blank=True, null=True, db_column='NIRE')
    cnaeprincipal = models.TextField(blank=True, null=True, db_column='CNAEPrincipal')
    cnaesecundario = models.TextField(blank=True, null=True, db_column='CNAESecundario')
    ramodeatividade = models.TextField(blank=True, null=True, db_column='RamoDeAtividade')
    responsavelcpf = models.CharField(max_length=50, blank=True, null=True, db_column='ResponsavelCPF')
    responsavelnome = models.CharField(max_length=255, blank=True, null=True, db_column='ResponsavelNome')
    protocolojuntacomercial = models.CharField(max_length=255, blank=True, null=True, db_column='ProtocoloJuntaComercial')
    geral = models.TextField(blank=True, null=True, db_column='Geral')
    protocoloredesim = models.CharField(max_length=255, blank=True, null=True, db_column='ProtocoloREDESIM')
    nirealt = models.CharField(max_length=50, blank=True, null=True, db_column='NireAlt')
    juntaobs = models.TextField(blank=True, null=True, db_column='JuntaObs')
    nregistroalt = models.CharField(max_length=50, blank=True, null=True, db_column='NRegistroAlt')
    nireantigos = models.CharField(max_length=255, blank=True, null=True, db_column='NireAntigos')
    nalteracao = models.CharField(max_length=50, blank=True, null=True, db_column='NAlteracao')
    redesimobs = models.TextField(blank=True, null=True, db_column='RedeSimObs')
    estadualobs = models.TextField(blank=True, null=True, db_column='EstadualObs')
    prefeituraobs = models.TextField(blank=True, null=True, db_column='PrefeituraObs')
    codigosimples = models.CharField(max_length=50, blank=True, null=True, db_column='CodigoSimples')
    cpfresponsavel = models.CharField(max_length=50, blank=True, null=True, db_column='CPFResponsavel')
    nomeresponsavel = models.CharField(max_length=255, blank=True, null=True, db_column='NomeResponsavel')
    arquivocontrato = models.CharField(max_length=255, blank=True, null=True, db_column='ArquivoContrato')
    procedimento = models.TextField(blank=True, null=True, db_column='Procedimento')
    regimefederal = models.CharField(max_length=255, blank=True, null=True, db_column='RegimeFederal')
    portedaempresa = models.CharField(max_length=50, blank=True, null=True, db_column='PorteDaEmpresa')
    tipodeempresa = models.CharField(max_length=50, blank=True, null=True, db_column='TipoDeEmpresa')
    altconsolidada = models.CharField(max_length=50, blank=True, null=True, db_column='AltConsolidada')
    motivo = models.TextField(blank=True, null=True, db_column='Motivo')
    iecomprovante = models.CharField(max_length=255, blank=True, null=True, db_column='IEComprovante')
    bombeirojunta = models.CharField(max_length=50, blank=True, null=True, db_column='BombeiroJunta')
    iejunta = models.CharField(max_length=50, blank=True, null=True, db_column='IEjunta')
    tituloeleitor = models.CharField(max_length=50, blank=True, null=True, db_column='Tituloeleitor')
    area = models.CharField(max_length=50, blank=True, null=True, db_column='area')
    area2 = models.CharField(max_length=50, blank=True, null=True, db_column='area2')
    obssimples = models.TextField(blank=True, null=True, db_column='ObsSimples')
    orgaopedsimples = models.CharField(max_length=255, blank=True, null=True, db_column='OrgãoPedSimples')
    pastadocumentos = models.CharField(max_length=255, blank=True, null=True, db_column='PastaDocumentos')
    resprg = models.CharField(max_length=50, blank=True, null=True, db_column='RespRG')
    historico = models.TextField(blank=True, null=True, db_column='Historico')
    altprot = models.CharField(max_length=255, blank=True, null=True, db_column='AltProt')
    capitals = models.CharField(max_length=50, blank=True, null=True, db_column='CapitalS')
    capitali = models.CharField(max_length=50, blank=True, null=True, db_column='CapitalI')
    cnhnumero = models.CharField(max_length=50, blank=True, null=True, db_column='CNHnumero')
    cnhexp = models.CharField(max_length=50, blank=True, null=True, db_column='CNHexp')
    respmae = models.CharField(max_length=255, blank=True, null=True, db_column='RespMae')
    cadimob = models.CharField(max_length=50, blank=True, null=True, db_column='CadImob')
    endzona = models.CharField(max_length=50, blank=True, null=True, db_column='EndZona')
    endquadra = models.CharField(max_length=50, blank=True, null=True, db_column='EndQuadra')
    resprgsigla = models.CharField(max_length=10, blank=True, null=True, db_column='RespRgSigla')
    procuracao = models.CharField(max_length=50, blank=True, null=True, db_column='Procuracao')
    procuracaon = models.CharField(max_length=50, blank=True, null=True, db_column='ProcuracaoN')
    novarazaosocial1 = models.CharField(max_length=255, blank=True, null=True, db_column='NovaRazaoSocial1')
    novarazaosocial2 = models.CharField(max_length=255, blank=True, null=True, db_column='NovaRazaoSocial2')
    novarazaosocial3 = models.CharField(max_length=255, blank=True, null=True, db_column='NovaRazaoSocial3')
    novarazaosocial = models.CharField(max_length=255, blank=True, null=True, db_column='NovaRazaoSocial')
    eventos = models.TextField(blank=True, null=True, db_column='Eventos')
    senhagov = models.CharField(max_length=255, blank=True, null=True, db_column='SenhaGov')
    resppai = models.CharField(max_length=255, blank=True, null=True, db_column='RespPai')
    nireregistro = models.CharField(max_length=50, blank=True, null=True, db_column='NIRERegistro')
    novarazaosocialfinal = models.CharField(max_length=255, blank=True, null=True, db_column='NovaRazaoSocialFinal')
    ieonline = models.CharField(max_length=50, blank=True, null=True, db_column='IEOnline')
    ietipo = models.CharField(max_length=50, blank=True, null=True, db_column='IETipo')
    ieeprocnum = models.CharField(max_length=255, blank=True, null=True, db_column='IEeProcNum')
    sistemaexterno = models.CharField(max_length=255, blank=True, null=True, db_column='SistemaExterno')
    dadossocios = models.TextField(blank=True, null=True, db_column='DadosSocios')
    quantidadesocios = models.CharField(max_length=10, blank=True, null=True, db_column='QuantidadeSocios')
    razaosocialantiga = models.CharField(max_length=255, blank=True, null=True, db_column='RazaoSocialAntiga')
    situacaocadastral = models.CharField(max_length=50, blank=True, null=True, db_column='SituacaoCadastral')
    divisaocapitalsocios = models.CharField(max_length=255, blank=True, null=True, db_column='DivisaoCapitalSocios')
    capitalquotavalor = models.CharField(max_length=50, blank=True, null=True, db_column='CapitalQuotaValor')
    capitaquotatotal = models.CharField(max_length=50, blank=True, null=True, db_column='CapitaQuotaTotal')
    cpfdoconjuge = models.CharField(max_length=50, blank=True, null=True, db_column='CPFdoCONJUGE')
    nomedoconjuge = models.CharField(max_length=255, blank=True, null=True, db_column='NOMEdoCONJUGE')
    responsavelorgaorg = models.CharField(max_length=255, blank=True, null=True, db_column='ResponsavelOrgaoRG')
    responsavelestadoorgaorg = models.CharField(max_length=255, blank=True, null=True, db_column='ResponsavelEstadoOrgaoRG')
    numeroprocesso = models.CharField(max_length=255, blank=True, null=True, db_column='NumeroProcesso')
    reciboprocesso = models.CharField(max_length=255, blank=True, null=True, db_column='ReciboProcesso')
    sede = models.CharField(max_length=50, blank=True, null=True, db_column='SEDE')
    pontodereferencia = models.CharField(max_length=255, blank=True, null=True, db_column='PontoDeReferencia')
    tipounidadeprodutiva = models.CharField(max_length=255, blank=True, null=True, db_column='TipoUnidadeProdutiva')
    formadeatuacao = models.CharField(max_length=255, blank=True, null=True, db_column='FormaDeAtuacao')
    dadoscomplestabelecimento = models.TextField(blank=True, null=True, db_column='DadosComplEstabelecimento')
    dadoscomplatividade = models.TextField(blank=True, null=True, db_column='DadosComplAtividade')
    dadoscomplpavimentos = models.CharField(max_length=50, blank=True, null=True, db_column='DadosComplPavimentos')
    dadoscomplpessoas = models.CharField(max_length=50, blank=True, null=True, db_column='DadosComplPessoas')
    dadoscomplsubsolo = models.CharField(max_length=50, blank=True, null=True, db_column='DadosComplSubsolo')
    dadoscomplliquido = models.CharField(max_length=50, blank=True, null=True, db_column='DadosComplLiquido')
    dadoscomplglp = models.CharField(max_length=50, blank=True, null=True, db_column='DadosComplGLP')
    ajudatipodeunidade = models.TextField(blank=True, null=True, db_column='AjudaTipodeUnidade')
    dbeprotocolo = models.CharField(max_length=255, blank=True, null=True, db_column='DBEProtocolo')
    federalprotocolo = models.CharField(max_length=255, blank=True, null=True, db_column='FederalProtocolo')
    senhasdeacesso = models.TextField(blank=True, null=True, db_column='SenhasDeAcesso')
    capitalsocialantigo = models.CharField(max_length=50, blank=True, null=True, db_column='CapitalSocialAntigo')
    capitalantigomudou = models.CharField(max_length=50, blank=True, null=True, db_column='CapitalAntigoMudou')
    cnaeatividadenolocal = models.TextField(blank=True, null=True, db_column='CNAEAtividadeNoLocal')
    cnaeatvlocalprincipal = models.TextField(blank=True, null=True, db_column='CNAEAtvLocalPrincipal')
    cnaeatvlocalsecundarios = models.TextField(blank=True, null=True, db_column='CNAEAtvLocalSEcundarios')
    bombeiroatvadm = models.CharField(max_length=50, blank=True, null=True, db_column='BombeiroAtvAdm')
    bombeiroatvresidencia = models.CharField(max_length=50, blank=True, null=True, db_column='BombeiroAtvresidencia')
    cnaedescricaooficial = models.TextField(blank=True, null=True, db_column='CNAEdescricaoOficial')
    objetodoestabelecimento = models.TextField(blank=True, null=True, db_column='ObjetoDOEstabelecimento')
    simplesecac = models.CharField(max_length=50, blank=True, null=True, db_column='SimplesEcac')
    avisarempresatexto = models.TextField(blank=True, null=True, db_column='AvisarEmpresaTexto')
    temenderecoantigoemp = models.CharField(max_length=50, blank=True, null=True, db_column='TemEnderecoAntigoEmp')
    enderecoantigoemp = models.TextField(blank=True, null=True, db_column='EnderecoAntigoEmp')
    codsistemaexterno = models.CharField(max_length=255, blank=True, null=True, db_column='CodSistemaExterno')

#checkbox de avisos
    avisarempresa = models.TextField(blank=True, null=True, db_column='AvisarEmpresa')
    prioridade = models.CharField(max_length=20, db_column='Prioridade', blank=True, null=True)
    lembrete = models.CharField(max_length=20, db_column='Lembrete', blank=True, null=True)

#anexar contrato
    doccontratos = models.BinaryField(blank=True, null=True, db_column='DocContratos')  # Alterado para BinaryField

    def normalizar_bool(self, valor):
        if not valor:
            return False
        valor = str(valor).strip().lower()
        return valor in ['checked', 'sim', 'true', '1', 't']

    def save(self, *args, **kwargs):
        # Carrega do banco o valor antigo, se existir
        if self.pk:
            try:
                antigo = Empresa.objects.get(pk=self.pk)
            except Empresa.DoesNotExist:
                antigo = None
        else:
            antigo = None

        # Lista de campos a normalizar
        for field in ['avisarempresa', 'lembrete', 'prioridade']:
            valor_novo = getattr(self, field)
            valor_antigo = getattr(antigo, field) if antigo else None
            if valor_novo != valor_antigo:
                if isinstance(valor_novo, bool):
                    setattr(self, field, 'Sim' if valor_novo else 'Não')
                elif isinstance(valor_novo, str):
                    v = valor_novo.strip().lower()
                    if v in ['sim', 'true', '1', 'checked', 'on']:
                        setattr(self, field, 'Sim')
                    elif v in ['nao', 'não', 'false', '0', 'unchecked', 'off']:
                        setattr(self, field, 'Não')
                    elif v in [None, '', 'null']:
                        setattr(self, field, None)
                    # Se for texto legado, mantém
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'Empresas'
        managed = True  # Alterado para True para permitir migrações
        ordering = ['razaosocial']

    def __str__(self):
        return self.razaosocial


