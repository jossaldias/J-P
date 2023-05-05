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
    # username = request.POST.get['nombres']
    # email = request.POST.get['email']
    # pwd = request.POST.get['pwd']

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