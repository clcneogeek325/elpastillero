from django import forms
from apps.Personal.models import Personal



class addPersonalForm(forms.ModelForm):
	class Meta:
		model = Personal
		exclude = {'status',}



#	"""Formulario personal"""
#	nombre = forms.CharField()
#	apellidoPaterno = forms.CharField()
#	apellidoMaterno = forms.CharField()
#	telefono = forms.CharField()
#	email = forms.EmailField()
#	
