from django.db import models
from apps.categoria.models import Categoria

class Pc(models.Model):
	nombre_pc = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria)
	descuento_medicamento_generico = models.IntegerField()
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre_pc
