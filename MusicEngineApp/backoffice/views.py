from datetime import datetime

from django.contrib.auth.decorators import user_passes_test
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader

from MusicEngineApp.backoffice.forms import TecnicoForm, HorarioTecnicoForm, MaterialForm, ReservaForm, SalaForm, \
    FacturaForm, linia_factura_formset
from MusicEngineApp.backoffice.models import Reserva, Tecnico, HorarioTecnico, Material, Sala, Factura


def can_backoffice(u):
    return u.is_superuser or u.groups.filter(name__in=['gestor', 'comercial']).exists() is True


@user_passes_test(can_backoffice, login_url="/login/")
def index(request):
    context = {'segment': 'home_back'}
    html_template = loader.get_template('backoffice/index.html')
    return HttpResponse(html_template.render(context, request))


@user_passes_test(can_backoffice, login_url="/login/")
def reservas_list(request):
    reserves = Reserva.objects.all()
    return render(request, 'backoffice/reserva_list.html',
                  {'reserves': reserves, 'segment': 'reservas_list'})


@user_passes_test(can_backoffice, login_url="/login/")
def reservas_view(request, id=None):
    tecnicos = Tecnico.objects.all()
    materials = Material.objects.all()
    salas = Sala.objects.all()

    # reserva = Reserva()
    reserva_form = ReservaForm()
    if id is not None:
        # reserva = Reserva.objects.get(id=id)
        reserva_form = ReservaForm(instance=Reserva.objects.get(id=id))

    return render(request, 'backoffice/reserva_view.html',
                  {'tecnicos': tecnicos, 'materials': materials, 'salas': salas,
                   'reserva_form': reserva_form, 'segment': 'reservas_view'})


@user_passes_test(can_backoffice, login_url="/login/")
def reservas_save(request, id = None):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            if id is not None:
                form.instance.id = id
            reserva = form.save()
            return redirect('reservas_list')  # Redirigir al usuario a
        else:
            return redirect('reservas_list')
    else:
        return redirect('reservas_list')


@user_passes_test(can_backoffice, login_url="/login/")
def reservas_delete(request, id):
    reserva = Reserva.objects.get(id=id)
    if reserva is not None:
        reserva.delete()
    return redirect('reservas_list')


@user_passes_test(can_backoffice, login_url="/login/")
def tecnicos_list(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'backoffice/tecnicos_especialistas.html',
                  {'tecnicos': tecnicos, 'segment': 'tecnicos_list'})


@user_passes_test(can_backoffice, login_url="/login/")
def tecnicos_create(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            tecnic = form.save()
            return redirect('tecnicos_list')  # Redirigir al usuario a
        else:
            # form = TecnicoForm()
            # return render(request, 'polls/create_book.html', {'form': form})
            return redirect('tecnicos_list')
    else:
        # form = TecnicoForm()
        # return render(request, 'polls/create_book.html', {'form': form})
        return redirect('tecnicos_list')


@user_passes_test(can_backoffice, login_url="/login/")
def tecnicos_delete(request, id):
    tecnico = Tecnico.objects.get(id=id)
    if tecnico is not None:
        tecnico.delete()
        return redirect('tecnicos_list')
    return redirect('tecnicos_list')


@user_passes_test(can_backoffice, login_url="/login/")
def tecnicos_search(request):
    if request.method == 'POST':
        try:
            fecha = datetime.strptime(request.POST['fecha'], '%Y-%m-%d').date()

        except ValueError:
            return redirect('horas_tecnicos_list')

        try:
            hora = datetime.strptime(request.POST['hora'], '%H:%M').time()
        except ValueError:
            hora = datetime.strptime('00:01', '%H:%M').time()

        if fecha is not None:
            consulta_tecnicos = HorarioTecnico.objects.exclude(
                tecnico_id__in=HorarioTecnico.objects.filter(
                    Q(fecha=fecha) &
                    Q(hora_inicio__lte=hora) &
                    Q(hora_fin__gte=hora)
                ).values('tecnico_id').distinct()
            ).values('tecnico__nombre').distinct()

            horas_tecnicos = HorarioTecnico.objects.all()
            tecnicos = Tecnico.objects.all()
            return render(request, 'backoffice/horas_tecnicos_especialistas.html',
                          {'horas_tecnicos': horas_tecnicos, 'tecnicos': tecnicos, 'segment': 'horas_tecnicos_list',
                           'consulta_tecnicos': consulta_tecnicos})
        else:
            return redirect('horas_tecnicos_list')
    else:
        return redirect('horas_tecnicos_list')


@user_passes_test(can_backoffice, login_url="/login/")
def horas_tecnicos_list(request):
    horas_tecnicos = HorarioTecnico.objects.all()
    tecnicos = Tecnico.objects.all()
    return render(request, 'backoffice/horas_tecnicos_especialistas.html',
                  {'horas_tecnicos': horas_tecnicos, 'tecnicos': tecnicos, 'segment': 'horas_tecnicos_list'})


@user_passes_test(can_backoffice, login_url="/login/")
def horas_tecnicos_create(request):
    if request.method == 'POST':
        form = HorarioTecnicoForm(request.POST)
        if form.is_valid():
            horas_tecnico = form.save()
            return redirect('horas_tecnicos_list')  # Redirigir al usuario a
        else:
            return redirect('horas_tecnicos_list')
    else:
        return redirect('horas_tecnicos_list')


@user_passes_test(can_backoffice, login_url="/login/")
def horas_tecnicos_delete(request, id):
    horas_tecnico = HorarioTecnico.objects.get(id=id)
    if horas_tecnico is not None:
        horas_tecnico.delete()
        return redirect('horas_tecnicos_list')
    return redirect('horas_tecnicos_list')


@user_passes_test(can_backoffice, login_url="/login/")
def material_list(request):
    material = Material.objects.all()
    form = MaterialForm()
    return render(request, 'backoffice/material.html',
                  {'material': material, 'segment': 'material_list', 'form': form})


@user_passes_test(can_backoffice, login_url="/login/")
def material_save(request, id=None):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            if id is not None:
                form.instance.id = id
            material = form.save()
            return redirect('material_list')  # Redirigir al usuario a
        else:
            return redirect('material_list')
    else:
        return redirect('material_list')


@user_passes_test(can_backoffice, login_url="/login/")
def material_edit(request, id):
    if id is not None:
        material = Material.objects.all()
        form = MaterialForm(instance=Material.objects.get(id=id))
        return render(request, 'backoffice/material.html',
                      {'material': material, 'segment': 'material_list', 'form': form})
    else:
        return redirect('material_list')


@user_passes_test(can_backoffice, login_url="/login/")
def material_delete(request, id):
    material = Material.objects.get(id=id)
    if material is not None:
        material.delete()
        return redirect('material_list')
    return redirect('material_list')


def salas_list(request):
    salas = Sala.objects.all()
    return render(request, 'backoffice/salas.html',
                  {'salas': salas, 'segment': 'salas_list'})


def salas_create(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            sala = form.save()
            return redirect('salas_list')  # Redirigir al usuario a
        else:
            return redirect('salas_list')
    else:
        return redirect('salas_list')


def salas_delete(request, id):
    sala = Sala.objects.get(id=id)
    if sala is not None:
        sala.delete()
    return redirect('salas_list')


@user_passes_test(can_backoffice, login_url="/login/")
def facturas_list(request):
    facturas = Factura.objects.all()
    return render(request, 'backoffice/factura_list.html',
                  {'facturas': facturas, 'segment': 'reservas_list'})


@user_passes_test(can_backoffice, login_url="/login/")
def facturas_view(request, id=None):
    factura = FacturaForm(prefix='factura')
    # facturas_encoded = serializers.serialize("json", Reserva.objects.values_list("id", "nombre_cliente", "DNI"), cls=DjangoJSONEncoder)
    facturas_encoded = serializers.serialize("json", Reserva.objects.all())

    # LineaFacturaFormSet = inlineformset_factory(Factura, LineaFactura, form=LineaFacturaForm, extra=1, can_delete=True )
    # LineaFacturaFormset = formset_factory(LineaFacturaForm, extra=1)
    linea_factura = linia_factura_formset(prefix='linea_factura')

    if id is not None:
        factura = FacturaForm(instance=Factura.objects.get(id=id), prefix='factura')
        # linea_factura = formset_factory(LineaFacturaForm(instance=LineaFactura.objects.get(factura_id=id)), extra=1)

        # LineaFacturaFormset = inlineformset_factory(Factura, LineaFactura, form=LineaFacturaForm(instance=LineaFactura.objects.get(factura_id=id)),  extra=1)
        # linea_factura = LineaFacturaFormset()
        linea_factura = linia_factura_formset(instance=Factura.objects.get(id=id), prefix='linea_factura')

    return render(request, 'backoffice/factura_view.html',
                  {'factura': factura,
                   'linea_factura': linea_factura,
                   'facturas_encoded': facturas_encoded,
                   'segment': 'factura_view'})


@user_passes_test(can_backoffice, login_url="/login/")
def facturas_save(request, id=None):
    if request.method == 'POST':

        fact = None
        if id is not None:
            fact = get_object_or_404(Factura, pk=id)

        factura = FacturaForm(request.POST, prefix='factura', instance=fact)

        if not factura.is_valid():
            return redirect('facturas_list')

        factura = factura.save()

        if fact is None:
            linea_factura = linia_factura_formset(request.POST, prefix='linea_factura', instance=factura)
        else:
            linea_factura = linia_factura_formset(request.POST, prefix='linea_factura', instance=fact)

        if not linea_factura.is_valid():
            return redirect('facturas_list')

        # for f in linea_factura:
        #    if not f.is_valid():
        #        return redirect('facturas_list')

        linea_factura = linea_factura.save()

        #if fact is None:
            #linea_factura = linia_factura_formset(request.POST, prefix='linea_factura', instance=factura)

        # for f in linea_factura:
        # f.instance.factura = factura
        # f.instance.id = f.data.get('id')
        #    f.save()

    return redirect('facturas_list')


@user_passes_test(can_backoffice, login_url="/login/")
def facturas_delete(request, id):
    factura = Factura.objects.get(id=id)
    if factura is not None:
        factura.delete()
    return redirect('facturas_list')


@user_passes_test(can_backoffice, login_url="/login/")
def facturas_search(request):
    if request.method == 'POST':
        try:
            search = request.POST['search']
        except ValueError:
            return redirect('facturas_list')

        if search is not None:
            try:
                search_number = int(search)
            except ValueError:
                search_number = None

            search_facturas = Factura.objects.filter(
                Q(id=search_number) |
                Q(nombre_cliente__contains=search)
            ).distinct()

            return render(request, 'backoffice/factura_list.html',
                          {'facturas': search_facturas, 'segment': 'facturas_list', 'search': search})

    return redirect('facturas_list')
