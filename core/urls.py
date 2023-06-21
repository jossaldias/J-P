from django.urls import path
from django.contrib.auth.decorators import login_required


from . import views

urlpatterns = [
    # INICIO
    path("", views.home, name="home"),
    path("logout/", views.exit, name="exit"),    
    path('registration/register', views.register, name="register"),

    # PAGINAS
   
    path('paginas/perfil', views.perfil, name="perfil"),
    path('paginas/editarPerfil', views.editarPerfil, name="editarPerfil"),
    path('paginas/misOrdenes', views.misOrdenes, name="misOrdenes"),

    path('paginas/usuarios', views.usuarios, name="usuarios"),    
    path('paginas/agregarUsuario', views.agregarUsuario, name="agregarUsuario"),
    path('paginas/eliminarUsuario', views.eliminarUsuario, name="eliminarUsuario"),
    path('paginas/editarUsuario', views.editarUsuario, name="editarUsuario"),

    path('paginas/accesorios', views.accesorios, name="accesorios"),
    path('paginas/contacto', views.contacto, name="contacto"),

    path('paginas/ordenes', views.ordenesCompra, name="ordenes"),    
    path('paginas/crearOrden', login_required(views.crearOrden), name="crearOrden"),
    path("addoc/<int:producto_id>/", views.provider_add, name="addoc"),
    path("eliminaroc/<int:producto_id>/", views.provider_eliminar, name="eliminaroc"),
    path("verOrden/<int:id>/", views.verOrden, name="verOrden"),
    path("clearoc/", views.provider_clear, name="clearoc"),
    path("crear-orden/",login_required(views.ProviderCreateView.as_view()), name="crear-orden"),
    path('paginas/ordenEnviada', views.ordenEnviada, name="ordenEnviada"),



    path('paginas/editarOrden', views.editarOrden, name="editarOrden"),
    path('paginas/editarEnvio', views.editarEnvio, name="editarEnvio"),

    
    path('paginas/carritoCompras', views.cart_detalle, name="carritoCompras"),
    path("add/<int:producto_id>/", views.cart_add, name="add"),
    path("eliminar/<int:producto_id>/", views.cart_eliminar, name="eliminar"),
    path("clear/", views.cart_clear, name="clear"),
    path('paginas/pedidoListo', views.pedidoListo, name="pedidoListo"),

    path("create-order/",login_required(views.OrderCreateView.as_view()), name="create-order"),


    path('paginas/inventario', views.inventarioProducto, name="inventario"),
    path('codigos/<int:producto_id>/', views.codigos, name='codigos'),
    path('paginas/compras', views.compras, name="compras"),
    path('paginas/agregarProducto', views.agregarProducto, name="agregarProducto"),
    path('paginas/editarProducto', views.editarProducto, name="editarProducto"),
    path('paginas/eliminarProducto', views.eliminarProducto, name="eliminarProducto"),

    path('paginas/juegos', views.juegos, name="juegos"), 
    path('paginas/accionAventura', views.accionAventura, name="accionAventura"),
    path('paginas/arcadeSimulacion', views.arcadeSimulacion, name="arcadeSimulacion"),
    path('paginas/deportesMusica', views.deportesMusica, name="deportesMusica"),
    path('paginas/shooterEstrategia', views.shooterEstrategia, name="shooterEstrategia"),
]
