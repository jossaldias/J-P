$(document).ready(function () {
    $('#error').hide()

    $('#login').submit(function (event) {

        let correo = $('#correo').val()
        let pwd = $('#pwd').val()

        let mensaje_error = ''
        if (correo === '') {
            mensaje_error += 'Debe ingresar un correo valido.<br>'
        }
        if (pwd === '') {
            mensaje_error += 'Debe ingresar una contraseña.<br>'
        }

        if (mensaje_error === '') {
            var data = new FormData(this)
            var action = function (d) {
                $('#error').show();
                $('#error').html(d)
                window.location.href = "/paginas/juegos";
            }

            $.ajax({
                url: 'http://127.0.0.1:8000/api/login',
                data: data,
                type: 'POST',
                contentType: false,
                processData: false,
                success: action,
                error: action,
            })
        }
        else {
            $('#error').show()
            $('#error').html(mensaje_error)
        }
        event.preventDefault()

    })
})