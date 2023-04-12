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
    class Meta:
        model = Material
        fields = ['nombre', 'descripcion']


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