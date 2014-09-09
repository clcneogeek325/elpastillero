from django import forms
from apps.Personal.models import Personal
from django.contrib.auth.models import User


class addPersonalForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		from apps.pc.models import Pc
		super(addPersonalForm, self).__init__(*args, **kwargs)
		self.fields['pc'] = forms.ModelChoiceField(queryset=Pc.objects.filter(status=True))

	class Meta:
		model = Personal
		exclude = {'status','user'}

class UserForm(forms.Form):
	user = forms.CharField(label="Nombre Usuario",widget=forms.TextInput())
	password = forms.CharField(label="Contrasenia ",widget=forms.PasswordInput())
	
	def clean_user(self):
		user = self.cleaned_data['user']
		try:
			u = User.objects.get(username=user)
		except User.DoesNotExist:
			return user
		raise forms.ValidationError('Lamentamos informarle que el usario ya exciste')
		
	
class ChangePasswdForm(forms.Form):
	password = forms.CharField(label="Escribe la nueva Contrasenia",widget=forms.PasswordInput())
	
