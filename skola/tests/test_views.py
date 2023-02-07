from django.test import TestCase, Client
from django.urls import reverse
from main.models import Profesor, Predmet, Ucenik, Ucionica


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('')
        self.profesor = reverse('profesori')
        self.predmet = reverse('predmeti')
        self.ucenik = reverse('ucenici')
        self.ucionica = reverse('ucionice')

        self.profesor1 = Profesor.objects.create(
            ime = 'TestName',
            prezime = 'TestSurr',
            placa = 'TestPaycheck',
        )

    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')

    def test_project_profesor_GET(self):
        client = Client()

        response = client.get(self.profesor)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/profesor_list.html')
