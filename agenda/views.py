#/usr/bin/env python
# -*- coding: UTF-8 -*-i
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django import newforms as forms
from agenda.models import Person
from django.newforms import form_for_model, form_for_instance

def index(request):
    "Home page"
    data = dict()
    agenda = Person.objects.all()
    data['agenda']=agenda
    return render_to_response('agenda/index.html',data)


def edit(request,id=None):
    "Edit the agenda"
    data = dict()
    if request.method == 'POST':
        Formulario = form_for_model(Person)
        formulario = Formulario(request.POST)
        if formulario.is_valid():
            persona = formulario.save()
            return HttpResponseRedirect('/agenda/ficha/guardada/%s/'%persona.id)
    else:
        if id == None:
            formulario = form_for_model(Person)
        else:
            persona = get_object_or_404(Person, id=id)
            formulario = form_for_instance(persona)
        data['formulario']=formulario()
    return render_to_response('agenda/edit.html',data)

def ficha(request,accion,id):
    "Add or modify the file"
    data = dict()
    data['accion']=accion
    data['persona']=get_object_or_404(Person,id=id)
    return render_to_response('agenda/ficha.html',data)
