import os
import requests
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .cart import Cart
from .models import Producto, User
from .forms import CustomUserCreationForm, agregarProductoForm, editarProductoForm, CartAddProductoForm, editarPerfilForm


# Create your views here.

# HOME

def home(request):
    print(request.session.session_key)

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
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.POST.get('id_perfil_editar'))
        form = editarPerfilForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('perfil')
    else:
        form = editarPerfilForm()
        context = {
            'form': form
        }
    return render(request, 'paginas/perfil.html', context)


def exit(request):
    logout(request)
    return redirect('home')





# CARRO DE COMPRAS

def carritoCompras(request):
    
    return render(request, 'paginas/productos/carritoCompras.html')



def cart_add(request, producto_id):

  cart = Cart(request)
  producto = get_object_or_404(Producto, id=producto_id)

  form = CartAddProductoForm(request.POST)
  if form.is_valid():
    cart_add = form.cleaned_data
    cart.add(
      producto=producto,
      cantidad=cart_add["cantidad"],
      override_cantidad=cart_add["override"]
    )

  return redirect("carritoCompras")




def cart_eliminar(request, producto_id):

  cart = Cart(request)
  producto = get_object_or_404(Producto, id=producto_id)
  cart.remove(producto)
  return redirect("carritoCompras")





def cart_clear(request):
  cart = Cart(request)
  cart.clear()
  return redirect("carritoCompras")


def cart_detalle(request):
  cart = Cart(request)
  return render(request, "paginas/productos/carritoCompras.html", {"cart": cart})





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
    
    productos = Producto.objects.filter(tipo_producto='Juego')
    context = {
        'productos': productos
    }
    extra_context = {"form": CartAddProductoForm()}
    return render(request, 'paginas/catalogo/juegos.html', context)


def accionAventura(request):
    productos = Producto.objects.filter(
                                        Q(categoria='Acción')|
                                        Q(categoria='Aventura'))                                    
    context = {
        'productos': productos
    }
    extra_context = {"form": CartAddProductoForm()}
    return render(request, 'paginas/categorias/accionAventura.html', context)

def arcadeSimulacion(request):
    productos = Producto.objects.filter(
                                        Q(categoria='Arcade')|
                                        Q(categoria='Simulación'))                                    
    context = {
        'productos': productos
    }
    extra_context = {"form": CartAddProductoForm()}
    return render(request, 'paginas/categorias/arcadeSimulacion.html', context)

def deportesMusica(request):
    productos = Producto.objects.filter(
                                        Q(categoria='Deportes')|
                                        Q(categoria='Carreras')|
                                        Q(categoria='Música'))                                    
    context = {
        'productos': productos
    }
    extra_context = {"form": CartAddProductoForm()}
    return render(request, 'paginas/categorias/deportesMusica.html', context)

def shooterEstrategia(request):
    productos = Producto.objects.filter(
                                        Q(categoria='Shooter')|
                                        Q(categoria='Estrategia')|
                                        Q(categoria='RPG')|
                                        Q(categoria='Puzzle')|  
                                        Q(categoria='Plataformas')   )                                 
    context = {
        'productos': productos
    }
    extra_context = {"form": CartAddProductoForm()}
    return render(request, 'paginas/categorias/shooterEstrategia.html', context)


def accesorios(request):
    productos = Producto.objects.filter(tipo_producto='Accesorio')
    context = {
        'productos': productos
    }
    extra_context = {"form": CartAddProductoForm()}
    return render(request, 'paginas/catalogo/accesorios.html', context)



