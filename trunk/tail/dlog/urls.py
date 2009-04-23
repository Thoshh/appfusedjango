#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from django.conf.urls.defaults import patterns

urlpatterns = patterns('dlog.views',
     (r'^tail/$', 'tail'),
)

