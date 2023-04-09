from django import forms

from MusicEngineApp.backoffice.models import Tecnico

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'descripcion', 'telefono']


