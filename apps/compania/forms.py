from django import forms
from apps.compania.models import Compania

class CompaniaForm(forms.ModelForm):
	nombre_compania = forms.CharField(label="Nombre De La Compania")
	class Meta:
		model = Compania
		exclude = {'status',}
