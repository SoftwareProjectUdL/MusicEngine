from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

from MusicEngineApp.backoffice.models import Tecnico, Material, Sala, Reserva
from MusicEngineApp.public.forms import ReservaForm


def can_public(u):
    return u.is_superuser or u.groups.filter(name__in=['client']).exists() is True


@user_passes_test(can_public, login_url='/login/')
def home_view(request):
    return render(request, "public/home.html", {'segment': 'home'})


@user_passes_test(can_public, login_url='/login/')
def reserva_view(request):
    tecnicos = Tecnico.objects.all()
    materials = Material.objects.all()
    salas = Sala.objects.all()
    reserva = ReservaForm({'nombre_cliente': request.user.username})
    return render(request, "public/reserva.html",
                  {'segment': 'reserva', 'tecnicos': tecnicos, 'materials': materials, 'salas': salas,
                   'reserva': reserva})


@user_passes_test(can_public, login_url='/login/')
def reserva_save(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.nombre_cliente = request.user.username
            #form.DNI = request.user.dni
            #form.telefono = request.user.telefono
            reserva = form.save()
            return render(request, "public/reserva.html",
                          {'segment': 'reserva', 'popup': 'Reserva creada correctament.', 'reserva': reserva})
        else:
            return redirect('reserva')
    else:
        return redirect('reserva')
