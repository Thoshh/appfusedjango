# -*- coding: UTF-8 -*-

from django.contrib import admin
from models import Evento, Inscrito

class InscritoInline(admin.TabularInline):
    model = Inscrito

class EventoManager(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'capacidad', 'inscritos', 'activo')
    list_filter = ('fecha', 'activo')
    prepopulated_fields  = {'slug': ("nombre",) }
    inlines = [ InscritoInline, ]
    

admin.site.register(Evento, EventoManager)
