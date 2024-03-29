from django import forms
from django.forms import inlineformset_factory

from MusicEngineApp.models import Tecnico, HorarioTecnico, Material, Reserva, Sala, Factura, LineaFactura


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
        labels = {'estado': 'Estado actual'}
        fields = ['nombre', 'descripcion', 'estado', 'cantidad']

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)


class ReservaForm(forms.ModelForm):
    estado = forms.ChoiceField(
        label="Estado",
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
        choices=Reserva.Estado.choices
    )

    nombre_cliente = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Nombre cliente'
        })
    )

    DNI = forms.CharField(
        required=False,
        label='DNI',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'DNI'
        })
    )

    telefono = forms.CharField(
        required=False,
        label='Telefono',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Telefono'
        })
    )

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
                "placeholder": "Hora inicio",
                "class": "form-control",
                "type": "time"
            }
        )
    )

    hora_fin = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "placeholder": "Hora fin",
                "class": "form-control",
                "type": "time"
            }
        )
    )

    material = forms.ModelChoiceField(
        required=False,
        queryset=Material.objects.all(),
        label="Material",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    tecnico = forms.ModelChoiceField(
        required=False,
        queryset=Tecnico.objects.all(),
        label="Tecnico",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    sala = forms.ModelChoiceField(
        required=False,
        queryset=Sala.objects.all(),
        label="Sala",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'DNI', 'telefono', 'fecha', 'hora_inicio', 'hora_fin', 'material',
                  'tecnico', 'sala', 'id', 'estado']

    def save(self, commit=True):
        return super().save(commit)


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre', 'descripcion']


class LineaFacturaForm(forms.ModelForm):
    concepto = forms.CharField(
        label='Concepto',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Concepto'
        })
    )
    cantidad = forms.IntegerField(
        label='Cantidad',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Cantidad'
        })
    )
    precio = forms.DecimalField(
        label='Preu',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Preu'
        })
    )

    class Meta:
        model = LineaFactura
        fields = ['concepto', 'precio', 'cantidad']


linia_factura_formset = inlineformset_factory(
    Factura, LineaFactura,
    form=LineaFacturaForm,
    extra=0,
    min_num=1,
    can_delete=True,
)


class FacturaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Fecha",
                "class": "form-control",
                "type": "date"
            }
        )
    )

    total = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Total",
                "class": "form-control",
                "id": "total"
            }
        )
    )

    reserva = forms.ModelChoiceField(
        required=False,
        queryset=Reserva.objects.all(),
        label="Reservas",
        widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'fillFields(this)'})
    )

    nombre_cliente = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre",
                "class": "form-control nombre_cliente"
            }
        ))

    dni = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "DNI",
                "class": "form-control dni"
            }
        ))

    class Meta:
        model = Factura
        fields = ['reserva', 'fecha', 'total', 'nombre_cliente', 'dni']
