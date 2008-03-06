#/usr/bin/env python
# -*- coding: UTF-8 -*-i
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import ObjectPaginator, InvalidPage
from django import http
from django import newforms as forms
from django.newforms import form_for_model, form_for_instance
from agenda.models import Person
from django.utils.translation import ugettext as _
from django.utils.translation import check_for_language, activate, to_locale, get_language
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers
from django.utils.cache import patch_vary_headers
from django.views.decorators.cache import never_cache

# ext+json
from django.http import HttpResponse 
from django.core import serializers 

RECORDS_PER_PAGE=2
VISIBLE_PAGES=2


def index(request, page=1):
    "Home page with pagination"
    request.logger.info('Entrant a a Index')
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
    request.logger.info('dades obtingutdes, preparant plana web')
    response = render_to_response('agenda/index.html',data)
    return response
index = cache_page(index, 3600)

def edit(request,id=None):
    "Edit the agenda"
    request.logger.info('Editando')
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

@cache_page(3600)
@cache_control(no_cache=True, must_revalidate=True)
@vary_on_headers('Content-Language')
def ficha(request,accion,id):
    "Add or modify the file"
    request.logger.info('Informació de la fitxa')
    data = dict()
    data['accion']=accion
    data['persona']=get_object_or_404(Person,id=id)
    return render_to_response('agenda/ficha.html',data)

def delete(request,id):
    persona = get_object_or_404(Person,id=id)
    if request.method =='POST':
        persona.delete()
        return HttpResponseRedirect('/agenda/deleted/')
    else:
        data = dict()
        data['ficha']=persona
        return render_to_response('agenda/confirmar.html',data)

def deleted(request):
    return render_to_response('agenda/deleted.html')

def cambiar_idioma(request,idioma):
    """
    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it should
    only be accessed as a POST request, but just for this kind of operation I personally
    prefer the GET option
    """
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)

    lang_code = idioma
    if lang_code and check_for_language(lang_code):
        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
        else:
            response.set_cookie('django_language', lang_code)
    return response

def grid_view(request):
    return render_to_response('agendajs/table.html')

def json_list(request):
    queryset = Person.objects.all()
    root_name = 'rows' # or it can be queryset.model._meta.verbose_name_plural
    data = '{"total": %s, "%s": %s}' % (queryset.count(), root_name, serializers.serialize('json', queryset))
    return HttpResponse(data, mimetype='text/javascript;')  
