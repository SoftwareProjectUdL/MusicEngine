from django.contrib import admin
from MusicEngineApp.backoffice.models import *

# Register your models here.
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')


class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')


class HorarioTecnicoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora_inicio', 'hora_fin', 'tecnico')
    search_fields = ('fecha', 'hora_inicio', 'hora_fin', 'tecnico')


class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'DNI', 'nombre_cliente', 'telefono', 'fecha', 'hora_inicio', 'hora_fin', 'sala', 'material', 'tecnico')
    search_fields = (
        'DNI', 'nombre_cliente', 'telefono', 'fecha', 'hora_inicio', 'hora_fin', 'sala', 'material', 'tecnico')


admin.site.register(Reserva, ReservaAdmin)
admin.site.register(HorarioTecnico, HorarioTecnicoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Tecnico, TecnicoAdmin)
