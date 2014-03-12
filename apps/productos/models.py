from django.db import models
from apps.proveedores.models import Proveedores


class Compania(models.Model):
	nombre_compania = models.CharField(blank=True, max_length=200)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre_compania
		
class Categoria(models.Model):
	nombre_categoria = models.CharField(blank=True, max_length=200)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre_categoria

class Producto(models.Model):
	codigo = models.CharField(max_length=200)
	nombre_producto = models.CharField(max_length=200)
	categoria = models.ManyToManyField(Categoria,blank=True,null=True)
	nombre_compania = models.ManyToManyField(Compania,blank=True,null=True)
	nombre_proveedor = models.ManyToManyField(Proveedores,blank=True,null=True)
	total_piezas = models.IntegerField(default=0)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre_producto
		