from django import forms
from apps.proveedores.models import  Proveedores


class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedores
		exclude = {'status',}

