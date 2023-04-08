from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from MusicEngineApp.backoffice.models import Reserva, Tecnico


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('backoffice/index.html')
    return HttpResponse(html_template.render(context, request))


#@login_required(login_url="/login/")
class ReservesListView(ListView):
    model = Reserva
    template_name = 'backoffice/reserva/reserva_list.html'
    context_object_name = 'reserves'


# @login_required(login_url="/login/")
class TecnicListView(ListView):
    model = Tecnico
    template_name = 'backoffice/tecnics_especialistes.html'
    context_object_name = 'tecnics'
