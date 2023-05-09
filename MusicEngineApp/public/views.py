from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


@user_passes_test(lambda u: u.is_authenticated is False, login_url='/')
def home_view(request, msg=None):
    return render(request, "public/home.html", {})