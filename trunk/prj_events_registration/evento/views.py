#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from models import Evento
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

def eventos(request):
    """Muestra la lista de eventos activos en la página principal"""
    data ={'eventos': Evento.activos.all() }
    return direct_to_template(request, 'index.html', data)


def ficha_evento(request, slug):
    """Información sobre un evento concreto"""
    evento = get_object_or_404(Evento, slug = slug)
    return direct_to_template(request, 'evento/ficha.html', {'evento': evento})
