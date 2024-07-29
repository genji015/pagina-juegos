from django.db import models

# Create your models here.

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)