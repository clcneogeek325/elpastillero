from django import forms
from apps.pc.models import Pc

class pcForm(forms.ModelForm):
	nombre_pc = forms.CharField(label="Nombre Del La Computadora")
	class Meta:
		model = Pc
		exclude = {'status',}
