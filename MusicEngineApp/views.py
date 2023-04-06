from django.shortcuts import render
from django.views.generic import ListView

from MusicEngineApp.models import Reserva


# Create your views here.

# ListViews
class ReservaListView(ListView):
    model = Reserva
    template_name = 'reserva/reserva_list.html'
    context_object_name = 'reservas'
