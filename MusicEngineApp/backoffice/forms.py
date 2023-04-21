from django import forms

from MusicEngineApp.backoffice.models import Tecnico, HorarioTecnico, Material, Reserva, Sala


class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'descripcion', 'telefono']


class HorarioTecnicoForm(forms.ModelForm):
    class Meta:
        model = HorarioTecnico
        fields = ['fecha', 'hora_inicio', 'hora_fin', 'tecnico']


class MaterialForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre",
                "class": "form-control"
            }
        ))

    descripcion = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Descripcion",
                "class": "form-control"
            }
        )
    )

    estado = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
        choices=Material.Estado.choices
    )

    cantidad = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Cantidad",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Material
        labels = { 'estado': 'Estado actual' }
        fields = ['nombre', 'descripcion', 'estado', 'cantidad']

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'DNI', 'telefono', 'fecha', 'hora_inicio', 'hora_fin', 'material',
                  'tecnico', 'sala', 'id']

    def save(self, commit=True):
        return super().save(commit)


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre', 'descripcion']
