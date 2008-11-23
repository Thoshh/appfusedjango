#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# --------------------------------------------------------------------
# Propósito: Show multiple forms
#---------------------------------------------------------------------
__author__="aaloy"
__date__ ="$23/11/2008 17:56:26$"

from multipleform.formularis import LoginForm
from multipleform.formularis import ContactForm
from multipleform.formularis import InfoForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def two_forms(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        login_form = LoginForm(request.POST)        
        if  login_form.is_valid() and contact_form.is_valid():
            # do whatever you need as everything is valid
            return HttpResponseRedirect('/thanks/')
    else:
        contact_form = ContactForm()
        login_form = LoginForm()
    forms = [contact_form, login_form]
    return render_to_response('two_forms.html', {'forms': forms})

def samename_forms(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        login_form = LoginForm(request.POST)
        info_form = InfoForm(request.POST, prefix="info")
        import ipdb; ipdb.set_trace()
        if  login_form.is_valid() and contact_form.is_valid() and info_form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        contact_form = ContactForm()
        login_form = LoginForm()
        info_form = InfoForm(prefix="info")
    forms = [contact_form, login_form, info_form]
    return render_to_response('same_forms.html', {'forms': forms})
