from django import forms

from MusicEngineApp.backoffice.models import Tecnico, HorarioTecnico, Material


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
