from django.test import TestCase
from ..models import CADSituacaoAlvara

class CADSituacaoAlvaraModelTest(TestCase):
    def setUp(self):
        self.situacao = CADSituacaoAlvara.objects.create(Descricao='Teste')

    def test_str(self):
        self.assertEqual(str(self.situacao), 'Teste')
        
    def test_verbose_name(self):
        self.assertEqual(
            CADSituacaoAlvara._meta.verbose_name, 'Situação do Alvará'
        )
        
    def test_verbose_name_plural(self):
        self.assertEqual(
            CADSituacaoAlvara._meta.verbose_name_plural, 'Situações dos Alvarás'
        )