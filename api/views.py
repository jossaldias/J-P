from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import *
from .serializers import *

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def crearCliente(request):
   
    Cliente.objects.create(
        nombres = request.POST['nombres'],
        apellidos = request.POST['apellidos'],
        correo = request.POST['correo'],
        pwd = request.POST['pwd'],
        pwd1 = request.POST['pwd1'],
        fecha_nac = request.POST['fecha_nac'],
        telefono = request.POST['telefono'],
        domicilio = request.POST['domicilio'],
        comuna = request.POST['comuna']
        
    )
    return Response('Se ha registrado con exito.')



@csrf_exempt
@api_view(['POST'])
def login(request):
    correo = request.POST['correo']
    password = request.POST['pwd']

    if(Cliente.objects.get(correo==correo)):

       return Response('Usuario correcto.')

    else:
       
       return Response('Usuario o contraseña incorrectos.')

    # pass_valido = check_password(password, correo.password)
    # if not pass_valido:
    #     return Response('Usuario o contraseña incorrectos.')

    # token, created = Token.objects.get_or_create(correo=correo)
    # return Response(token.key)



# @csrf_exempt
# @api_view(['GET'])
# def login(request, correo, pwd):
#     clientes = Cliente.objects.authenticate(correo=correo, pwd=pwd)
#     serializer = ClienteSerializer(clientes, many=True)
#     return Response(serializer.data)
