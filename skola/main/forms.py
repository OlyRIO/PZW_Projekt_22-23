from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import *


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



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