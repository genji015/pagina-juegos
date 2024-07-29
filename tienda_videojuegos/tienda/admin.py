from django.contrib import admin
from tienda.models import Videojuego, Consola, Accesorio

# Register your models here.

admin.site.register(Videojuego)
admin.site.register(Consola)
admin.site.register(Accesorio)