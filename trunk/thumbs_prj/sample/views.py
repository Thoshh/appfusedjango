#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# --------------------------------------------------------------------
# Propósito:
#---------------------------------------------------------------------

from models import Photo
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import AttachmentForm


def index(request):
    "Obtains the attachment and saves it to the disk"
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            import ipdb; ipdb.set_trace()
            f = form.cleaned_data['image']
            foto = Photo()
            foto.image.save(f.name, f)
            foto.comments = form.cleaned_data['comments']
            foto.save()
            return HttpResponseRedirect('/')
    else:
        form = AttachmentForm()
    fotos = Photo.objects.all()
    return render_to_response('index.html', {'form':form, 'fotos': fotos})

def display(request, id):
    foto = Photo.objects.get(pk=id)
    return render_to_response('image.html', {'foto': foto})
    


