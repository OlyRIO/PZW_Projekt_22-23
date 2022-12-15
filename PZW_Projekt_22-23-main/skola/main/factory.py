import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory
class ProfesorFactory(DjangoModelFactory):
    class Meta:
        model = Profesor

    profesor_ime = factory.Faker("first_name")
    profesor_prezime = factory.Faker("last_name")
    profesor_placa = factory.Faker("paycheck")


class UcenikFactory(DjangoModelFactory):
    class Meta:
        model = Ucenik


class UcionicaFactory(DjangoModelFactory):
    class Meta:
        model = Ucionica


class PredmetFactory(DjangoModelFactory):
    class Meta:
        model = Predmet
