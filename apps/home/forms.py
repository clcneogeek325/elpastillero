from django import forms
from apps.home.models import Farmacia


class FarmaciaForm(forms.ModelForm):
	class Meta:
		model = Farmacia
		exclude = {'status',}



#	nombre = forms.CharField()
#	direccion = forms.CharField()
#	telefono = forms.CharField()
