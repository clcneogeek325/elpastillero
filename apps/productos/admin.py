from django.contrib import admin
from apps.productos.models import Producto,Mejor_proveedor,productoSinCodigo

admin.site.register(Producto)
admin.site.register(Mejor_proveedor)
admin.site.register(productoSinCodigo)
