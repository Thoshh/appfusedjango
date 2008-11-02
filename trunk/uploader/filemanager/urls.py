#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('filemanager.views',
    (r'^list/$', 'list'),
    ('^attach/$','attach'),
)

#additional patterns here
#urlpatterns +=  patterns('base',
#    (re, view function),
#)