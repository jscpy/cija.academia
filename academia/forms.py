from django import forms
from models import Comentario

class ComentarioForm(forms.ModelForm):
	usuario = forms.CharField(
		max_length = 30, 
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Escribe tu nombre'
			})
		)
	
	comentario = forms.CharField(
		widget = forms.Textarea(
			attrs = {
				'class' : 'form-control',
				'rows': '4'
			})
		)

	class Meta:
		model = Comentario
		exclude = ["post"]
