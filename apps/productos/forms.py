from django import forms
from apps.productos.models import Producto


class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = {'status','precio_compra','precio_venta'}
		

class GetCodigoProductoForm(forms.Form):
	codigo = forms.CharField()
	
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	passwd = forms.CharField(widget=forms.PasswordInput(render_value=False))
	

