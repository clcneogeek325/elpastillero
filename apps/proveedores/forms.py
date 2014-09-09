from django import forms
from apps.proveedores.models import  Proveedores
from apps.compania.models import Compania

class ProveedorForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		from apps.compania.models import Compania
		super(ProveedorForm, self).__init__(*args, **kwargs)
		self.fields['compania'] = forms.ModelChoiceField(queryset=Compania.objects.filter(status=True))
	class Meta:
		model = Proveedores
		exclude = {'status',}

