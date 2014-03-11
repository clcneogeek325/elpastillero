from django.db import models


class Proveedores(models.Model):
	"""Agregando proveedores"""
	nombre = models.CharField(max_length=200)
	apellido_Paterno = models.CharField(max_length=200)
	apellido_Materno = models.CharField(max_length=200)
	compania = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200)
	email = models.EmailField()
	status = models.BooleanField(default=True)
	
	def __unicode__(self):
		nombbreCompleto = "%s %s %s" % (self.nombre,self.apellido_Paterno,self.apellido_Materno)
		return nombbreCompleto

