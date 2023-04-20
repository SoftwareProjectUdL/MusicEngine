from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


#@user_passes_test(lambda u: u.is_authenticated is False, login_url='/')
def login_view(request, msg=None):
    form = LoginForm(request.POST or None)
    msg = request.GET.get('msg')
    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name__in=['gestor', 'comercial']).exists():
                    return redirect("/backoffice")
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "authentication/login.html", {"form": form, "msg": msg})


@user_passes_test(lambda u: u.is_authenticated is False, login_url='/')
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='client')
            user.groups.add(group)
            return redirect("/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, "authentication/register.html", {"form": form, "msg": msg, "success": success})


@user_passes_test(lambda u: u.is_authenticated is True, login_url='/')
def logout_redirect(request):
    logout(request)
    return redirect("/login?msg=Logged out successfully.")
