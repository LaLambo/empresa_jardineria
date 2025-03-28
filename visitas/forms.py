from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['cliente', 'direccion', 'tipo_servicio', 'disponibilidad', 'fecha', 'estado','metros_cuadrados']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'cliente': 'Cliente',
            'direccion': 'Dirección',
            'tipo_servicio': 'Tipo de Servicio',
            'disponibilidad': 'Disponibilidad',
            'fecha': 'Fecha',
            'estado': 'Estado',
            'metros_cuadrados': 'Metros Cuadrados'
        }