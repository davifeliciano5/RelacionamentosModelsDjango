from django.contrib import admin
from .models import Carro,Chassi,Montadora


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora','modelo','chassi','preco','get_motorista')

    def get_motorista(self, obg):
        return ', '.join([m.username for m in obg.motorista.all()])
    get_motorista.short_description = 'Motorista'

