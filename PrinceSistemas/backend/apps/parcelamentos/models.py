from django.db import models

class Parcelamento(models.Model):
    id_parcel = models.AutoField(primary_key=True, db_column='ID_Parcel')
    razao_social = models.TextField(db_column='RazaoSocial', blank=True, null=True)
    cnpj = models.TextField(db_column='CNPJ', blank=True, null=True)
    forma_envio = models.TextField(db_column='FormaDeEnvio', blank=True, null=True)
    responsavel = models.TextField(db_column='Responsavel', blank=True, null=True)
    whatsapp = models.TextField(db_column='Whatsapp', blank=True, null=True)
    email = models.TextField(db_column='Email', blank=True, null=True)
    socio = models.TextField(db_column='Socio', blank=True, null=True)
    cpf = models.TextField(db_column='CPF', blank=True, null=True)
    senhagov = models.TextField(db_column='SenhaGov', blank=True, null=True)
    data_criacao = models.TextField(db_column='DataCriacao', blank=True, null=True)
    data_lembrete = models.TextField(db_column='DataLembrete', blank=True, null=True)
    data_finalizado = models.TextField(db_column='DataFinalizado', blank=True, null=True)
    mei = models.TextField(db_column='MEI', blank=True, null=True)
    inss_antigo = models.TextField(db_column='InssAntigo', blank=True, null=True)
    inss_novo = models.TextField(db_column='InssNovo', blank=True, null=True)
    inss_procur = models.TextField(db_column='InssProcur', blank=True, null=True)
    data_solic_mei = models.TextField(db_column='DataSolicMEI', blank=True, null=True)
    data_envia_mei = models.TextField(db_column='DataEnviaMEI', blank=True, null=True)
    data_final_mei = models.TextField(db_column='DataFinalMEI', blank=True, null=True)
    motivo_mei = models.TextField(db_column='MotivoMEI', blank=True, null=True)
    prot_mei = models.TextField(db_column='ProtMEI', blank=True, null=True)
    total_parc_mei = models.TextField(db_column='TotalParcMEI', blank=True, null=True)
    envia_parc_mei = models.TextField(db_column='EnviaParcMEI', blank=True, null=True)
    data_solic_antigo = models.TextField(db_column='DataSolicAntigo', blank=True, null=True)
    data_envia_antigo = models.TextField(db_column='DataEnviaAntigo', blank=True, null=True)
    data_final_antigo = models.TextField(db_column='DataFinalAntigo', blank=True, null=True)
    motivo_antigo = models.TextField(db_column='MotivoAntigo', blank=True, null=True)
    prot_antigo = models.TextField(db_column='ProtAntigo', blank=True, null=True)
    total_parc_antigo = models.TextField(db_column='TotalParcAntigo', blank=True, null=True)
    envia_parc_antigo = models.TextField(db_column='EnviaParcAntigo', blank=True, null=True)
    data_solic_novo = models.TextField(db_column='DataSolicNovo', blank=True, null=True)
    data_envio_novo = models.TextField(db_column='DataEnvioNovo', blank=True, null=True)
    data_final_novo = models.TextField(db_column='DataFinalNovo', blank=True, null=True)
    motivo_novo = models.TextField(db_column='MotivoNovo', blank=True, null=True)
    prot_novo = models.TextField(db_column='ProtNovo', blank=True, null=True)
    total_parc_novo = models.TextField(db_column='TotalParcNovo', blank=True, null=True)
    envia_parc_novo = models.TextField(db_column='EnviaParcNovo', blank=True, null=True)
    data_solic_proc = models.TextField(db_column='DataSolicProc', blank=True, null=True)
    data_envia_proc = models.TextField(db_column='DataEnviaProc', blank=True, null=True)
    data_final_proc = models.TextField(db_column='DataFinalProc', blank=True, null=True)
    motivo_proc = models.TextField(db_column='MotivoProc', blank=True, null=True)
    prot_proc = models.TextField(db_column='Protproc', blank=True, null=True)
    total_parc_proc = models.TextField(db_column='TotalParcProc', blank=True, null=True)
    envia_parc_proc = models.TextField(db_column='EnviaParcProc', blank=True, null=True)
    parcel_env_mei = models.TextField(db_column='ParcelEnvMEI', blank=True, null=True)
    parcel_env_inss_ant = models.TextField(db_column='ParcelEnvINSSAnt', blank=True, null=True)
    parcel_env_inss_nov = models.TextField(db_column='ParcelEnvINSSNov', blank=True, null=True)
    parcel_env_inss_proc = models.TextField(db_column='ParcelEnvINSSProc', blank=True, null=True)
    finalizado_empresa = models.TextField(db_column='FinalizadoEmpresa', blank=True, null=True)
    finalizado_mei = models.TextField(db_column='FinalizadoMEI', blank=True, null=True)
    finalizado_inss_ant = models.TextField(db_column='FinalizadoINSSAnt', blank=True, null=True)
    finalizado_inss_nov = models.TextField(db_column='FinalizadoINSSNov', blank=True, null=True)
    finalizado_inss_proc = models.TextField(db_column='FinalizadoINSSProc', blank=True, null=True)
    finalizado_mes_geral = models.TextField(db_column='FinalizadoMesGeral', blank=True, null=True)
    geral = models.TextField(db_column='Geral', blank=True, null=True)
    para_fazer = models.TextField(db_column='ParaFazer', blank=True, null=True)
    atraso_parcela_mei = models.TextField(db_column='AtrasoParcelaMEI', blank=True, null=True)
    atraso_parcela_inss_antigo = models.TextField(db_column='AtrasoParcelaINSSAntigo', blank=True, null=True)
    atraso_parcela_inss_novo = models.TextField(db_column='AtrasoParcelaINSSNovo', blank=True, null=True)
    atraso_parcela_inss_procu = models.TextField(db_column='AtrasoParcelaINSSProcu', blank=True, null=True)

    class Meta:
        db_table = "Parcelamentos"
        managed = False  # Mantido como False, pois a tabela já existe

    def __str__(self):
        return self.razao_social

    def format_documento(self):
        """
        Formata o CNPJ/CPF de forma consistente
        """
        if not self.cnpj:
            return None
        
        # Remove todos os caracteres não numéricos
        doc = ''.join(filter(str.isdigit, self.cnpj))
        
        # Verifica se é CNPJ ou CPF
        if len(doc) == 14:  # CNPJ
            return f"{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}"
        elif len(doc) == 11:  # CPF
            return f"{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:]}"
        
        return self.cnpj  # Retorna original se não for 11 ou 14 dígitos