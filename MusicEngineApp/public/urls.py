from django.urls import path

from .views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('reserva', reserva_view, name="reserva"),
    path('reserva/save', reserva_save, name="reserva_save"),
]
