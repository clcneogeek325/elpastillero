from django.db import models

class Categoria(models.Model):
	nombre_categoria = models.CharField(blank=True, max_length=200)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre_categoria

