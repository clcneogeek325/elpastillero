from django import forms
from apps.categoria.models import Categoria



class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		exclude = {'status',}

