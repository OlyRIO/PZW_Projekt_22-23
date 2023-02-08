from django import forms
from django.forms import ModelForm
from .models import *

# Kreiranje formi
class ProfesorForm(forms.ModelForm):
    
    class Meta:
        model = Profesor
        fields = ('profesor_ime', 'profesor_prezime', 'profesor_placa')
        
class PredmetForm(forms.ModelForm):
    
    class Meta:
        model = Predmet
        fields = ('predmet_naziv', 'predmet_opis', 'predmet_predavac')
        
class UcenikForm(forms.ModelForm):
    
    class Meta:
        model = Ucenik
        fields = ('ucenik_ime', 'ucenik_prezime', 'ucenik_predmeti', 'ucenik_razrednik')

class UcionicaForm(forms.ModelForm):
    
    class Meta:
        model = Ucionica
        fields = ('predmet', 'ucionica_broj', 'ucionica_kvadratura')
        