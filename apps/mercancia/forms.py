from django import forms
from apps.mercancia.models import Mercancia

class MercanciaForm(forms.ModelForm):
	class Meta:
		model = Mercancia
		exclude = {'producto',
					'personal',
					'categoria',}
		widgets = {
                        'fecha_caducidad': forms.TextInput(attrs={'class':'controls input-append date form_date"','data-date':'','data-date-format':'dd/mm/yyyy','data-link-field':'dtp_input2','data-link-format':'yyyy-mm-dd'}),
        }

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
		widgets = {
                        'fecha_caducidad': forms.TextInput(attrs={'class':'controls input-append date form_date"','data-date':'','data-date-format':'dd/mm/yyyy','data-link-field':'dtp_input2','data-link-format':'yyyy-mm-dd'}),
        }
