#/usr/bin/env python
# -*- coding: UTF-8 -*-
from agenda.models import Person
from django import http
from django.core import serializers
from django.core.paginator import QuerySetPaginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.utils.translation import check_for_language
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from formularis import PersonForm
from formularis import SearchForm
from django.db.models import Q
from django.core.paginator import EmptyPage
from django.template import RequestContext
import urllib
import cgi

RECORDS_PER_PAGE=2
VISIBLE_PAGES=3


def index(request, page=1):
    "Home page with pagination. Adapted to the trunk version of paginator"
    newurl = ''
    
    #cgi.parse_qsl(request)
    if (len(request.GET)>0) or (len(request.META['PATH_INFO']) >0):
        if request.GET:
            search_form = SearchForm(request.GET)
        else:
            values = {}
            for k,v in cgi.parse_qs(request.META['PATH_INFO'], True).items():
                if v[0] != 'None':
                    values[k] = v[0]
            search_form = SearchForm(values)

        if search_form.is_valid():
            searchdict = search_form.cleaned_data
            qdict = { 'first_name': 'first_name__icontains',
                      'last_name': 'last_name__icontains',
                      'age': 'age'}
            q_objs = [Q(**{qdict[k]: searchdict[k]}) for k in qdict.keys() if searchdict.get(k, None)]
            results = Person.objects.select_related().filter(*q_objs).order_by('first_name')

            # Encode the GET data to a URL so we can append it to the next
            # and previous page links.
            rawurl = urllib.urlencode(searchdict)
            if len(rawurl):
                newurl = '&' + rawurl
    else:
        results = Person.objects.all()
        search_form = SearchForm()

    data = dict()
    actual_page = int(page)
    paginator = QuerySetPaginator(results,RECORDS_PER_PAGE)
    try:
        data['page'] = paginator.page(int(page))
    except EmptyPage:
        data['page'] = paginator.page(1)
        actual_page = 1
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
    data['form'] = search_form
    data['newurl'] = newurl
    return  render_to_response('agenda/index.html',data, context_instance=RequestContext(request))
    


def edit(request,id=None):
    """Edit the agenda, the definition is a nice trick from 
    http://themorgue.org/blog/2008/05/14/django-and-modelform/"""
    formulario = PersonForm(request.POST or None, instance = id and Person.objects.get(id = id) )
    if request.method == 'POST':
        if formulario.is_valid():
            persona = formulario.save()
            return HttpResponseRedirect('/agenda/ficha/guardada/%s/'%persona.id)
    return render_to_response('agenda/edit.html', {'formulario': formulario})


@cache_control(no_cache=True, must_revalidate=True)
@vary_on_headers('Content-Language')
def ficha(request,accion,id):
    "Add or modify the file"
    data = dict()
    data['accion'] = accion
    data['persona'] = get_object_or_404(Person,id=id)
    return render_to_response('agenda/ficha.html', data)

def delete(request,id):
    "Delete the file"
    persona = get_object_or_404(Person,id=id)
    if request.method == 'POST':
        persona.delete()
        return HttpResponseRedirect('/agenda/deleted/')
    else:
        data = dict()
        data['ficha'] = persona
        return render_to_response('agenda/confirmar.html', data)

def deleted(request):
    "Returns the deleted message"
    return render_to_response('agenda/deleted.html')

def cambiar_idioma(request, idioma):
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
    "Shows the table js view"
    return render_to_response('agendajs/table.html')

def json_list(request):
    "Returns the data in json format"
    queryset = Person.objects.all()
    root_name = 'rows' # or it can be queryset.model._meta.verbose_name_plural
    data = '{"total": %s, "%s": %s}' % (queryset.count(), root_name, serializers.serialize('json', queryset))
    return HttpResponse(data, mimetype='text/javascript;') 
