from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from main.models import Profesor, Ucenik, Ucionica, Predmet
from .forms import *

## Create your views here.
def homepage(request):
    return HttpResponse('Welcome to homepage! <strong>#samoOIRI</strong>')
    # primjetiti korištenje HTML-a


class ProfesorList(ListView):
    model = Profesor


class UcenikList(ListView):
    model = Ucenik



class UcionicaList(ListView):
    model = Ucionica


class PredmetList(ListView):
    model = Predmet

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