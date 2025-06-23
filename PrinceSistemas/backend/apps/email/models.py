from django.db import models

class Email(models.Model):
    id_email = models.AutoField(db_column='ID_eMail', primary_key=True)
    email = models.TextField(db_column='eMail', blank=True, null=True)
    senhaemail = models.TextField(db_column='SenhaEmail', blank=True, null=True)
    smtpclient = models.TextField(db_column='SmtpClient', blank=True, null=True)
    smtpport = models.TextField(db_column='SmtpPort', blank=True, null=True)
    clientssl = models.TextField(db_column='clientSsl', blank=True, null=True)
    caixadesaida = models.TextField(db_column='CaixaDeSaida', blank=True, null=True)
    parageral = models.TextField(db_column='ParaGeral', blank=True, null=True)
    habilitassl = models.TextField(db_column='HabilitaSsl', blank=True, null=True)
    credencial = models.TextField(db_column='Credencial', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eMail'
        ordering = ['id_email']

class Emailcaixadesaida(models.Model):
    id_emailcaixadesaida = models.AutoField(db_column='ID_eMailCaixaDeSaida', primary_key=True)
    idemailprincipal = models.TextField(db_column='IDeMailPrincipal', blank=True, null=True)
    emailprincipal = models.TextField(db_column='eMailPrincipal', blank=True, null=True)
    emaildestino = models.TextField(db_column='eMailDestino', blank=True, null=True)
    assunto = models.TextField(db_column='Assunto', blank=True, null=True)
    caixadesaidatexto = models.TextField(db_column='CaixaDeSaidaTexto', blank=True, null=True)
    dataenviado = models.DateTimeField(db_column='DataEnviado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eMailCaixaDeSaida'