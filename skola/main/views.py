from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from main.models import Profesor, Ucenik, Ucionica, Predmet
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect


## Create your views here.
def index(request):
    return render(request, 'main/homepage.html')

class ProfesorList(ListView):
    model = Profesor


class UcenikList(ListView):
    model = Ucenik



class UcionicaList(ListView):
    model = Ucionica


class PredmetList(ListView):
    model = Predmet


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def add_profesor(request):
    submitted = False
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ProfesorForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_profesor.html', {'form':form, 'submitted':submitted})

def add_predmet(request):
    submitted = False
    if request.method == "POST":
        form = PredmetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = PredmetForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_predmet.html', {'form':form, 'submitted':submitted})

def add_ucenik(request):
    submitted = False
    if request.method == "POST":
        form = UcenikForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = UcenikForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_ucenik.html', {'form':form, 'submitted':submitted})

def add_ucionica(request):
    submitted = False
    if request.method == "POST":
        form = UcionicaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = UcionicaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_ucionica.html', {'form':form, 'submitted':submitted})
