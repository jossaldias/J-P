from django.urls import path
from .views import *

urlpatterns = [
    # INICIO
    path("", home, name="home"),
    path("logout/", exit, name="exit"),    
    # PAGINAS
    path('paginas/juegos', juegos, name="juegos"), 
    path('paginas/perfil', perfil, name="perfil"),
    path('paginas/editarPerfil', editarPerfil, name="editarPerfil"),
    path('paginas/accesorios', accesorios, name="accesorios"),
    path('paginas/contacto', contacto, name="contacto"),
    path('registration/register', register, name="register"),
    path('paginas/carritoCompras', carritoCompras, name="carritoCompras"),
    path('paginas/inventario', inventarioProducto, name="inventario"),
    path('paginas/agregarProducto', agregarProducto, name="agregarProducto"),
    path('paginas/accionAventura', accionAventura, name="accionAventura"),
    path('paginas/arcadeSimulacion', arcadeSimulacion, name="arcadeSimulacion"),
    path('paginas/deportesMusica', deportesMusica, name="deportesMusica"),
    path('paginas/shooterEstrategia', shooterEstrategia, name="shooterEstrategia"),
]
