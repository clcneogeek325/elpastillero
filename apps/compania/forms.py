from django import forms
from apps.compania.models import Compania

class CompaniaForm(forms.ModelForm):
	class Meta:
		model = Compania
		exclude = {'status',}
