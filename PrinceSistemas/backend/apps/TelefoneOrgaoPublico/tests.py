from django.test import TestCase
from .models import TelefoneOrgaoPublico

class TelefoneOrgaoPublicoModelTest(TestCase):
    def setUp(self):
        TelefoneOrgaoPublico.objects.create(
            Nome="Teste",
            Telefone1="123456789",
            TelefoneOutros="987654321",
            Obs="Observação de teste",
            CEP="12345-678",
            Endereço="Rua Teste",
            Numero="123",
            Complemento="Apto 1",
            Bairro="Bairro Teste",
            Cidade="Cidade Teste",
            Estado="Estado Teste",
            email="teste@example.com",
            site="http://example.com",
            OrgaoEstado="Órgão Estado Teste",
            OrgaoCidade="Órgão Cidade Teste"
        )

    def test_telefone_orgao_publico_creation(self):
        telefone = TelefoneOrgaoPublico.objects.get(Nome="Teste")
        self.assertEqual(telefone.Telefone1, "123456789")
        self.assertEqual(telefone.Cidade, "Cidade Teste")
        self.assertEqual(telefone.email, "teste@example.com")