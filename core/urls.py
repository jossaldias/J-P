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
    path('paginas/agregarProducto', pageTest, name="agregarProducto"),
    path('paginas/accion_y_aventura', pageTest, name="accion_y_aventura"),
    path('paginas/arcade_y_simulacion', pageTest, name="arcade_y_simulacion"),
    path('paginas/deportes_y_musica', pageTest, name="deportes_y_musica"),
    path('paginas/shooter_y_estrategia', pageTest, name="shooter_y_estrategia"),
]
