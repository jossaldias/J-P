from django.urls import path

from . import views

urlpatterns = [
    # INICIO
    path("", views.home, name="home"),
    path("logout/", views.exit, name="exit"),    
    path('registration/register', views.register, name="register"),

    # PAGINAS
   
    path('paginas/perfil', views.perfil, name="perfil"),
    path('paginas/editarPerfil', views.editarPerfil, name="editarPerfil"),
    path('paginas/editarUsuario', views.editarUsuario, name="editarUsuario"),
    path('paginas/misOrdenes', views.misOrdenes, name="misOrdenes"),

    path('paginas/usuarios', views.usuarios, name="usuarios"),    
    path('paginas/agregarUsuario', views.agregarUsuario, name="agregarUsuario"),

    path('paginas/accesorios', views.accesorios, name="accesorios"),
    path('paginas/contacto', views.contacto, name="contacto"),

    path('paginas/ordenes', views.ordenes, name="ordenes"),    
    path('paginas/agregarOrden', views.agregarOrden, name="agregarOrden"),

    
    path('paginas/carritoCompras', views.cart_detalle, name="carritoCompras"),
    path("add/<int:producto_id>/", views.cart_add, name="add"),
    path("eliminar/<int:producto_id>/", views.cart_eliminar, name="eliminar"),
    path("clear/", views.cart_clear, name="clear"),
    
    path("create/", views.OrderCreateView.as_view(), name="create"),


    path('paginas/inventario', views.inventarioProducto, name="inventario"),
    path('paginas/agregarProducto', views.agregarProducto, name="agregarProducto"),
    path('paginas/editarProducto', views.editarProducto, name="editarProducto"),
    path('paginas/eliminarProducto', views.eliminarProducto, name="eliminarProducto"),

    path('paginas/juegos', views.juegos, name="juegos"), 
    path('paginas/accionAventura', views.accionAventura, name="accionAventura"),
    path('paginas/arcadeSimulacion', views.arcadeSimulacion, name="arcadeSimulacion"),
    path('paginas/deportesMusica', views.deportesMusica, name="deportesMusica"),
    path('paginas/shooterEstrategia', views.shooterEstrategia, name="shooterEstrategia"),
]
