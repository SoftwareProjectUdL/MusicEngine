from django import forms
from django.forms import inlineformset_factory

from MusicEngineApp.backoffice.models import Tecnico, Reserva, Sala, Material


class ReservaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Fecha",
                "class": "form-control",
                "type": "date"
            }
        )
    )

    hora_inicio = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "placeholder": "Hora inici",
                "class": "form-control",
                "type": "time"
            }
        )
    )

    hora_fin = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "placeholder": "Hora final",
                "class": "form-control",
                "type": "time"
            }
        )
    )

    tecnico = forms.ModelChoiceField(
        required=True,
        queryset=Tecnico.objects.all(),
        label="Tecnico",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    sala = forms.ModelChoiceField(
        required=True,
        queryset=Sala.objects.all(),
        label="Sala",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    material = forms.ModelChoiceField(
        required=True,
        queryset=Material.objects.all(),
        label="Material",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    nombre_cliente = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )

    DNI = forms.CharField(
        required=False,
    )

    telefono = forms.CharField(
        required=False,
    )

    class Meta:
        model = Reserva
        fields = ['fecha', 'hora_inicio', 'hora_fin', 'tecnico', 'material', 'sala', 'nombre_cliente', 'DNI', 'telefono']
