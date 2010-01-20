#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from models import Evento
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from evento.models import Inscrito
from evento.forms import ConfirmForm, InscripcioForm
from django.utils.translation import ugettext_lazy as _


def eventos(request):
    """Muestra la lista de eventos activos en la página principal"""
    data ={'eventos': Evento.activos.all() }
    return direct_to_template(request, 'index.html', data)


def ficha_evento(request, slug):
    """Información sobre un evento concreto"""
    evento = get_object_or_404(Evento, slug = slug)
    return direct_to_template(request, 'evento/ficha.html', {'evento': evento})

@login_required
def inscribirse(request, slug):
    """Un usuario puede inscribirse a un envento si no se ha inscrito ya,
    está autenticado y el evento está activo"""
    user = request.user
    evento = get_object_or_404(Evento, slug = slug)
    inscripcion = None
    if evento.activo:
        if request.method == 'GET':
            form = InscripcioForm()
        else:
            form = InscripcioForm(request.POST)
            if form.is_valid():
                try:
                    inscripcion = Inscrito.objects.get(user=user, evento = evento)
                    msg = _("Ja estàs inscrit a l'event")
                except Inscrito.DoesNotExist:
                    inscripcion = Inscrito(user=user, evento=evento, 
                                    comentario = form.cleaned_data['comentario'])
                    inscripcion.en_lista_espera = evento.completo
                    inscripcion.save()
                    return redirect('inscripcion-realizada', slug = slug) 
        return direct_to_template(request, 'evento/inscripcion_evento.html', 
                                    {'evento': evento, 'form':form})
    else:
        msg = _("L'event ja està tancat i no admet més inscripcions")
    data = {'msg': msg, 'inscripcion': inscripcion}
    return direct_to_template(request, 'evento/message.html', data)

@login_required
def inscripcion_realizada(request, slug):
    evento = get_object_or_404(Evento, slug=slug)
    inscripcion = get_object_or_404(Inscrito, user = request.user, evento = evento)
    return direct_to_template(request, 'evento/inscrito.html', {'evento':evento, 'inscripcion': inscripcion})

@login_required
def mis_inscripciones(request):
    return direct_to_template(request, 'evento/mis_inscripciones.html' )

@login_required
def cancela_inscripcion(request, slug):
    """Cancela la inscripción a un evento"""
    evento = get_object_or_404(Evento, slug=slug)
    if not evento.admite_inscripciones:
        return direct_to_template(request, 'evento/message.html', {msg: "L'event és tancat" })
    if request.method == 'GET':
        form = ConfirmForm()
    else:
        form = ConfirmForm(request.POST)
        if form.is_valid():
            inscripcion = get_object_or_404(Inscrito, user = request.user, evento = evento)
            inscripcion.delete()
            return redirect('inscripcion-cancelada', slug = slug)
    return direct_to_template(request, 'evento/cancela_inscripcion.html', 
                              {'evento': evento, 'form': form } )
   

@login_required
def inscripcion_cancelada(request, slug):
    evento = get_object_or_404(Evento, slug=slug) 
    return direct_to_template(request, 'evento/inscripcion_cancelada.html', {'evento': evento} )


    
