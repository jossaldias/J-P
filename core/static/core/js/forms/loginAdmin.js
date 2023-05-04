$(document).ready(function () {
    $('#error').hide()

    $('#login').submit(function (event) {
        event.preventDefault()

        let username = $('#user').val()
        let password = $('#pwd').val()

        let mensaje_error = ''
        if (username === '') {
            mensaje_error += 'Debe ingresar un nombre de usuario.<br>'
        }
        if (password === '') {
            mensaje_error += 'Debe ingresar una contraseña.'
        }

        if (mensaje_error === '') {
            var data = new FormData(this)

            var action = function (d) {
                $('#error').show();
                $('#error').html(d)
            }

            $.ajax({
                url: 'http://127.0.0.1:8000/paginas/loginAdmin',
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
    })
})