from django.db import models

class Telefone(models.Model):
    ID_Telefones = models.AutoField(primary_key=True)
    Nome = models.TextField(blank=True, null=True, verbose_name="Nome")
    Telefone1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Telefone Principal")
    TelefoneOutros = models.CharField(max_length=255, blank=True, null=True, verbose_name="Outros Telefones")
    Obs = models.TextField(blank=True, null=True, verbose_name="Observações")
    CEP = models.CharField(max_length=20, blank=True, null=True, verbose_name="CEP")
    Endereço = models.TextField(blank=True, null=True, verbose_name="Endereço")
    Numero = models.TextField(blank=True, null=True, verbose_name="Número")
    Complemento = models.TextField(blank=True, null=True, verbose_name="Complemento")
    Bairro = models.TextField(blank=True, null=True, verbose_name="Bairro")
    Cidade = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cidade")
    Estado = models.CharField(max_length=255, blank=True, null=True, verbose_name="Estado")
    email = models.TextField(blank=True, null=True, verbose_name="E-mail")
    site = models.TextField(blank=True, null=True, verbose_name="Site")
    
    # Usar BooleanField com custom getter/setter para compatibilidade
    # Especificar o nome exato das colunas no banco de dados
    OrgaoEstado = models.TextField(blank=True, null=True, verbose_name="Órgão Estadual", db_column="orgaoestado")
    OrgaoCidade = models.TextField(blank=True, null=True, verbose_name="Órgão Municipal", db_column="orgaocidade")
    OrgaoFederal = models.TextField(blank=True, null=True, verbose_name="Órgão Federal", db_column="orgaofederal")

    class Meta:
        db_table = 'Telefones'
        managed = False
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
        ordering = ['Nome']
    
    def get_orgao_federal(self):
        """Converte o valor de texto para booleano"""
        return self.OrgaoFederal == 'true'
    
    def set_orgao_federal(self, value):
        """Converte o valor booleano para texto"""
        self.OrgaoFederal = 'true' if value else 'false'
    
    def get_orgao_estadual(self):
        """Converte o valor de texto para booleano"""
        return self.OrgaoEstado == 'true'
    
    def set_orgao_estadual(self, value):
        """Converte o valor booleano para texto"""
        self.OrgaoEstado = 'true' if value else 'false'
    
    def get_orgao_municipal(self):
        """Converte o valor de texto para booleano"""
        return self.OrgaoCidade == 'true'
    
    def set_orgao_municipal(self, value):
        """Converte o valor booleano para texto"""
        self.OrgaoCidade = 'true' if value else 'false'
    
    # Propriedades para acessar como booleanos
    is_orgao_federal = property(get_orgao_federal, set_orgao_federal)
    is_orgao_estadual = property(get_orgao_estadual, set_orgao_estadual)
    is_orgao_municipal = property(get_orgao_municipal, set_orgao_municipal)
    
    def __str__(self):
        return self.Nome or "Sem nome"