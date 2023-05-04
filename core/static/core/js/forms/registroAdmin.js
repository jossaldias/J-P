$(document).ready(function () {
    $('#error').hide()

    $('#formRegistro').submit(function (event) {
        event.preventDefault()

        let username = $('#username').val()
        let email = $('#email').val()
        let password = $('#pwd').val()
        let password1 = $('#pwd1').val()

        let mensaje_error = ''
        if (username === '') {
            mensaje_error += 'Debe ingresar su nombre.<br>'
        }
        if (email === '') {
            mensaje_error += 'Debe ingresar un correo electronico.<br>'
        }
        if (password === '') {
            mensaje_error += 'Debe ingresar una contraseña valida.<br>'
        }
        else if (password != password1) {
            mensaje_error += 'Las contraseñas no coinciden.<br>'
        }

        if (mensaje_error === '') {
            var data = new FormData(this)
            var action = function (d) {
                console.log(d);
            }

            $.ajax({
                url: 'http://127.0.0.1:8000/api/registroAdmin/',
                data: data,
                type: 'POST',
                contentType: false,
                processData: false,
                success: action,
                error: action,
            })

            $('#error').show()
            $('#error').html('Usuario creado con exito.')
        }
        else {
            $('#error').show()
            $('#error').html(mensaje_error)
        }

    })

})