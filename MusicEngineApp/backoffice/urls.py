from django.urls import path

from MusicEngineApp.backoffice import views
from MusicEngineApp.backoffice.views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home_back'),

    path('tecnicos', tecnicos_list, name='tecnicos_list'),
    path('tecnicos/create', tecnicos_create, name='tecnicos_create'),
    path('tecnicos/delete/', tecnicos_delete, name='tecnicos_delete'),
    path('tecnicos/delete/<int:id>', tecnicos_delete, name='tecnicos_delete'),
    path('tecnicos/search', tecnicos_search, name='tecnicos_search'),

    path('horas-tecnicos', horas_tecnicos_list, name='horas_tecnicos_list'),
    path('horas-tecnicos/create', horas_tecnicos_create, name='horas_tecnicos_create'),
    path('horas-tecnicos/delete/', horas_tecnicos_delete, name='horas_tecnicos_delete'),
    path('horas-tecnicos/delete/<int:id>', horas_tecnicos_delete, name='horas_tecnicos_delete'),

    path('material', material_list, name='material_list'),
    path('material/save', material_save, name='material_save'),
    path('material/save/<int:id>', material_save, name='material_save'),
    path('material/delete/', material_delete, name='material_delete'),
    path('material/delete/<int:id>', material_delete, name='material_delete'),
    path('material/edit/', material_edit, name='material_edit'),
    path('material/edit/<int:id>', material_edit, name='material_edit'),

    path('sales', salas_list, name='salas_list'),
    path('sales/create', salas_create, name='salas_create'),
    path('sales/delete/', salas_delete, name='salas_delete'),
    path('sales/delete/<int:id>', salas_delete, name='salas_delete'),

    path('reservas', reservas_list, name='reservas_list'),
    path('reservas/view/', reservas_view, name='reservas_view'),
    path('reservas/view/<int:id>', reservas_view, name='reservas_view'),
    path('reservas/create', reservas_create, name='reservas_create'),
    path('reservas/delete/', reservas_delete, name='reservas_delete'),
    path('reservas/delete/<int:id>', reservas_delete, name='reservas_delete'),

    # path('', views.index, name='home'),
    # path('', lambda request: redirect('backoffice', permanent=False)),

    # Matches any html file
    # re_path(r'^backoffice/.*\.*', views., name='pages'),

]
