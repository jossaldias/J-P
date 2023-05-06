from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=70)
    apellidos = models.CharField(max_length=70)
    correo = models.CharField(max_length=100, unique=True)
    pwd = models.CharField(max_length=100)
    pwd1 = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    fecha_nac = models.DateField()
    domicilio = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    # suscrito = models.BooleanField(default=False)