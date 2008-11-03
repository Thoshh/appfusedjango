#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy

from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Eliminat, in_view
import chivato

def list(request):
    "Lists the deleted users"
    deleted = Eliminat.objects.all()
    in_view.send(sender=chivato.views.list, ip=request.META['REMOTE_ADDR'],
        name=request.get_full_path())
    return render_to_response('list.html', {'deleted':deleted})