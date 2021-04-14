from django.urls import path, include
from . import views
from .views import *

urlpatterns = [

    path('index/',views.HomePageView, name = 'base'),

    path('add/',views.inserimento, name='nuovo_libro'),
    path('detail/<Cod>/',views.LibroDetailView, name='detail'),
    path('mod/<cod>/', views.mod_libro, name= 'modifica_libro'),
    path('del/<Cod>/', views.del_libro, name='cancella'),

    path('prenotazione/', views.PrenotazioneView, name='prnt'),
    path('SLibro/', views.del_singoloView, name='delS'),
    path('ritardi/', views.PrestitoPageView, name = 'ritardi'),
    path('ResetS/<Cod>/',views.ResetSingoloView, name='reset'),
    path('DelRit/<Cod>/',views.del_singololibro, name='delrit'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',views.loginView, name='login'),
    path('register/',views.Register, name='register'),
    path('logout/',views.logoutview, name='logout'),
    path('listNew', views.Ghet, name='newList')

]
