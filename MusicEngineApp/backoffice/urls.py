from django.shortcuts import redirect
from django.urls import path, re_path
from MusicEngineApp.backoffice import views

urlpatterns = [

    # The home page
    path('backoffice', views.index, name='home'),
    # path('', views.index, name='home'),
    # path('', lambda request: redirect('backoffice', permanent=False)),

    # Matches any html file
    # re_path(r'^backoffice/.*\.*', views., name='pages'),

]
