from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_videojuego/', views.agregar_videojuego, name='agregar_videojuego'),
    path('agregar_consola/', views.agregar_consola, name='agregar_consola'),
    path('agregar_accesorio/', views.agregar_accesorio, name='agregar_accesorio'),
    path('buscar/', views.buscar, name='buscar'),
]