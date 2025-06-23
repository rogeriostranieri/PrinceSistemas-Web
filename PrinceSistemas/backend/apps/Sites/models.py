from django.db import models

class Sites(models.Model):
    id_sites = models.AutoField(primary_key=True, db_column='ID_Sites')
    estado = models.CharField(max_length=255, db_column='Estado')
    cidade = models.CharField(max_length=255, db_column='Cidade')
    distrito = models.CharField(max_length=255, null=True, blank=True, db_column='Distrito')
    estado_sigla = models.CharField(max_length=2, db_column='EstadoSigla')
    site_estado = models.URLField(null=True, blank=True, db_column='SiteEstado')
    site_cidade = models.URLField(null=True, blank=True, db_column='SiteCidade')
    site_junta_unificada = models.URLField(null=True, blank=True, db_column='SiteJuntaUnificada')
    site_junta_antiga = models.URLField(null=True, blank=True, db_column='SiteJuntaAntiga')
    site_alvara1 = models.URLField(null=True, blank=True, db_column='SiteAlvara1')
    site_alvara2 = models.URLField(null=True, blank=True, db_column='SiteAlvara2')
    site_alvara_pedido1 = models.URLField(null=True, blank=True, db_column='SiteAlvaraPedido1')
    site_alvara_pedido2 = models.URLField(null=True, blank=True, db_column='SiteAlvaraPedido2')
    site_pref_protocolo = models.URLField(null=True, blank=True, db_column='SitePrefProtocolo')
    observacoes = models.TextField(null=True, blank=True, db_column='Observacoes')
    site_redesim_protocolo = models.URLField(null=True, blank=True, db_column='SiteREDESIMProtocolo')
    site_redesim_consulta_cnpj = models.URLField(null=True, blank=True, db_column='SiteREDESIMConsultaCNPJ')
    site_redesim_abrir_cnpj = models.URLField(null=True, blank=True, db_column='SiteREDESIMAbrirCNPJ')
    site_redesim_meu_cnpj = models.URLField(null=True, blank=True, db_column='SiteREDESIMMeuCNPJ')
    bombeiro_consulta = models.URLField(null=True, blank=True, db_column='BombeiroConsulta')
    bombeiro_solicita = models.URLField(null=True, blank=True, db_column='BombeiroSolicita')
    bombeiro_unificado = models.URLField(null=True, blank=True, db_column='BombeiroUnificado')
    bombeiro_redesim = models.URLField(null=True, blank=True, db_column='BombeiroREDESIM')
    federal_ecac = models.URLField(null=True, blank=True, db_column='FederalECAC')
    federal_parc_proc = models.URLField(null=True, blank=True, db_column='FederalParcProc')
    federal_procuradoria = models.URLField(null=True, blank=True, db_column='FederalProcuradoria')

    class Meta:
        managed = False
        db_table = 'Sites'
        ordering = ['estado', 'cidade']

    def __str__(self):
        return f"{self.cidade} - {self.estado}"