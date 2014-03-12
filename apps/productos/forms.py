from django import forms
from apps.productos.models import Producto



class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = {'status',}



