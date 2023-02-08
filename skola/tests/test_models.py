from django.test import TestCase
from main.models import Profesor, Predmet, Ucenik, Ucionica

#jedini test koji radi atm


class Testmodels(TestCase):

    def setUp(self):
        self.profesor1 = Profesor.objects.create(
            profesor_ime = 'Barlo',
            profesor_prezime = 'Kabic',
            profesor_placa = 25
        )
        self.predmet1 = Predmet.objects.create(
            predmet_naziv = 'Matisa',
            predmet_opis = 'Linearna aldžebra',
            predmet_predavac = self.profesor1
        )
        self.ucenik1 = Ucenik.objects.create(
            ucenik_ime = 'Ivica',
            ucenik_prezime = 'Kostelic',
            ucenik_razrednik = self.profesor1,
        )
        self.ucionica1 = Ucionica.objects.create(
            predmet_id = self.predmet1.id,
            ucionica_broj= 2,
            ucionica_kvadratura = 80,
        )

    def test_profesor(self):
        self.assertEquals(self.profesor1.profesor_ime, "Barlo")
        self.assertEquals(self.predmet1.predmet_naziv, "Matisa")
        self.assertEquals(self.ucenik1.ucenik_ime, "Ivica")
        self.assertEquals(self.ucionica1.ucionica_broj, 2)
