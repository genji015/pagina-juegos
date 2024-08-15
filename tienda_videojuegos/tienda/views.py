from django.shortcuts import render, redirect
from .forms import VideojuegoForm, ConsolaForm, AccesorioForm
from .models import Videojuego, Consola, Accesorio

def index(request):
    return render(request, 'tienda/base.html')

def agregar_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VideojuegoForm()
    return render(request, 'tienda/agregar_videojuego.html', {'form': form})

def agregar_consola(request):
    if request.method == 'POST':
        form = ConsolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ConsolaForm()
    return render(request, 'tienda/agregar_consola.html', {'form': form})

def agregar_accesorio(request):
    if request.method == 'POST':
        form = AccesorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AccesorioForm()
    return render(request, 'tienda/agregar_accesorio.html', {'form': form})

def buscar(request):
    query = request.GET.get('q')
    if query:
        resultados_videojuegos = Videojuego.objects.filter(nombre__icontains=query)
        resultados_consolas = Consola.objects.filter(nombre__icontains=query)
        resultados_accesorios = Accesorio.objects.filter(nombre__icontains=query)
    else:
        resultados_videojuegos = []
        resultados_consolas = []
        resultados_accesorios = []

    return render(request, 'tienda/buscar.html', {
        'resultados_videojuegos': resultados_videojuegos,
        'resultados_consolas': resultados_consolas,
        'resultados_accesorios': resultados_accesorios,
    })

# Create your views here.
