from django.urls import path
from .views import *

urlpatterns = [
    # INICIO
    path("", home, name="home"),

    # PAGINAS
    path('paginas/juegos', juegos, name="juegos"),
    path('paginas/accesorios', accesorios, name="accesorios"),
    path('paginas/contacto', contacto, name="contacto"),
    path('paginas/login', login, name="login"),
    path('paginas/loginAdmin', loginAdmin, name="loginAdmin"),
    path('paginas/registro', registro, name="registro"),
    path('paginas/carritoCompras', carritoCompras, name="carritoCompras"),
    path('paginas/agregarProducto', agregarProducto, name="agregarProducto"),
    path('paginas/accionAventura', accionAventura, name="accionAventura"),
    path('paginas/arcadeSimulacion', arcadeSimulacion, name="arcadeSimulacion"),
    path('paginas/deportesMusica', deportesMusica, name="deportesMusica"),
    path('paginas/shooterEstrategia', shooterEstrategia, name="shooterEstrategia"),
]
