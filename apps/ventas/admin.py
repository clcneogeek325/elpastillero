from django.contrib import admin
from apps.ventas.models import Tabla_temporal,Venta, Productos_vendidos

admin.site.register(Tabla_temporal)
admin.site.register(Venta)
admin.site.register(Productos_vendidos)
