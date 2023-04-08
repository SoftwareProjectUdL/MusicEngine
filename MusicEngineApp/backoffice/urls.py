from django.shortcuts import redirect
from django.urls import path
from MusicEngineApp.backoffice import views
from MusicEngineApp.backoffice.views import *


urlpatterns = [

    # The home page
    path('backoffice', views.index, name='home'),
    path('backoffice/tecnics', TecnicListView.as_view(), name='tecnic_list'),
    path('backoffice/reservas', ReservesListView.as_view(), name='reserves_list'),

    # path('', views.index, name='home'),
    # path('', lambda request: redirect('backoffice', permanent=False)),

    # Matches any html file
    # re_path(r'^backoffice/.*\.*', views., name='pages'),

]
