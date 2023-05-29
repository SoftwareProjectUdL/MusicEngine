from datetime import datetime

from django.contrib import admin, auth
from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre


class Material(models.Model):
    class Estado(models.IntegerChoices):
        BUENO = 0, ('bueno')
        REGULAR = 1, ('regular')
        MALO = 2, ('malo')

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField(default=Estado.BUENO, choices=Estado.choices)
    cantidad = models.IntegerField()

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre


class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre


class HorarioTecnico(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre

    def horas(self):
        # get the difference between the two times
        h_inicio = datetime.combine(datetime.today(), self.hora_inicio)
        h_fin = datetime.combine(datetime.today(), self.hora_fin)
        duration = h_fin - h_inicio
        return duration.total_seconds() / 3600



class Reserva(models.Model):

    class Estado(models.IntegerChoices):
        PENDIENTE = 0, ('pendiente')
        VALIDADA = 1, ('validada')
        PAGADA = 2, ('pagada')
        CANCELADA = 3, ('cancelada')

    id = models.AutoField(primary_key=True)
    DNI = models.CharField(max_length=100)
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    estado = models.IntegerField(default=Estado.PENDIENTE, choices=Estado.choices)


    def __str__(self):
        return self.nombre_cliente

    def __unicode__(self):
        return self.nombre_cliente


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    total = models.IntegerField()
    lineas = models.ManyToManyField(
        'LineaFactura',
        related_name='lineas',
    )

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre_cliente


class LineaFactura(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.IntegerField()


class LiniaFacturaAdmin(admin.TabularInline):
    model = LineaFactura
    extra = 1



class Tiquet(models.Model):
    id = models.AutoField(primary_key=True)
    assunto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField(default=datetime.now)


class ConversacionTiquet(models.Model):
    id = models.AutoField(primary_key=True)
    tiquet = models.ForeignKey(Tiquet, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now)


class ConversacionTiquetAdmin(admin.TabularInline):
    model = ConversacionTiquet
    extra = 1