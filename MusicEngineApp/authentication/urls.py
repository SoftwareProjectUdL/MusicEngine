from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", logout_redirect, name="logout")
]
