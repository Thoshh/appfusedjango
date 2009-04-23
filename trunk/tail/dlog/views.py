#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# --------------------------------------------------------------------
#

from django.http import HttpResponse
from django.utils import simplejson


def _tail(f, actual = 0):
    """
    Returns a tuple with the actual position on the file
    and the last read lines in html format.
    """
    text =""
    if actual == 0:
        f.seek(0, 2)
    else:
        f.seek(actual)
        log = f.readlines()
        if log:
            log.reverse()
            text = "<br/>".join(log)
    return f.tell(), text
    

def tail(request):
    "Tail simulation"
    f = open('sample.log', 'rU')
    pos = int(request.GET['pos'])
    pos, msg =  _tail(f, actual= pos )
    f.close()
    data = {'msg': msg,
            'pos' : pos
           }    
    return HttpResponse(simplejson.dumps(data))

