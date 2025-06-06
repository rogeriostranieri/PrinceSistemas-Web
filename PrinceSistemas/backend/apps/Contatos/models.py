from django.db import models

class Contato(models.Model):
    ID_Contatos = models.SmallIntegerField(primary_key=True, verbose_name="ID")
    Nome = models.TextField(blank=True, null=True, verbose_name="Nome")
    Sobrenome = models.TextField(blank=True, null=True, verbose_name="Sobrenome")
    Telefone_Residencial = models.TextField(blank=True, null=True, verbose_name="Telefone Residencial")
    Telefone_Trabalho = models.TextField(blank=True, null=True, verbose_name="Telefone Trabalho")
    Telefone_Celular_Particular = models.TextField(blank=True, null=True, verbose_name="Celular Particular")
    Telefone_Celular_Contato = models.TextField(blank=True, null=True, verbose_name="Celular Contato")
    email = models.TextField(blank=True, null=True, verbose_name="E-mail")
    End_CEP = models.TextField(blank=True, null=True, verbose_name="CEP")
    End_Rua = models.TextField(blank=True, null=True, verbose_name="Rua")
    End_Numero = models.TextField(blank=True, null=True, verbose_name="Número")
    End_Comp = models.TextField(blank=True, null=True, verbose_name="Complemento")
    End_Bairro = models.TextField(blank=True, null=True, verbose_name="Bairro")
    End_Cidade = models.TextField(blank=True, null=True, verbose_name="Cidade")
    End_Estado = models.TextField(blank=True, null=True, verbose_name="Estado")
    End_Pais = models.TextField(blank=True, null=True, verbose_name="País")
    Outras_Informacoes = models.TextField(blank=True, null=True, verbose_name="Outras Informações")
    Data = models.TextField(blank=True, null=True, verbose_name="Data")

    def __str__(self):
        return f"{self.Nome} {self.Sobrenome}" if self.Sobrenome else self.Nome or "Sem nome"
    
    def nome_completo(self):
        """Retorna o nome completo do contato"""
        if self.Nome and self.Sobrenome:
            return f"{self.Nome} {self.Sobrenome}"
        return self.Nome or "Sem nome"
    
    def endereco_completo(self):
        """Retorna o endereço completo formatado"""
        partes = []
        if self.End_Rua:
            endereco = self.End_Rua
            if self.End_Numero:
                endereco += f", {self.End_Numero}"
            partes.append(endereco)
        if self.End_Comp:
            partes.append(self.End_Comp)
        if self.End_Bairro:
            partes.append(self.End_Bairro)
        if self.End_Cidade:
            cidade_estado = self.End_Cidade
            if self.End_Estado:
                cidade_estado += f" - {self.End_Estado}"
            partes.append(cidade_estado)
        if self.End_CEP:
            partes.append(f"CEP: {self.End_CEP}")
        if self.End_Pais and self.End_Pais.lower() != "brasil":
            partes.append(self.End_Pais)
        
        return ", ".join(partes) if partes else "Endereço não informado"
    
    class Meta:
        db_table = 'Contatos'
        managed = False
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['Nome', 'Sobrenome']