#/usr/bin/env python
# -*- coding: UTF-8 -*-i
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import QuerySetPaginator, InvalidPage

from django import http
from django import newforms as forms
from django.newforms import form_for_model, form_for_instance
from django.utils.translation import ugettext as _
from django.utils.translation import check_for_language, activate, to_locale, get_language
from django.utils.cache import patch_vary_headers
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.cache import never_cache
from agenda.models import Person

# ext+json
from django.http import HttpResponse 
from django.core import serializers 

RECORDS_PER_PAGE=2
VISIBLE_PAGES=3


def index(request, page=1):
    "Home page with pagination. Adapted to the trunk version of paginator"
    request.logger.info('Entrant a a Index')
    data = dict()
    actual_page = int(page)
    paginator = QuerySetPaginator(Person.objects.all(),RECORDS_PER_PAGE)
    data['page'] = paginator.page(int(page))
    data['paginator'] = paginator
    data['url']='/agenda/list/page/'
    #numbre of pages you want visible    
    if actual_page+VISIBLE_PAGES-1 <= paginator.num_pages:
        start_range = actual_page
    else:
        start_range = max(paginator.num_pages - VISIBLE_PAGES +1,1)
    end_range= min(start_range+VISIBLE_PAGES-1, paginator.num_pages)
    data['range'] = range(start_range,end_range)
    data['end_range'] = end_range    
#    if end_range<>total:
#        print "..",
#    print total
#    if actual_page <= total:
#        actual_page +=1
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
