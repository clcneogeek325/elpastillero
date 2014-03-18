from django import forms
from apps.mercancia.models import Mercancia

class MercanciaForm(forms.ModelForm):
	class Meta:
		model = Mercancia
		fields = {'proveedor',
				  'compania',
				  'fecha_caducidad',
				  'fecha_ingreso',
				  'precio_sugerido',
				  'precio_farmacia',
				  'descuento_compra',
				  'precio_compra',
				  'descuento_venta',
				  'ganancia',
				  'precio_venta',
				  'iva'}
	
	
