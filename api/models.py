from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    correo = models.EmailField(blank=True, primary_key=True)
    telefono = models.IntegerField(default=1000)
    fecha_nac = models.DateField(auto_now_add=True)
    domicilio = models.CharField(max_length=80)
    comuna = models.CharField(max_length=80)
    pwd = models.CharField(max_length=8)
    pwd1 = models.CharField(max_length=8)