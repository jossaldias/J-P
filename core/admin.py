#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Producto, Order ,  Item
 

# Register your models here.
admin.site.register(User)

admin.site.register(Producto)

admin.site.register(Order)

admin.site.register(Item)