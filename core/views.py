import os
import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from .models import Producto
from .forms import CustomUserCreationForm, agregarProductoForm, editarProductoForm


# Create your views here.

# HOME

def home(request):
   
    return render(request, 'base/home.html', {'home': home})




# PERFILES

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

@login_required
def perfil(request):
    return render(request, 'paginas/perfil.html')

@login_required
def editarPerfil(request):
    return render(request, 'paginas/editarPerfil.html')

def exit(request):
    logout(request)
    return redirect('home')





# CARRO DE COMPRAS

def carritoCompras(request):
    return render(request, 'paginas/productos/carritoCompras.html')




# MANTENEDOR PRODUCTOS

@login_required
def inventarioProducto(request):
    productos = Producto.objects.all()
    form_editar = editarProductoForm()
    context = {
        'productos': productos,
        'form_editar':form_editar
    }
  
    return render(request, 'paginas/productos/inventario.html', context)

@login_required
def agregarProducto(request):
    
    if request.method == 'POST':
        form = agregarProductoForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('inventario')
    else:
        form = agregarProductoForm()
        context = {
            'form': form
        }
    return render(request, 'paginas/productos/agregarProducto.html', context)

@login_required
def editarProducto(request):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=request.POST.get('id_producto_editar'))
        form_editar = editarProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if form_editar.is_valid():
            form_editar.save()
        return redirect('inventario')
    else:
        form_editar = editarProductoForm()
        context = {
            'form_editar': form_editar
        }
    return render(request, 'paginas/productos/inventario.html', context)

@login_required
def eliminarProducto(request):
    if request.POST:
        productos = Producto.objects.get(pk=request.POST.get('id_producto_eliminar'))
        productos.delete()    
  
    return redirect('inventario')




# CONTACTO FORM

def contacto(request):
    return render(request, 'paginas/informacion/contacto.html')



# PRODUCTOS

def juegos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
  
    return render(request, 'paginas/catalogo/juegos.html', context)

def accesorios(request):
    return render(request, 'paginas/catalogo/accesorios.html')

def accionAventura(request):
    response = requests.get(
        'https://www.freetogame.com/api/games?category=action&category=fighting&sort-by=release-date')
    action = response.json()
    print(response)
    return render(request, 'paginas/categorias/accionAventura.html', 
    {'action': action})

def arcadeSimulacion(request):
    response = requests.get(
        'https://www.freetogame.com/api/games?category=ARPG&category=pixel&sort-by=release-date')
    pixel = response.json()
    print(response)
    return render(request, 'paginas/categorias/arcadeSimulacion.html',
    {'pixel': pixel})

def deportesMusica(request):
    response = requests.get(
        'https://www.freetogame.com/api/games?category=racing&category=sports&sort-by=release-date')
    sports = response.json()
    print(response)
    return render(request, 'paginas/categorias/deportesMusica.html',
    {'sports': sports})

def shooterEstrategia(request):
    response = requests.get(
        'https://www.freetogame.com/api/games?category=shooter&category=strategy')
    shoot = response.json()
    print(response)
    return render(request, 'paginas/categorias/shooterEstrategia.html', {'shoot': shoot})

