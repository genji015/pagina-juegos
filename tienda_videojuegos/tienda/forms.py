from django import forms
from .models import Videojuego, Consola, Accesorio

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = '__all__'

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = '__all__'

class AccesorioForm(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = '__all__'