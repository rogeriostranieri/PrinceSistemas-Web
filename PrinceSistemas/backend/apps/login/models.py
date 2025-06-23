from django.db import models

class Login(models.Model):
    NIVEL_CHOICES = [
        ('A', 'Administrador'),
        ('G', 'Gerente'),
        ('C', 'Comum')
    ]
    
    id_login = models.AutoField(primary_key=True, db_column='id_login')
    usuario = models.CharField(max_length=150, db_column='usuario')
    senha = models.CharField(max_length=128, db_column='senha')  # texto puro, pois o banco está assim
    nome_completo = models.CharField(max_length=255, db_column='nomecompleto', blank=True, null=True)
    tema = models.CharField(max_length=50, db_column='tema', blank=True, null=True)
    datanascimento = models.CharField(max_length=20, db_column='datanascimento', blank=True, null=True)
    email = models.CharField(max_length=255, db_column='email', blank=True, null=True)
    nivel_acesso = models.CharField(max_length=1, db_column='nivel_acesso', choices=NIVEL_CHOICES, default='C', blank=True, null=True)

    class Meta:
        db_table = 'Login'
        managed = False  # Não deixa o Django tentar criar/alterar a tabela
        ordering = ['usuario']

    def __str__(self):
        return self.usuario

    def check_password(self, raw_password):
        # Como não pode alterar o banco, compara texto puro
        return self.senha == raw_password
        
    @property
    def is_admin(self):
        return self.nivel_acesso == 'A'
        
    @property
    def is_gerente(self):
        return self.nivel_acesso == 'G'
