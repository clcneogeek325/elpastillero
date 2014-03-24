from django import forms
from apps.mercancia.models import Mercancia

class MercanciaForm(forms.ModelForm):
	class Meta:
		model = Mercancia
		exclude = {'producto',
					'personal',
					'categoria',}
					
class MercanciaSuperForm(forms.ModelForm):
	class Meta:
		model = Mercancia
		exclude = {'producto',
					'personal',
					'categoria',
					'precio_sugerido',
					'precio_farmacia',
					'descuento_compra',
					'descuento_venta',
					'ganancia',
					}
					
