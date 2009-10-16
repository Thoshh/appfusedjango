#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.http import HttpResponseRedirect
from django.conf import settings
import os

def envia(request):
    for f in request.FILES.getlist('arx'):
        handle_uploaded_file(f)
    return HttpResponseRedirect('/bulk/')

def multi(request):
    for f in request.FILES.getlist('arx'):
        handle_uploaded_file(f)
    return HttpResponseRedirect('/multi/')

def handle_uploaded_file(f):
    """Simple file manager. It gets the name of
    the file and writes it into the folder we have configured in the settings"""
    path=os.path.join(settings.UPLOAD_FOLDER, f.name)
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
