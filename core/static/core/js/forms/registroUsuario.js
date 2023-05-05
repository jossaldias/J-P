$(document).ready(function () {
    $('#error').hide()

    $('#formRegistro').submit(function (event) {
        event.preventDefault()
        let nombres = $('#nombres').val()
        let apellidos = $('#apellidos').val()
        let correo = $('#correo').val()
        let telefono = $('#telefono').val()
        let fecha_nac = $('#fecha_nac').val()
        let direccion = $('#domicilio').val()
        let comuna = $('#comuna').val()
        let pwd = $('#pwd').val()
        let pwd1 = $('#pwd1').val()

        let mensaje_error = ''
        if (nombres === '') {
            mensaje_error += 'Debe ingresar su nombre.<br>'
        }
        if (apellidos === '') {
            mensaje_error += 'Debe ingresar su apellido.<br>'
        }
        if (correo === '') {
            mensaje_error += 'Debe ingresar su correo.<br>'
        }
        if (telefono === '') {
            mensaje_error += 'Debe ingresar un telefono.<br>'
        }
        if (fecha_nac === '') {
            mensaje_error += 'Debe ingresar su fecha de nacimiento.<br>'
        }
        if (direccion === '') {
            mensaje_error += 'Debe ingresar su direccion residencial.<br>'
        }
        if (comuna === '') {
            mensaje_error += 'Debe ingresar la comuna donde vive.<br>'
        }
        if (pwd === '') {
            mensaje_error += 'Debe ingresar una contraseña valida.'
        }
        else if (pwd !== pwd1) {
            mensaje_error += 'Las contraseñas no coinciden.<br>'
        }

        if (mensaje_error === '') {
            var data = new FormData(this);
            var action = function (d) {
                console.log(d);
            }

            $.ajax({
                url: 'http://127.0.0.1:8000/paginas/registro',
                data: data,
                type: 'POST',
                contentType: false,
                processData: false,
                success: action,
                error: action
            })
        }
        else {
            $('#error').show()
            $('#error').html(mensaje_error)
            event.preventDefault();
        }
    })
})
