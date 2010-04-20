#!/usr/bin/env python
#-*- coding: UTF-8 -*-

"""This example shows how can you use the admin widget
in your forms"""

from django import forms
from django.contrib.admin import widgets
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

class DateForm(forms.Form):
    """Sample date form with admin widgets"""
    fecha = forms.DateField(input_formats=['%d-%m-%Y'],
                            widget=widgets.AdminDateWidget)
    hora = forms.TimeField(widget=widgets.AdminTimeWidget)
    instante = forms.DateTimeField(
            input_formats=['%d-%m-%Y %H:%M'],
            widget=widgets.AdminSplitDateTime)

def index(request):
    data = {}
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            #process and redirect
            return redirect('thanks')
    else:
        form = DateForm()
    data['form'] = form
    return render_to_response('index.html', data, context_instance=RequestContext(request))


