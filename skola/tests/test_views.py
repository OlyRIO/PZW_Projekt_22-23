from django.test import TestCase, Client
from django.urls import reverse
from main.models import Profesor, Predmet, Ucenik, Ucionica

#drugi test isto radi WOOOOOO

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('main:homepage')
        self.profesor = reverse('main:profesori')
        self.predmet = reverse('main:predmeti')
        self.ucenik = reverse('main:ucenici')
        self.ucionica = reverse('main:ucionice')
        self.register = reverse('main:register')

        self.profesor1 = Profesor.objects.create(
            profesor_ime = 'TestName',
            profesor_prezime = 'TestSurr',
            profesor_placa = 20,
        )

    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/homepage.html')

    def test_project_profesor_GET(self):
        client = Client()

        response = client.get(self.profesor)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/profesor_list.html')
    
    def test_project_predmet_GET(self):
        client = Client()

        response = client.get(self.predmet)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/predmet_list.html')

    def test_project_ucenik_GET(self):
        client = Client()

        response = client.get(self.ucenik)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/ucenik_list.html')

    def test_project_ucionica_GET(self):
        client = Client()

        response = client.get(self.ucionica)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/ucionica_list.html')


    def test_project_register_GET(self):
        client = Client()

        response = client.get(self.register)
        self.assertEquals(response.status_code, 200)

