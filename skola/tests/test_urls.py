from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import index, ProfesorList, UcenikList, UcionicaList, PredmetList


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, index)

    def test_profesori_url_is_resolved(self):
        url = reverse('profesori')

        self.assertEquals(resolve(url).func.view_class, ProfesorList)

    def test_authors_url_is_resolved(self):
        url = reverse('ucenici')

        self.assertEquals(resolve(url).func.view_class, UcenikList)

    def test_authors_url_is_resolved(self):
        url = reverse('ucionice')
        print("Nešto se desilo.")

        self.assertEquals(resolve(url).func.view_class, UcionicaList)
    def test_authors_url_is_resolved(self):
        url = reverse('predmeti')

        self.assertEquals(resolve(url).func.view_class, PredmetList)
