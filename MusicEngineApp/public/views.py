from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


def can_public(u):
    return u.is_superuser or u.groups.filter(name__in=['client']).exists() is True


@user_passes_test(can_public, login_url='/login/')
def home_view(request, msg=None):
    return render(request, "public/home.html", {})