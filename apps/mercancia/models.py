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
	precio_sugerido = models.FloatField()
	precio_farmacia = models.FloatField()
	descuento_compra = models.IntegerField()
	precio_compra = models.FloatField()
	descuento_venta = models.IntegerField()
	ganancia = models.FloatField()
	precio_venta = models.FloatField()
	iva = models.IntegerField()
	factura = models.CharField(max_length=200,blank=True)
	
