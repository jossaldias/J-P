import os
import requests
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .cart import Cart
from .models import Producto, User, Item, Order, Compra
from .forms import CustomUserCreationForm, agregarProductoForm, editarProductoForm, CartAddProductoForm, editarPerfilForm, OrderCreateForm, editarUsuarioForm, agregarOrdenCompraForm   


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
    form = editarPerfilForm()
    context = {
        
        'form':form
    }
    return render(request, 'registration/perfil.html', context)

@login_required
def editarPerfil(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.POST.get('id_perfil_editar'))
        form = editarPerfilForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('perfil')
    else:
        form = editarPerfilForm()
        context = {
            'form': form
        }
    return render(request, 'paginas/perfil.html', context)

@login_required
def editarUsuario(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.POST.get('id_usuario_editar'))
        form_editar = editarUsuarioForm(data=request.POST, files=request.FILES, instance=user)
        if form_editar.is_valid():
            form_editar.save()
           
        return redirect('usuarios')
    else:
        form_editar = editarUsuarioForm()
        context = {
            'form_editar': form_editar
        }
    return render(request, 'paginas/usuarios.html', context)

def exit(request):
    logout(request)
    return redirect('home')

@login_required
def usuarios(request):
    users = User.objects.all()
    form_editar = editarUsuarioForm()
    context = {
        'users': users,
        'form_editar':form_editar
    }
  
    return render(request, 'registration/usuarios.html', context)

@login_required
def agregarUsuario(request):
    
    if request.method == 'POST':
        form = editarUsuarioForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('usuarios')
    else:
        form = editarUsuarioForm()
        context = {
            'form': form
        }
    return render(request, 'registration/agregarUsuario.html', context)

@login_required
def eliminarUsuario(request):
    if request.POST:
        users = User.objects.get(pk=request.POST.get('id_usuario_eliminar'))
        users.delete()    
  
    return redirect('usuarios')


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
    print(context)
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


# CARRO DE COMPRAS

def carritoCompras(request):
    return redirect('carritoCompras')


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

def pedidoListo(request):
    
    return render(request, 'paginas/productos/pedidoListo.html')
# CONTACTO FORM

def contacto(request):
    return render(request, 'paginas/informacion/contacto.html')


#MIS COMPRAS

def misOrdenes(request):
    ordenes = Order.objects.filter(user=request.user)
    print(ordenes)
    return render(request, 'paginas/productos/misOrdenes.html',  {'ordenes': ordenes} )

#ORDENES DE COMPRA
@login_required
def ordenes(request):
    
    compras = Compra.objects.all()
    context = {
        'compras': compras,
    }

    return render(request, 'paginas/productos/ordenes.html',context)

@login_required
def agregarOrden(request):
    
    if request.method == 'POST':
        form_orden = agregarOrdenCompraForm(data = request.POST, files = request.FILES)
        if form_orden.is_valid():
            form_orden.save()
        return redirect ('ordenes')
    else:
        form_orden = agregarOrdenCompraForm()
        context = {
            'form_orden': form_orden
        }
    print(context)
    return render(request, 'paginas/productos/agregarOrden.html', context)


# PRODUCTOS

def juegos(request):
    
    productos = Producto.objects.filter(
                                        Q(tipo_producto='Juego')|
                                        Q(tipo_producto='Codigo Digital')
                                        )
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

#CREAR ORDER
class OrderCreateView(CreateView):
  model = Order
  form_class = OrderCreateForm
  template_name="order/order_form.html"

  def form_valid(self, form):
    cart = Cart(self.request)
    if cart:
      order = form.save(commit=False)
      order.user = self.request.user
      order.is_pagado = True
      order.save()
      for item in cart:
        Item.objects.create(
          orden=order,
          producto=item["producto"],
          costo=item["costo"],
          cantidad=item["cantidad"],
        )
      cart.clear()
      return render(self.request, 'order/ordenCreada.html', {'order': order})
    return HttpResponseRedirect(reverse("home"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["cart"] = Cart(self.request)
    return context

