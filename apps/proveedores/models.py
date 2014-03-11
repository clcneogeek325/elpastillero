from django.db import models


class Proveedores(models.Model):
	"""Agregando proveedores"""
	nombre = models.CharField(max_length=200)
	apellidoPaterno = models.CharField(max_length=200)
	apellidoMaterno = models.CharField(max_length=200)
	compania = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200)
	email = models.EmailField()
	status = models.BooleanField(default=True)
	
	def __unicode__(self):
		nombbreCompleto = "%s %s %s" % (self.nombre,self.apellidoPaterno,self.apellidoMaterno)
		return nombbreCompleto

