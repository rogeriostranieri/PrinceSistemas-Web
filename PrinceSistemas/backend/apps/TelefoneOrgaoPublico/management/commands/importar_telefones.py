from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Importa dados da tabela "Telefones" do banco de dados.'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT "ID_Telefones", "Nome", "Telefone1", "TelefoneOutros", "Obs", "CEP", "Endereço", "Numero", "Complemento", "Bairro", "Cidade", "Estado", email, site, "OrgaoEstado", "OrgaoCidade"
                FROM public."Telefones";
            """)
            telefones = cursor.fetchall()

            for telefone in telefones:
                self.stdout.write(str(telefone))  # Aqui você pode adicionar a lógica para processar os dados conforme necessário.