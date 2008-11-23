#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from django.conf.urls.defaults import patterns

urlpatterns = patterns('multipleform.views',
     (r'twoforms/$','two_forms'),
     (r'samenameforms/$','samename_forms'),
)

