from django.urls import path

from MusicEngineApp.backoffice import views
from MusicEngineApp.backoffice.views import *

urlpatterns = [

    # The home page
    path('backoffice', views.index, name='home_back'),

    path('backoffice/tecnicos', tecnicos_list, name='tecnicos_list'),
    path('backoffice/tecnicos/create', tecnicos_create, name='tecnicos_create'),
    path('backoffice/tecnicos/delete/', tecnicos_delete, name='tecnicos_delete'),
    path('backoffice/tecnicos/delete/<int:id>', tecnicos_delete, name='tecnicos_delete'),
    path('backoffice/tecnicos/search', tecnicos_search, name='tecnicos_search'),

    path('backoffice/horas-tecnicos', horas_tecnicos_list, name='horas_tecnicos_list'),
    path('backoffice/horas-tecnicos/create', horas_tecnicos_create, name='horas_tecnicos_create'),
    path('backoffice/horas-tecnicos/delete/', horas_tecnicos_delete, name='horas_tecnicos_delete'),
    path('backoffice/horas-tecnicos/delete/<int:id>', horas_tecnicos_delete, name='horas_tecnicos_delete'),

    path('backoffice/material', material_list, name='material_list'),
    path('backoffice/material/create', material_create, name='material_create'),
    path('backoffice/material/delete/', material_delete, name='material_delete'),
    path('backoffice/material/delete/<int:id>', material_delete, name='material_delete'),

    path('backoffice/reservas', reservas_list, name='reservas_list'),
    path('backoffice/reservas/view', reservas_view, name='reservas_view'),
    path('backoffice/reservas/create', reservas_create, name='reservas_create'),

    # path('', views.index, name='home'),
    # path('', lambda request: redirect('backoffice', permanent=False)),

    # Matches any html file
    # re_path(r'^backoffice/.*\.*', views., name='pages'),

]
