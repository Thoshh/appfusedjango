#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from models import CustomerForm

def index(request):
    data = {'form': CustomerForm()}
    return  render_to_response('index.html',data, context_instance=RequestContext(request))
