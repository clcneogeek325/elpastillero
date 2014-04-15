from django import forms
from datetime import datetime

from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import DateInput
class getMejorProveedor(forms.Form):
	codigo = forms.CharField(label="Codigo del Producto")
	
class getFechaForm(forms.Form):
	fecha = forms.DateField()
	
class getRangoFechaForm(forms.Form):
	fechauno = forms.DateField(label="Fecha 1",
			widget=DateInput(attrs = {'class': 'vDateField', 'size': '50','name':'fechauno'}))
	fechados = forms.DateField(label="fecha 2",
			widget=DateInput(attrs = {'class': 'vDateField', 'size': '20','name':'fechados'}))
	
class getCampoForm(forms.Form):
	TOPIC_CHOICES = (
    ('fecha', 'Solo por la fecha'),
    ('factura', 'Buscar Por Factura'),
    ('categoria', 'Por Categoria'),
    ('compania', 'Por Compania'),
    )
	campo = forms.ChoiceField(choices=TOPIC_CHOICES)
	busqueda = forms.CharField(required=False)
			
			
			
			

