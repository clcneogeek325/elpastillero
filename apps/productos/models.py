import datetime
from django.db import models
from apps.proveedores.models import Proveedores
from apps.categoria.models import Categoria
from apps.compania.models import Compania
from apps.Personal.models import Personal


class Producto(models.Model):
	codigo = models.CharField(primary_key=True,max_length=200)
	nombre_producto = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria)
	total_piezas = models.IntegerField(default=0)
	precio_compra = models.FloatField(max_length=10)
	precio_venta = models.FloatField(max_length=10)
	numero_minimo_piezas = models.IntegerField(default=0)
	status = models.BooleanField(default=True)
	tiene_codigo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre_producto
		
class Mejor_proveedor(models.Model):
	producto  = models.ForeignKey(Producto)
	proveedor = models.ForeignKey(Proveedores)
	precio = models.FloatField(max_length=10)
	def __unicode__(self):
		return self.producto.nombre_producto
		

	
class productoSinCodigo(models.Model):
	nombre_producto =models.CharField(max_length=200)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre_producto
