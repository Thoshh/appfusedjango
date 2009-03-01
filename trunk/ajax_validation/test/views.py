#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# --------------------------------------------------------------------
# Propósito: Test ajax validation
#---------------------------------------------------------------------

from formularis import ContactForm, validate
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def index(request):
    redirect_url = '/thanks'
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if request.is_ajax():
            return validate(request, contact_form, redirect_url)
        else:
            if contact_form.is_valid():
            # do whatever you need as everything is valid
                return HttpResponseRedirect(redirect_url)
    else:
        contact_form = ContactForm()            
    return render_to_response('index.html', {'form': contact_form})


