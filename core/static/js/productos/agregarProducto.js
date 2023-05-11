$(document).ready(function () {
    $('#error').hide()

    $('#formAgregar').submit(function (event) {
        let nombre = $('#nombre').val()
        let descripcion = $('#descripcion').val()
        let categoria = $('#categoria').val()
        let precio = $('#precio').val()
        let stock = $('#stock').val()
        let imagen = $('#imagen').val()

        let mensaje_error = ''
        if (nombre === '') {
            mensaje_error += 'Debes ingresar el nombre del producto.<br>'
        }
        if (descripcion === '') {
            mensaje_error += 'Debe ingresar la descripcion del producto.<br>'
        }
        if (categoria === '') {
            mensaje_error += 'Debe indicar la categoria del producto.<br>'
        }
        if (precio < 0 || precio === '') {
            mensaje_error += 'El valor del producto debe ser mayor a 0.<br>'
        }
        if (stock < 0 || stock === '') {
            mensaje_error += 'El stock del producto debe ser mayor a 0.<br>'
        }
        if (imagen === '') {
            mensaje_error += 'Debe ingresar una imagen para el producto.'
        }

        if (mensaje_error === '') {
            var data = new FormData(this)
            var action = function (d) {
                console.log(d);
            }

            $.ajax({
                url: 'http://127.0.0.1:8000/paginas/pageTest',
                data: data,
                type: 'POST',
                contentType: false,
                processData: false,
                success: action,
                error: action,
            })
        }
        else {
            event.preventDefault()
            $('#error').show()
            $('#error').html(mensaje_error)
        }
        event.preventDefault()
    })
})