import os
import requests

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from .forms import CustomUserCreationForm


# Create your views here.

# HOME


def home(request):
    return render(request, 'base/home.html')

# PAGINAS

def exit(request):
    logout(request)
    return redirect('home')

def juegos(request):
    response = requests.get(
        'https://api.rawg.io/api/games?key=b40d42ec4f374f75aa29ef424c698357')
    games = response.json()
    print(response)
    return render(request, 'paginas/catalogo/juegos.html', {'games': games['results']})


def accesorios(request):
    return render(request, 'paginas/catalogo/accesorios.html')

@login_required
def perfil(request):
    return render(request, 'paginas/perfil.html')

def contacto(request):
    return render(request, 'paginas/informacion/contacto.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data = request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'] )
            login (request, user)

            return redirect('home') 

    return render(request, 'registration/register.html', data)

def carritoCompras(request):
    return render(request, 'paginas/productos/carritoCompras.html')

@login_required
def agregarProducto(request):
    return render(request, 'paginas/productos/agregarProducto.html')

def accionAventura(request):
    return render(request, 'paginas/categorias/accionAventura.html')

def arcadeSimulacion(request):
    return render(request, 'paginas/categorias/arcadeSimulacion.html')

def deportesMusica(request):
    return render(request, 'paginas/categorias/deportesMusica.html')

def shooterEstrategia(request):
    return render(request, 'paginas/categorias/shooterEstrategia.html')

