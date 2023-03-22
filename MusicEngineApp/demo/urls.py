from django.urls import path, re_path
from MusicEngineApp.demo import views

urlpatterns = [

    # The home page
    path('demo', views.index, name='demo'),

    # Matches any html file
    re_path(r'^demo/.*\.*', views.pages, name='pages'),

]
