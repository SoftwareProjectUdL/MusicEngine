from django.shortcuts import redirect
from django.urls import path
from MusicEngineApp.backoffice import views
from MusicEngineApp.backoffice.views import *


urlpatterns = [

    # The home page
    path('backoffice', views.index, name='home'),
    path('backoffice/tecnicos', TecnicoListView.as_view(), name='tecnico_list'),
    path('backoffice/tecnicos/create', create_tecnico, name='tecnico_create'),
    path('backoffice/tecnicos/delete/', delete_tecnico, name='tecnico_delete'),
    path('backoffice/tecnicos/delete/<int:id>', delete_tecnico, name='tecnico_delete'),

    path('backoffice/reservas', ReservesListView.as_view(), name='reserves_list'),

    # path('', views.index, name='home'),
    # path('', lambda request: redirect('backoffice', permanent=False)),

    # Matches any html file
    # re_path(r'^backoffice/.*\.*', views., name='pages'),

]
