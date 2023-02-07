from django.test import TestCase
from main.models import Profesor, Predmet, Ucenik, Ucionica

class Testmodels(TestCase):

    def setUp(self):
        self.profesor1 = Profesor.objects.create(
            ime = 'TestName',
            prezime = 'TestSurr',
            placa = 'TestPaycheck'
        )

    def test_author(self):
        self.assertEquals(self.author1.name, "Penis")
