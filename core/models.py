from django.db import models

# Create your models here.


class Accesorio(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=250)
