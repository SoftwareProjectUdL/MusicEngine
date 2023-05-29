from sqlite3 import Date

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from MusicEngineApp.models import Tecnico, Material, Sala, Reserva, Tiquet, ConversacionTiquet, Factura
from MusicEngineApp.public.forms import ReservaForm, TiquetForm, ConversacionTiquetForm


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
            # form.DNI = request.user.dni
            # form.telefono = request.user.telefono
            reserva = form.save()
            return render(request, "public/reserva.html",
                          {'segment': 'reserva', 'popup': 'Reserva creada correctament.', 'reserva': reserva})
        else:
            return redirect('reserva')
    else:
        return redirect('reserva')


@user_passes_test(can_public, login_url='/login/')
def reserva_state(request, id, estado):
    reserva = Reserva.objects.get(id=id)
    reserva.estado = estado
    reserva.save()
    if int(estado) == Reserva.Estado.PAGADA and not Factura.objects.filter(reserva=reserva).exists():
        factura = Factura(reserva=reserva, total=100, fecha=Date.today(), nombre_cliente=reserva.nombre_cliente, dni=reserva.DNI)
        factura.save()
        return redirect('facturas')
    elif int(estado) == Reserva.Estado.CANCELADA and Factura.objects.filter(reserva=reserva).exists():
        Factura.objects.get(reserva=reserva).delete()
    return redirect('historico')


@user_passes_test(can_public, login_url='/login/')
def historico_view(request):
    reservas = Reserva.objects.filter(nombre_cliente=request.user.username)
    estado = Reserva.Estado
    return render(request, "public/historico-reservas.html",
                  {'segment': 'hisotrico', 'reserves': reservas, 'estado': estado})


@user_passes_test(can_public, login_url='/login/')
def tiquets_list(request, id=None):
    tiquets = Tiquet.objects.filter(usuario=User.objects.get(id=request.user.id))
    conversacion_tiquet = ConversacionTiquetForm(prefix="conversacion_tiquet",
                                                 initial={'usuario': request.user.id})

    tiquet = TiquetForm(prefix="tiquet", initial={'usuario': request.user.id})
    conversaciones = []
    if id is not None:
        tiquet = TiquetForm(instance=Tiquet.objects.get(id=id), prefix="tiquet",
                            initial={'usuario': User.objects.get(id=request.user.id)})
        conversaciones = ConversacionTiquet.objects.filter(tiquet=Tiquet.objects.get(id=id))

    return render(request, "public/tiquets.html",
                  {'segment': 'tiquets', 'tiquet_form': tiquet, 'tiquets': tiquets, 'conversaciones': conversaciones,
                   'conv_tiquet_form': conversacion_tiquet})


@user_passes_test(can_public, login_url='/login/')
def tiquets_save(request, id=None):
    if request.method == 'POST':

        form_tiquet = TiquetForm(request.POST, prefix="tiquet")
        form_conv_tiquet = ConversacionTiquetForm(request.POST, prefix="conversacion_tiquet")

        # form_tiquet.instance.usuario = User.objects.get(id=request.user.id)
        # form_conv_tiquet.instance.usuario = User.objects.get(id=request.user.id)
        # form_conv_tiquet.cleaned_data['usuario'] = request.user.id
        # form_conv_tiquet.changed_data.append('usuario')
        # form_conv_tiquet.instance.usuario_id = request.user.id
        # form_conv_tiquet.fields['usuario'].initial = request.user.id

        if form_tiquet.is_valid():
            if id is not None:
                form_tiquet.instance.id = id
            tiquet = form_tiquet.save()
            form_conv_tiquet.instance.usuario = User.objects.get(id=request.user.id)
            form_conv_tiquet.instance.tiquet = tiquet
            form_conv_tiquet = ConversacionTiquetForm(
                {'usuario': User.objects.get(id=request.user.id), 'tiquet': Tiquet.objects.get(id=tiquet.id),
                 'mensaje': request.POST['conversacion_tiquet-mensaje']})
            if form_conv_tiquet.is_valid():
                form_conv_tiquet.save()
            return redirect('/tiquets/' + str(tiquet.id))
        else:
            return redirect('tiquets')
    return redirect('tiquets')


@user_passes_test(can_public, login_url='/login/')
def tiquets_delete(request, id=None):
    if id is not None:
        tiquet = Tiquet.objects.get(id=id)
        tiquet.delete()
    return redirect('tiquets')

@user_passes_test(can_public, login_url='/login/')
def facturas_list(request):
    facturas = Factura.objects.filter(nombre_cliente=request.user.username)
    return render(request, 'public/facturas.html',
                  {'facturas': facturas, 'segment': 'reservas'})