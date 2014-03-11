from django.db import models
from apps.proveedores.models import Proveedores

class Producto(models.Model):
	codigo = models.CharField(max_length=200)
	nombre_producto = models.CharField(max_length=200)
	nombre_compania = models.CharField(max_length=200)
	nombre_proveedor = models.ManyToManyField(Proveedores,blank=True,null=True)
	total_piezas = models.IntegerField(blank=True,null=True)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre_producto
		
