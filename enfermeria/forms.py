from django import forms
from models import Medicamento

class MedicamentoForm(forms.ModelForm):
	concepto = forms.CharField(
		label = 'Concepto',
		widget = forms.TextInput(
			attrs = {
				'class' : 'form-control',
				'placeholder' : 'Paracetamol',
				'onkeyup' : 'this.value = this.value.toUpperCase()'
			})
	)

	lista_presentaciones = (
		('TABLETAS', 'Tabletas'),
		('TABLETAS RECUBIERTAS', 'Tabletas Recubiertas'),
		('SUSPENSION', 'Suspension'),
		('SUSPENSION AEROSOL', 'Suspension Aerosol'),
		('GRAGEAS', 'Grageas'),
		('CAPSULAS', 'Capsulas'),
		('COMPRIMIDOS', 'Comprimidos'),
		('CREMA', 'Crema'),
		('FRASCO', 'Frasco'),
		('SOL. INYECTABLE', 'Solucion Inyectable'),
		('PIEZA', 'Pieza')
	)

	presentacion = forms.ChoiceField(
		label = 'Presentacion',
		choices = lista_presentaciones,
		widget = forms.Select(
			attrs = {
				'class' : 'form-control',
			}
		)
	)

	unidad_medida = forms.CharField(
		label = 'Unidad de Medida',
		widget = forms.TextInput(
			attrs = {
				'class' : 'form-control',
				'placeholder' : '100 GRAMOS',
				'onkeyup' : 'this.value = this.value.toUpperCase()'
			})
	)

	lote = forms.CharField(
		label = 'Lote',
		widget = forms.TextInput(
			attrs = {
				'class' : 'form-control',
				'placeholder' : 'AB1005',
				'onkeyup' : 'this.value = this.value.toUpperCase()'
			})
	)

	cantidad = forms.CharField(
		label = 'Cantidad',
		widget = forms.TextInput(
			attrs = {
				'class' : 'form-control',
				'placeholder' : '100'
			})
	)

	fecha_caducidad = forms.DateField(
		label = 'Fecha de Caducidad',
		widget = forms.TextInput(
			attrs = {
				'class' : 'form-control',
				'placeholder' : '2015/01/01'
			})
	)

	class Meta:
		model = Medicamento
		exclude = ["fecha_ingreso"]
