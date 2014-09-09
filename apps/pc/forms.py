from django import forms
from apps.pc.models import Pc

class pcForm(forms.ModelForm):
#	nombre_pc = forms.CharField(label="Nombre Del La Computadora")
	class Meta:
		model = Pc
		exclude = {'status',}


	def __init__(self, *args, **kwargs):
		super(pcForm, self).__init__(*args, **kwargs)
		self.fields['categoria'].label = "CATEGORIA : En caso de que en esta maquina no tenga descuento, esta y el siguientecampo dejelo  en blanco"
		self.fields['nombre_pc'].label = "Nombre de la computadora"
		self.fields['descuento_medicamento_generico'].label = "Descuento en medicamento %"
