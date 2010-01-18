#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns("",
     url(r'ficha/(?P<slug>[\w-]+)/$', views.ficha_evento, name='ficha-evento'),
     url(r'inscribirse/(?P<slug>[\w-]+)/$', views.inscribirse, name='inscribirse'),                      
     url(r'inscripcion/(?P<evento>[\w-]+)/$', views.inscripcion_realizada, name='inscripcion-realizada'),
)
