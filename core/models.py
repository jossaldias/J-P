from datetime import date
from django.db import models

# Create your models here.


class Accesorio(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    descripcion = models.TextField(max_length=250)
    precio = models.IntegerField(default=1000)
    imagen = models.CharField(max_length=250)


class LogIn(models.Model):
    correo = models.EmailField(blank=True, primary_key=True)
    contraseña = models.CharField(max_length=8)


class LoginAdmin(models.Model):
    correo = models.EmailField(blank=True, primary_key=True)
    contraseña = models.CharField(max_length=8)


class formRegistro(models.Model):
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    correo = models.EmailField(blank=True, primary_key=True)
    telefono = models.IntegerField(default=1000)
    fecha_nac = models.DateField(auto_now_add=True)
    domicilio = models.CharField(max_length=80)
    comuna = models.CharField(max_length=80)
    pwd = models.CharField(max_length=8)
    pwd1 = models.CharField(max_length=8)


class Contacto(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    correo = models.EmailField(blank=True, primary_key=True)
    telefono = models.IntegerField(default=1000)
    mesnsaje = models.TextField(max_length=250)
