function editarProducto(id, id_producto, nombre, descripcion, costo, cantidad) {
    document.getElementById("id_producto_editar").value = id;
    document.getElementById("producto_editar").value = id_producto;
    document.getElementById("nombre_editar").value = nombre;
    document.getElementById("descripcion_editar").value = descripcion;
    document.getElementById("costo_editar").value = costo;
    document.getElementById("cantidad_editar").value = cantidad;
}


function eliminarProducto(id) {
    document.getElementById("id_producto_eliminar").value = id;
}





