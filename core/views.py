import os
import requests
import time
import random
import string


from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .utils import render_to_pdf
from django.views.generic import View
from django.db.models import Sum


from .cart import Cart
from .provider import Provider
from .models import *
from .forms import *


# Create your views here.

# HOME

def home(request):
    print(request.session.session_key)

    return render(request, 'base/home.html', {'home': home})

def buscar(request):
    query = request.GET.get('q')
    productos = Producto.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    context = {
        'productos': productos,
        'query': query
    }
    return render(request, 'paginas/catalogo/buscar.html', context)

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


def dashboard(request):
    products = Producto.objects.all() 
    product_count = products.count()

    orders = Order.objects.all()
    order_count = orders.count()

    products_sold = Item.objects.values('producto_id').annotate(total_quantity=Sum('cantidad')).order_by('-total_quantity')
    product_names = Producto.objects.filter(id__in=[product_sold['producto_id'] for product_sold in products_sold])

    products_sold_dict = {product_sold['producto_id']: {'total_quantity': product_sold['total_quantity'], 'name': product_name.nombre} for product_sold, product_name in zip(products_sold, product_names)}


    context = {
        'products': products,
        'product_count': product_count,

        'orders': orders,
        'order_count': order_count,
        'products_sold': products_sold_dict.values(),

        
    }
    return render(request, 'paginas/productos/dashboard.html', context)


class verInventario(View):

    def get(self, request, *args, **kwargs):
        productos = Producto.objects.all()
        form_editar = editarProductoForm()
        context = {
            'productos': productos,
            'form_editar':form_editar
        }
        
        pdf = render_to_pdf('paginas/productos/verInventario.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

@login_required
def codigos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    codigos = producto.codigos.all()
    context = {
        'codigos': codigos,
        'producto': producto
    }
    return render(request, 'paginas/productos/codigos.html', context)

@login_required
def agregarProducto(request):
    if request.method == 'POST':
        form = agregarProductoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            tipo_producto = form.cleaned_data['tipo_producto']
            
            if tipo_producto == 'Código Digital':
                cantidad_codigos = form.cleaned_data['cantidad']
                producto.save()


                for _ in range(cantidad_codigos):
                    codigo = generar_codigo_aleatorio()
                    Codigo.objects.create(codigo=codigo, producto_id=producto.id)
                
                producto.cantidad += cantidad_codigos
                numero_aleatorio = random.randint(10000, 99999)  
                producto.id_producto = numero_aleatorio
                producto.save()

            else:
                numero_aleatorio = random.randint(20000, 29999)  
                producto.id_producto = numero_aleatorio
                producto.save()


            return redirect('inventario')
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
  if request.method == 'POST':
        id_producto_eliminar = request.POST.get('id_producto_eliminar')
        producto = Producto.objects.get(pk=id_producto_eliminar)

        codigos = Codigo.objects.filter(producto_id=id_producto_eliminar)

        codigos.delete()

        producto.delete()

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
    template_name = "order/order_form.html"

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

                if producto.tipo_producto == "Código Digital":
                    codigos = producto.codigos.all()[:cantidad]
                    codigos_borrados = [codigo.codigo for codigo in codigos]

                    for codigo in codigos:
                        codigo.delete()

                    for codigo_borrado in codigos_borrados:
                        Item.objects.create(
                            orden=order,
                            producto=producto,
                            costo=costo,
                            cantidad=1,
                            codigo=codigo_borrado,
                        )

                Item.objects.create(
                    orden=order,
                    producto=producto,
                    costo=costo,
                    cantidad=cantidad,
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


#FACTURAS
@login_required
def factura(request):
    orders = Orden.objects.filter(estado_orden='Finalizada')
    form_editar = editarOrdenForm()

    context = {
        'orders': orders,
        "form_editar": form_editar
    }
  
    return render(request, 'ordencompra/factura.html', context)

class verFactura(View):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')  
        orders = get_object_or_404(Orden, id=id)
        nfactura = random.randint(1000, 9999)

        context = {
            'orders': orders,
            'nfactura': nfactura,
        }
    
        pdf = render_to_pdf('ordencompra/verFactura.html', context)
        return HttpResponse(pdf, content_type='application/pdf')



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



class verOrden(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        orders = get_object_or_404(Orden, id=id)

        context = {
            'orders': orders
        }

        pdf = render_to_pdf('ordencompra/verOrden.html', context)
        return HttpResponse(pdf, content_type='application/pdf')





@login_required
def codigos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    codigos = producto.codigos.all()
    context = {
        'codigos': codigos,
        'producto': producto
    }
    return render(request, 'paginas/productos/codigos.html', context)


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
            orden = form_editar.save(commit=False)
            estado_orden = form_editar.cleaned_data['estado_orden']
            orden.estado_orden = estado_orden
            numero_aleatorio = random.randint(1000, 9999)  
            orden.nfactura = numero_aleatorio

            orden.save()

            if estado_orden == 'Finalizada':
                item_providers = orden.itemproviders.all()
                for item_provider in item_providers:
                    producto = item_provider.producto
                    producto.cantidad += item_provider.cantidad
                    producto.save()

                    if producto.tipo_producto == 'Código Digital':
                        for _ in range(item_provider.cantidad):
                            codigo = generar_codigo_aleatorio()
                            Codigo.objects.create(
                                codigo=codigo,
                                _order=0,  
                                producto_id=producto.id
                            )

        return redirect('ordenes')
    else:
        form_editar = editarOrdenForm()
        context = {
            'form_editar': form_editar
        }
        return render(request, 'paginas/productos/ordenes.html', context)

def generar_codigo_aleatorio():
    letras = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(letras) for _ in range(10))
    return codigo

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
   item = Item.objects.all()
   form_editar = editarEnvioForm()

   context = {
        'ordenes': ordenes,
        'item': item,
        "form_editar": form_editar
   }
  
  
   return render(request, 'paginas/productos/compras.html', context)

class verCompras(View):

    def get(self, request, *args, **kwargs):
        ordenes = Order.objects.all()
        item = Item.objects.all()
        form_editar = editarEnvioForm()

        context = {
                'ordenes': ordenes,
                'item': item,
                "form_editar": form_editar
        }
        
        pdf = render_to_pdf('paginas/productos/verCompras.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


