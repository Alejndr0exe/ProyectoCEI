from django import forms 
from .models import Script, Data, Manual

class addScript(forms.ModelForm):
	class Meta:
		model = Script
		fields = ('documento','descripcion')
		
class addData(forms.ModelForm):
	class Meta:
		model = Data
		fields = ('documento','descripcion')

class addManual(forms.ModelForm):
	class Meta:
		model = Manual
		fields = ('documento','descripcion')
