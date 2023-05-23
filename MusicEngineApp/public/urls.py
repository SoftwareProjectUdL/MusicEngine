from django.urls import path

from .views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('reserva', reserva_view, name="reserva"),
    path('reserva/save', reserva_save, name="reserva_save"),
    path('reserva/state/', reserva_state, name="reserva_state"),
    path('reserva/state/<int:id>/<str:estado>', reserva_state, name="reserva_state"),
    path('historic', historico_view, name="historico"),
]
