from django import forms
from apps.Personal.models import Personal



class addPersonalForm(forms.ModelForm):
	class Meta:
		model = Personal
		exclude = {'status',}



