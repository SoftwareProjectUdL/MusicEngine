from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import ListView

from MusicEngineApp.backoffice.forms import HorarioTecnicoForm, TecnicoForm
from MusicEngineApp.backoffice.models import Reserva, Tecnico, HorarioTecnico


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'home_back'}
    html_template = loader.get_template('backoffice/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def reservas_list(request):
    reserves = Reserva.objects.all()
    return render(request, 'backoffice/reserva/reserva_list.html',
                  {'reserves': reserves, 'segment': 'reservas_list'})


# @login_required(login_url="/login/")
def tecnicos_list(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'backoffice/tecnicos_especialistas.html',
                  {'tecnicos': tecnicos, 'segment': 'tecnicos_list'})


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


def tecnicos_delete(request, id):
    tecnico = Tecnico.objects.get(id=id)
    if tecnico is not None:
        tecnico.delete()
        return redirect('tecnicos_list')
    return redirect('tecnicos_list')


# class HorasTecnicoListView(ListView):
#     model = HorarioTecnico
#     template_name = 'backoffice/horas_tecnicos_especialistas.html'
#     context_object_name = 'horas_tecnicos'


def horas_tecnicos_list(request):
    horas_tecnicos = HorarioTecnico.objects.all()
    tecnicos = Tecnico.objects.all()
    return render(request, 'backoffice/horas_tecnicos_especialistas.html',
                  {'horas_tecnicos': horas_tecnicos, 'tecnicos': tecnicos, 'segment': 'horas_tecnicos_list'})


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


def horas_tecnicos_delete(request, id):
    horas_tecnico = HorarioTecnico.objects.get(id=id)
    if horas_tecnico is not None:
        horas_tecnico.delete()
        return redirect('horas_tecnicos_list')
    return redirect('horas_tecnicos_list')
