from django.urls import path, re_path
from MusicEngineApp.demo import views

urlpatterns = [

    # The home page
    path('demo', views.index, name='home'),

    # Matches any html file
    re_path(r'^demo/.*\.*', views.pages, name='pages'),

]
