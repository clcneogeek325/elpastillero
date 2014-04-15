import datetime
from django.db import models
from apps.proveedores.models import Proveedores
from apps.categoria.models import Categoria
from apps.compania.models import Compania
from apps.Personal.models import Personal
from apps.productos.models import Producto
from django.contrib.auth.models import User
from apps.pc.models import Pc



class Tabla_temporal(models.Model):
	personal = models.ForeignKey(Personal)
	producto = models.ForeignKey(Producto)
	numero_piezas = models.IntegerField(max_length=5)
	precio_compra = models.FloatField(max_length=10)
	precio_venta = models.FloatField(max_length=10)
	valor_piezas_vendidas = models.FloatField(max_length=10)
	utilidad = models.FloatField(max_length=10)
	porcentage_descuento = models.IntegerField(10)
#	pc = models.ForeignKey(Pc)

#	total_descuento_producto = models.FloatField(max_length=10)

	
	
class Venta(models.Model):
	personal = models.ForeignKey(Personal)
	fecha_venta = models.DateTimeField(default=datetime.datetime.now)
	total_venta = models.FloatField(max_length=10)
	utilidad = models.FloatField(max_length=10)

#	total_descuento_venta = models.FloatField(max_length=10)
#	pc = models.ForeignKey(Pc)


class Productos_vendidos(models.Model):
	venta = models.ForeignKey(Venta)
	fecha_venta = models.DateTimeField(default=datetime.datetime.now)
	producto = models.ForeignKey(Producto)
	precio_compra = models.FloatField(max_length=10)
	precio_venta = models.FloatField(max_length=10)
	piezas_vendias = models.IntegerField(max_length=3)
	valor_piezas_vendidas = models.FloatField(max_length=10)
	porcentage_descuento = models.IntegerField(10)
#	porcentage_descuento_producto = models.IntegerField(10)
	
