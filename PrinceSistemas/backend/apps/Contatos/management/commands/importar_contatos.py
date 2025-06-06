from django.core.management.base import BaseCommand
from backend.apps.Contatos.models import Contato  # Ajuste o caminho conforme necessário
import csv

class Command(BaseCommand):
    help = 'Importa contatos de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV a ser importado')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contato = Contato(
                    Nome=row['Nome'],
                    Sobrenome=row['Sobrenome'],
                    Telefone_Residencial=row['Telefone_Residencial'],
                    Telefone_Trabalho=row['Telefone_Trabalho'],
                    Telefone_Celular_Particular=row['Telefone_Celular_Particular'],
                    Telefone_Celular_Contato=row['Telefone_Celular_Contato'],
                    email=row['email'],
                    End_CEP=row['End_CEP'],
                    End_Rua=row['End_Rua'],
                    End_Numero=row['End_Numero'],
                    End_Comp=row['End_Comp'],
                    End_Bairro=row['End_Bairro'],
                    End_Cidade=row['End_Cidade'],
                    End_Estado=row['End_Estado'],
                    End_Pais=row['End_Pais'],
                    Outras_Informacoes=row['Outras_Informacoes'],
                    Data=row['Data'],
                )
                contato.save()
        
        self.stdout.write(self.style.SUCCESS('Contatos importados com sucesso!'))