from django import forms
from django.contrib.auth.models import User

from MusicEngineApp.models import Tecnico, Reserva, Sala, Material, Tiquet, ConversacionTiquet


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
        fields = ['fecha', 'hora_inicio', 'hora_fin', 'tecnico', 'material', 'sala', 'nombre_cliente', 'DNI',
                  'telefono']


class TiquetForm(forms.ModelForm):
    assunto = forms.CharField(
        label='Assunto',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Assunto'
        })
    )

    descripcion = forms.CharField(
        label='Descripció',
        widget=forms.Textarea(attrs={
            'class': 'form-control input',
            'placeholder': 'descripció'
        })
    )

    usuario = forms.ModelChoiceField(
        required=True,
        queryset=User.objects.all(),
        label="Material",
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Tiquet
        fields = ['id', 'assunto', 'descripcion', 'usuario']


class ConversacionTiquetForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        required=False,
        queryset=User.objects.all(),
        label="Usuari",
        widget=forms.HiddenInput()
    )

    tiquet = forms.ModelChoiceField(
        required=False,
        queryset=Tiquet.objects.all(),
        label="Tiquet",
        widget=forms.HiddenInput()
    )

    mensaje = forms.CharField(
        label='Missatge',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'missatge'
        })
    )

    class Meta:
        model = ConversacionTiquet
        fields = ['id', 'tiquet', 'mensaje', 'usuario']
