from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('index/',views.HomePageView, name = 'base'),
    path('add/',views.inserimento, name='nuovo_libro'),
    path('detail/<Cod>/',views.LibroDetailView, name='detail'),
    path('mod/<Cod>/', views.mod_libro, name= 'modifica_libro'),
    path('del<Cod>/', views.del_libro, name='cancella')
]
