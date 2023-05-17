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
    response = requests.get(
        'https://www.freetogame.com/api/games?sort-by=date')
    home = response.json()
    print(response)
    return render(request, 'base/home.html', {'home': home})

# PAGINAS

def exit(request):
    logout(request)
    return redirect('home')

def juegos(request):
    response = requests.get(
        'https://www.freetogame.com/api/games')
    games = response.json()
    print(response)
    return render(request, 'paginas/catalogo/juegos.html', {'games': games})


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
    response = requests.get(
        'https://www.freetogame.com/api/games?category=action')
    action = response.json()
    print(response)
    return render(request, 'paginas/categorias/accionAventura.html', 
    {'action': action})

def arcadeSimulacion(request):
    response = requests.get(
        'https://www.freetogame.com/api/games?category=pixel')
    pixel = response.json()
    print(response)
    return render(request, 'paginas/categorias/arcadeSimulacion.html',
    {'pixel': pixel})

def deportesMusica(request):
    response = requests.get(
        'https://www.freetogame.com/api/games?category=sports')
    sports = response.json()
    print(response)
    return render(request, 'paginas/categorias/deportesMusica.html',
    {'sports': sports})

def shooterEstrategia(request):
    response = requests.get(
        'https://www.freetogame.com/api/games?category=shooter')
    shoot = response.json()
    print(response)
    return render(request, 'paginas/categorias/shooterEstrategia.html', {'shoot': shoot})

