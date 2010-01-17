#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns("",
     url(r'ficha/^(?P<slug>[\w-]+)/$', views.ficha_evento, name='ficha-evento'),
)
