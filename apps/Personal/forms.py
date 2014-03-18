from django import forms
from apps.Personal.models import Personal



class addPersonalForm(forms.ModelForm):
	class Meta:
		model = Personal
		exclude = {'status','user'}

class UserForm(forms.Form):
	user = forms.CharField(label="Nombre Usuario",widget=forms.TextInput())
	password = forms.CharField(label="Contrasenia ",widget=forms.PasswordInput())
	

