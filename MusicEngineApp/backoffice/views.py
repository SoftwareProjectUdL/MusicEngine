from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from MusicEngineApp.backoffice.forms import TecnicoForm, HorarioTecnicoForm, MaterialForm
from MusicEngineApp.backoffice.models import Reserva, Tecnico, HorarioTecnico, Material


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'home_back'}
    html_template = loader.get_template('backoffice/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def reservas_list(request):
    reserves = Reserva.objects.all()
    return render(request, 'backoffice/reserva/reserva_list.html',
                  {'reserves': reserves, 'segment': 'reservas_list'})


@login_required(login_url="/login/")
def tecnicos_list(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'backoffice/tecnicos_especialistas.html',
                  {'tecnicos': tecnicos, 'segment': 'tecnicos_list'})


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def tecnicos_delete(request, id):
    tecnico = Tecnico.objects.get(id=id)
    if tecnico is not None:
        tecnico.delete()
        return redirect('tecnicos_list')
    return redirect('tecnicos_list')


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def horas_tecnicos_list(request):
    horas_tecnicos = HorarioTecnico.objects.all()
    tecnicos = Tecnico.objects.all()
    return render(request, 'backoffice/horas_tecnicos_especialistas.html',
                  {'horas_tecnicos': horas_tecnicos, 'tecnicos': tecnicos, 'segment': 'horas_tecnicos_list'})


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def horas_tecnicos_delete(request, id):
    horas_tecnico = HorarioTecnico.objects.get(id=id)
    if horas_tecnico is not None:
        horas_tecnico.delete()
        return redirect('horas_tecnicos_list')
    return redirect('horas_tecnicos_list')


@login_required(login_url="/login/")
def material_list(request):
    material = Material.objects.all()
    return render(request, 'backoffice/material.html',
                  {'material': material})


@login_required(login_url="/login/")
def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save()
            return redirect('material_list')  # Redirigir al usuario a
        else:
            return redirect('material_list')
    else:
        return redirect('material_list')


@login_required(login_url="/login/")
def material_delete(request, id):
    material = Material.objects.get(id=id)
    if material is not None:
        material.delete()
        return redirect('material_list')
    return redirect('material_list')