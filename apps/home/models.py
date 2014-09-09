from django.db import models

class Farmacia(models.Model):
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(blank=True, max_length=200)
	telefono = models.CharField(blank=True, max_length=200)
	status = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.nombre
