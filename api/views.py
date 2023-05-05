from cmath import log
from telnetlib import STATUS
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from .models import *
from .serializers import *

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def crearCliente(request):
    username = request.POST['nombres']
    email = request.POST['email']
    pwd = request.POST['pwd']

    Cliente.objects.create(
        nombres = username,
        apellidos = request.POST['apellidos'],
        correo = email,
        contraseña = pwd,
        fecha_nacimiento = request.POST['fec_nac'],
        telefono = request.POST['telefono'],
        domicilio = request.POST['domicilio'],
        comuna = request.POST['comuna']
    )
    return Response('Se ha registrado con exito.')