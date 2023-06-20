import os
import requests
import time

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.db.models import F

from .cart import Cart
from .provider import Provider
from .models import *
from .forms import *


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
def codigos(request):
    codigos = Codigo.objects.all()
    context = {
        'codigos': codigos,
    
    }
  
    return render(request, 'paginas/productos/codigos.html', context)

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
            producto = item["producto"]
            costo = item["costo"]
            cantidad = item["cantidad"]

            Item.objects.create(
            orden=order,
            producto=item["producto"],
            costo=item["costo"],
            cantidad=item["cantidad"],
            )
            Producto.objects.filter(id=producto.id).update(cantidad=F('cantidad') - cantidad)

      cart.clear()
      return render(self.request, 'order/ordenCreada.html', {'order': order})
    return HttpResponseRedirect(reverse("home"))
  
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["cart"] = Cart(self.request)
    return context  

@login_required
def pedidoListo(request):
    
    return render(request, 'paginas/productos/pedidoListo.html')
# CONTACTO FORM

def contacto(request):
    return render(request, 'paginas/informacion/contacto.html')


#MIS COMPRAS
@login_required
def misOrdenes(request):
    ordenes = Order.objects.filter(user=request.user)
    print(ordenes)
    return render(request, 'paginas/productos/misOrdenes.html',  {'ordenes': ordenes} )

#ORDENES DE COMPRA
@login_required
def ordenesCompra(request):
    orders = Orden.objects.all()
    form_editar = editarOrdenForm()

    context = {
        'orders': orders,
        "form_editar": form_editar
    }
  
    return render(request, 'ordencompra/ordenes.html',context)

def crearOrden (request):
    productos = Producto.objects.all()
    provider = Provider(request)

    context = {
        'productos': productos,
        "provider": provider
    }
    extra_context = {"form": ProviderAddProductoForm()}
    return render(request, 'ordenCompra/crearOrden.html',context)

def provider_add(request, producto_id):

  provider = Provider(request)
  producto = get_object_or_404(Producto, id=producto_id)

  form = ProviderAddProductoForm(request.POST)
  if form.is_valid():
    provider_add = form.cleaned_data
    provider.add(
      producto=producto,
      cantidad=provider_add["cantidad"],
      override_cantidad=provider_add["override"]
    )
    return HttpResponseRedirect(reverse("crearOrden"))

def provider_eliminar(request, producto_id):

  provider = Provider(request)
  producto = get_object_or_404(Producto, id=producto_id)
  provider.remove(producto)
  return redirect("crearOrden")

def provider_clear(request):
  provider = Provider(request)
  provider.clear()
  return redirect("crearOrden")

class ProviderCreateView(CreateView):
  model = Orden
  form_class = OrdenCreateForm
  template_name="ordencompra/provider_form.html"

  def form_valid(self, form):
    provider = Provider(self.request)
    if provider:
      orden = form.save(commit=False)
      orden.user = self.request.user
      orden.is_pagado = True
      orden.save()
      for itemprovider in provider:
          ItemProvider.objects.create(
          orden=orden,
          producto=itemprovider["producto"],
          costo=itemprovider["costo"],
          cantidad=itemprovider["cantidad"],
        )
      provider.clear()
      return render(self.request, 'ordencompra/ordenEnviada.html', {'orden': orden})
    return HttpResponseRedirect(reverse("home"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["provider"] = Provider(self.request)
    return context


@login_required
def ordenEnviada(request):
    
    return render(request, 'ordencompra/ordenEnviada.html')

########

@login_required
def editarOrden(request):
    if request.method == 'POST':
        orden = get_object_or_404(Orden, pk=request.POST.get('id_compra_editar'))
        form_editar = editarOrdenForm(data=request.POST, files=request.FILES, instance=orden)
        if form_editar.is_valid():
            form_editar.save()
        return redirect('ordenes')
    else:
        form_editar = editarOrdenForm()
        context = {
            'form_editar': form_editar
        }
    return render(request, 'paginas/productos/ordenes.html', context)

@login_required
def editarEnvio(request):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=request.POST.get('id_envio_editar'))
        form_editar = editarEnvioForm(data=request.POST, files=request.FILES, instance=order)
        if form_editar.is_valid():
            form_editar.save()
        return redirect('compras')
    else:
        form_editar = editarEnvioForm()
        context = {
            'form_editar': form_editar
        }
    return render(request, 'paginas/productos/compras.html', context)


@login_required
def eliminarOrden(request):
    if request.POST:
        compras = Compra.objects.get(pk=request.POST.get('id_compra_eliminar'))
        compras.delete()    
  
    return redirect('ordenes')


######



# PRODUCTOS

def juegos(request):
    
    productos = Producto.objects.filter(
                                        Q(tipo_producto='Juego Físico')|
                                        Q(tipo_producto='Código Digital')
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

# COMPRAS

@login_required
def compras(request):
   ordenes = Order.objects.all()
   form_editar = editarEnvioForm()

   context = {
        'ordenes': ordenes,
        "form_editar": form_editar
   }
  
  
   return render(request, 'paginas/productos/compras.html', context)


