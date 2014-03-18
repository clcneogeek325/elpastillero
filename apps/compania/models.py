from django.db import models

class Compania(models.Model):
	nombre_compania = models.CharField(blank=True, max_length=200)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre_compania
		

