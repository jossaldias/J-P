from django.urls import path

from .views import *

urlpatterns = [
    # path('obtenerProductos/', obtenerProductos),
    # path('crearProducto/', crearProducto),
    # path('editarProducto/<p_id>', editarProducto),
    # path('eliminarProducto/<p_id>', eliminarProducto),
    # path('buscarProducto/<nombre>', buscarProducto),
    # path('obtenerProductosDescuento/', obtenerProductosDescuento),

    # path('obtenerClientes/', obtenerClientes),
    path('crearCliente', crearCliente),
    # path('editarCliente/<p_id>', editarCliente),
    # path('eliminarCliente/<p_id>', eliminarCliente),

    # path('registroAdmin/', crearAdmin),
    path('login', login),
]