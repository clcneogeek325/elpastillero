from django import forms
from apps.productos.models import Producto,productoSinCodigo
from apps.categoria.models import Categoria

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = {'status','precio_compra','precio_venta','total_piezas','tiene_codigo',}


class ProductoFormCompleto(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = {'status','tiene_codigo',}


class ProductoCompletoSinCodForm(forms.ModelForm):
	total_piezas = forms.IntegerField(label="Numero de piezas")
	class Meta:
		model = Producto
		exclude = {'status','tiene_codigo',}

class GetCodigoProductoForm(forms.Form):
	codigo = forms.CharField()
	
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Escribe el nombre de usuario'}))
	passwd = forms.CharField(widget=forms.PasswordInput(render_value=False,attrs={'class': 'form-control','placeholder':'Escribe el tu contrasenia'}))
	
class productoSinCodigoForm(forms.ModelForm):
	class Meta:
		model = productoSinCodigo
		exclude = {'status','tiene_codigo',}
		
