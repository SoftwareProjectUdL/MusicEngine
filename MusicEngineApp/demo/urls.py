from django.urls import path, re_path

from MusicEngineApp.demo import views

urlpatterns = [

    # The home page
    path('', views.index, name='demo'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
