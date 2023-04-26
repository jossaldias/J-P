from django.urls import path
from .views import accesorios, home, juegos

urlpatterns = [
    # INICIO
    path("", home, name="home"),

    # PAGINAS
    path('paginas/juegos', juegos, name="juegos"),
    path('paginas/accesorios', accesorios, name="accesorios"),
]
