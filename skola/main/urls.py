from django.urls import path
from . import views
from main.views import ProfesorList, UcenikList, UcionicaList, PredmetList

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('profesori/', ProfesorList.as_view(), name='profesori'),
    path('ucenici/', UcenikList.as_view(), name='ucenici'),
    path('ucionice/', UcionicaList.as_view(), name='ucionice'),
    path('predmeti/', PredmetList.as_view(), name='predmeti'),
    path('', views.index, name='homepage'),
    path('register/', views.register_request, name='register'),
    path('add_profesor/', views.add_profesor),
    path('add_predmet/', views.add_predmet),
    path('add_ucenik/', views.add_ucenik),
    path('add_ucionica/', views.add_ucionica),
]