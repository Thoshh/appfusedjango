#/usr/bin/env python
# -*- coding: UTF-8 -*-


from agenda.models import Person

# ext+json+jqrid
from django.http import HttpResponse 
from django.core import serializers 
# settings
from django.conf import settings
from django.db import connection


RECORDS_PER_PAGE=2
VISIBLE_PAGES=3


# How to usue jqGrid. First version
# ---------------------------------

def jqfilter(op,field):
    """We need to make the conversion from the search parameters that
    jqgrid sends and the sql ones.
    I you send a non existing codintion it would apply the equal one"""

    jqgrid = {'bw': ("%s like %%s", "%s%%"  ),
              'eq': ("%s = %%s",    "%s"    ),
              'gt': ("%s > %%s",    "%s"    ),
              'ge': ("%s >= %%s",   "%s"    ),
              'ne': ("%s <> %%s",   "%s"    ),
              'lt': ("%s < %%s",    "%s"    ),
              'le': ("%s <= %%s",   "%s"    ),
              'ew': ("%s like %%s", "%%%s"  ),
              'cn': ("%s like %%s", "%%%s%%")
              }
    try:
        condition, template = jqgrid[op]
    except:
        condition, template = jqgrid['eq']
    return condition % field, template

def ajax_dades(request):
    """Ajax needed by  jqgrid. This is not generic nor the best code you can have 
    but for teaching purposes I prefer to sacrifice style.   
    
    This code takes a python object, Person in our case and deals with pagination,
    and filters as is sent by jqGrid.
    
    """

    orden = "id" if (request.GET.get('sidx')=="" or None) else request.GET.get('sidx') 
    sort_order = "" if request.GET.get('sord') == "asc" else "-"
    orden = sort_order+orden
    pagina = int(request.GET.get('page')) if request.GET.get('page') != 'page' else 1 
    files = int(request.GET.get('rows'))  # files = rows in catalan :)
    
    # Here goes the model.--
    dades = Person.objects
    # ----------------------
    
    # We compute what we are going to present in the grid

    if request.GET.get('_search')=='true':
        # We're on searching mode
        searchField = request.GET.get('searchField')
        searchOp = request.GET.get('searchOper')
        field, template = jqfilter(searchOp, searchField)
        fields = [ field ]
        values = [ template  % request.GET.get('searchString')]
        try:
            total = dades.all().extra(where=fields, params = values).count()
            rta = dades.all().extra(where=fields, params = values)
        except Exception, e:
            print e
            data = '{"total":%(pages)s, "page":%(page)s, "records":%(total)s, "rows":%(rta)s }'\
                % {'pages':0, 'page':0, 'total':0, 'rta':None}
            return HttpResponse(data, mimetype="application/json")
    else:
        # Normal mode, so no filters applied
        rta = dades.all()
        total = dades.all().count() 
    
    # Page calculation
    reste = 1 if total % files >0 else 0
    pages = total / files  + reste
    if pagina > pages:
        pagina = 1

    # Get just the data we needo for our page
    rta = rta.order_by(orden)[(pagina-1)*files:pagina*files]

    #just for debug purposes
    if settings.DEBUG:
        print 
        print "QUERY ====================================="
        print connection.queries
        print "==========================================="
        print

    # We build the json that jqgrid likes best :)
    rows = serializers.serialize("json",rta)
    dades = '{"total":%(pages)s, "page":%(page)s, "records":%(total)s, "rows":%(rta)s }' % {'pages':pages, 'page':pagina, 'total':total, 'rta':rows}
    return HttpResponse(dades, mimetype='application/json')
 
