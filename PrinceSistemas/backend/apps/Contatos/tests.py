from django.test import TestCase
from .models import Contato

class ContatoModelTest(TestCase):

    def setUp(self):
        Contato.objects.create(
            Nome="John",
            Sobrenome="Doe",
            Telefone_Residencial="123456789",
            Telefone_Trabalho="987654321",
            Telefone_Celular_Particular="555555555",
            Telefone_Celular_Contato="666666666",
            email="john.doe@example.com",
            End_CEP="12345-678",
            End_Rua="Main St",
            End_Numero="100",
            End_Comp="Apt 1",
            End_Bairro="Downtown",
            End_Cidade="Metropolis",
            End_Estado="NY",
            End_Pais="USA",
            Outras_Informacoes="No additional info",
            Data="2023-01-01"
        )

    def test_contato_creation(self):
        contato = Contato.objects.get(Nome="John")
        self.assertEqual(contato.Sobrenome, "Doe")
        self.assertEqual(contato.Telefone_Residencial, "123456789")
        self.assertEqual(contato.email, "john.doe@example.com")