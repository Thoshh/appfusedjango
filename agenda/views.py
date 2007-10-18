#/usr/bin/env python
# -*- coding: UTF-8 -*-i
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django import newforms as forms
from agenda.models import Person
from django.newforms import form_for_model, form_for_instance
from django.core.paginator import ObjectPaginator, InvalidPage
RECORDS_PER_PAGE=2
VISIBLE_PAGES=2
def index(request, page=1):
    "Home page with pagination"
    data = dict()
    paginator = ObjectPaginator(Person.objects.all(),RECORDS_PER_PAGE)
    actual =  int(page) 
    min_page = actual
    max_page = actual + VISIBLE_PAGES
    if actual >= paginator.pages:
        max_page = actual+1
        min_page = actual-VISIBLE_PAGES+1
    page_numbers = [n for n in range(min_page, max_page ) ]
    data['agenda']=paginator.get_page(actual-1)
    data['actual_page'] = actual
    data['previous_page'] = actual-1
    data['next_page'] = actual +1
    data['has_next']=paginator.has_next_page(actual-1)
    data['has_previous'] = paginator.has_previous_page(actual-1)
    data['page_numbers'] = page_numbers
    data['url']='/agenda/list/page/'
    data['pages']=paginator.pages
    data['hits'] = paginator.hits
    data['show_first'] = 1 not in page_numbers
    data['show_last'] = page not in page_numbers
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
