from django.contrib import admin
from apps.productos.models import Producto,Categoria,Compania

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Compania)
