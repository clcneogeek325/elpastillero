from django import forms
from apps.categoria.models import Categoria



class CategoriaForm(forms.ModelForm):
	nombre_categoria = forms.CharField(label="Nombre Categoria")
	class Meta:
		model = Categoria
		exclude = {'status',}
