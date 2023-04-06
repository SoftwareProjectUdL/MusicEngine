from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')


class Material(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')


class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')


class HorarioTecnico(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre


class HorarioTecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora_inicio', 'hora_fin', 'tecnico')
    search_fields = ('nombre', 'fecha', 'hora_inicio', 'hora_fin', 'tecnico')


class Reserva(models.Model):
    DNI = models.CharField(max_length=100)
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre


class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'DNI', 'nombre_cliente', 'telefono', 'fecha', 'hora_inicio', 'hora_fin', 'sala', 'material', 'tecnico')
    search_fields = (
        'DNI', 'nombre_cliente', 'telefono', 'fecha', 'hora_inicio', 'hora_fin', 'sala', 'material', 'tecnico')
