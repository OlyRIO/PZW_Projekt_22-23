from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import index, ProfesorList, UcenikList, UcionicaList, PredmetList, register_request


#radi mićila

class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('main:homepage')
        print(resolve(url))

        self.assertEquals(resolve(url).func, index)

    def test_profesori_url_is_resolved(self):
        url = reverse('main:profesori')

        self.assertEquals(resolve(url).func.view_class, ProfesorList)

    def test_ucenici_url_is_resolved(self):
        url = reverse('main:ucenici')

        self.assertEquals(resolve(url).func.view_class, UcenikList)

    def test_ucionice_url_is_resolved(self):
        url = reverse('main:ucionice')

        self.assertEquals(resolve(url).func.view_class, UcionicaList)
    def test_predmeti_url_is_resolved(self):
        url = reverse('main:predmeti')

        self.assertEquals(resolve(url).func.view_class, PredmetList)
