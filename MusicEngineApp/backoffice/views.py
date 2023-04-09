from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import ListView

from MusicEngineApp.backoffice.forms.TecnicoForm import TecnicoForm
from MusicEngineApp.backoffice.models import Reserva, Tecnico


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('backoffice/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
class ReservesListView(ListView):
    model = Reserva
    template_name = 'backoffice/reserva/reserva_list.html'
    context_object_name = 'reserves'


# @login_required(login_url="/login/")
class TecnicoListView(ListView):
    model = Tecnico
    template_name = 'backoffice/tecnicos_especialistas.html'
    context_object_name = 'tecnicos'


def create_tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            tecnic = form.save()
            return redirect('tecnico_list')  # Redirigir al usuario a
        else:
            # form = TecnicoForm()
            # return render(request, 'polls/create_book.html', {'form': form})
            return redirect('tecnico_list')
    else:
        # form = TecnicoForm()
        # return render(request, 'polls/create_book.html', {'form': form})
        return redirect('tecnico_list')


def delete_tecnico(request, id):
    tecnico = Tecnico.objects.get(id=id)
    if tecnico is not None:
        tecnico.delete()
        return redirect('tecnico_list')
    return redirect('tecnico_list')
