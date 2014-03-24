from django import forms
from apps.productos.models import Producto,productoSinCodigo
from apps.categoria.models import Categoria

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = {'status','precio_compra','precio_venta','total_piezas',}


class ProductoFormCompleto(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = {'status',}

class GetCodigoProductoForm(forms.Form):
	codigo = forms.CharField()
	
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	passwd = forms.CharField(widget=forms.PasswordInput(render_value=False))
	
class productoSinCodigoForm(forms.ModelForm):
	class Meta:
		model = productoSinCodigo
		exclude = {'status',}
		
