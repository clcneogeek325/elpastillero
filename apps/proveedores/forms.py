from django import forms
from apps.proveedores.models import  Proveedores


class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedores
		exclude = {'status',}

#	nombre = forms.CharField(max_length=200)
#	apellidoPaterno = forms.CharField( max_length=200)
#	apellidoMaterno = forms.CharField( max_length=200)
#	compania = forms.CharField(max_length=200)
#	telefono = forms.CharField(max_length=200)
#	email = forms.EmailField()
#	
