from rest_framework import serializers
from .models import *

# class ProductoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Producto
#         fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'