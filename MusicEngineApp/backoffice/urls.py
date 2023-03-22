from django.urls import path, re_path
from MusicEngineApp.backoffice import views

urlpatterns = [

    # The home page
    path('backoffice', views.index, name='home'),

    # Matches any html file
    # re_path(r'^backoffice/.*\.*', views., name='pages'),

]
