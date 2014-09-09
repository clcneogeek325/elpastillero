from django import forms


class ventasForm(forms.Form):
	codigo_producto = forms.CharField(max_length=20)
	cantidad = forms.IntegerField()

class finVentaForm(forms.Form):
	total_venta = forms.CharField()
	recibi = forms.CharField()
	cambio= forms.CharField()