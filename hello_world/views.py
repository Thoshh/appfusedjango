#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', {'msg':'hello world'})
