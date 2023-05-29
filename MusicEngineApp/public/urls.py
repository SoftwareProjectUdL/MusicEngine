from django.urls import path

from .views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('reserva', reserva_view, name="reserva"),
    path('reserva/save', reserva_save, name="reserva_save"),
    path('reserva/state/', reserva_state, name="reserva_state"),
    path('reserva/state/<int:id>/<str:estado>', reserva_state, name="reserva_state"),
    path('historic', historico_view, name="historico"),
    path('tiquets/', tiquets_list, name="tiquets"),
    path('tiquets/<int:id>', tiquets_list, name="tiquets"),
    path('tiquets/save/', tiquets_save, name="tiquets_save"),
    path('tiquets/save/<int:id>', tiquets_save, name="tiquets_save"),
    path('tiquets/delete/', tiquets_delete, name="tiquets_delete"),
    path('tiquets/delete/<int:id>', tiquets_delete, name="tiquets_delete"),
    path('facturas', facturas_list, name="facturas"),

]
