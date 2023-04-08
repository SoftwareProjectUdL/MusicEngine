from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView
from MusicEngineApp.backoffice.models import Reserva


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('backoffice/index.html')
    return HttpResponse(html_template.render(context, request))


def reserves(request):
    context = {'segment': 'reservas'}
    html_template = loader.get_template('backoffice/reserva/reserva_list.html')
    return HttpResponse(html_template.render(context, request))

