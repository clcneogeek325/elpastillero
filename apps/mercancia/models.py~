from django.db import models
from apps.productos.models import Producto
from apps.Personal.models import Personal
from apps.proveedores.models import Proveedores
import datetime
from apps.categoria.models import Categoria
from apps.compania.models import Compania


class Mercancia(models.Model):
	producto = models.ForeignKey(Producto)
	personal = models.ForeignKey(Personal)
	proveedor = models.ForeignKey(Proveedores)
	categoria = models.ForeignKey(Categoria)
	compania = models.ForeignKey(Compania)
	piezas_compra = models.IntegerField()
	fecha_caducidad  = models.DateField()
	fecha_ingreso = models.DateTimeField(default=datetime.datetime.now)
	precio_sugerido = models.FloatField(blank=True,null=True)
	precio_farmacia = models.FloatField(blank=True,null=True)
	descuento_compra = models.IntegerField(blank=True,null=True)
	precio_compra = models.FloatField()
	descuento_venta = models.IntegerField(blank=True,null=True)
	ganancia = models.FloatField(blank=True,null=True)
	precio_venta = models.FloatField()
	iva = models.IntegerField(blank=True,null=True)
	factura = models.CharField(max_length=200,blank=True,null=True)
	
