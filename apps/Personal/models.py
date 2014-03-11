from django.db import models

class Personal(models.Model):
	"""Agregando peesonal"""
	nombre = models.CharField(max_length=200)
	apellidoPaterno = models.CharField(max_length=200)
	apellidoMaterno = models.CharField(max_length=200)
	telefono = models.CharField(max_length=100)
	email = models.EmailField()
	status = models.BooleanField(default=True)
	
	def __unicode__(self):
		nombbreCompleto = "%s %s %s" % (self.nombre,self.apellidoPaterno,self.apellidoMaterno)
		return nombbreCompleto

