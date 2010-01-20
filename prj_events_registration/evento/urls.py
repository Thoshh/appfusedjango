#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns("",
     url(r'mis-inscripciones/$', views.mis_inscripciones, name='mis-inscripciones'),
     url(r'ficha/(?P<slug>[\w-]+)/$', views.ficha_evento, name='ficha-evento'),
     url(r'inscribirse/(?P<slug>[\w-]+)/$', views.inscribirse, name='inscribirse'),                      
     url(r'inscripcion-realizada/(?P<slug>[\w-]+)/$', views.inscripcion_realizada, name='inscripcion-realizada'),
     url(r'cancela/(?P<slug>[\w-]+)/$', views.cancela_inscripcion, name='cancela-inscripcion'),
     url(r'inscripcion-cancelada/(?P<slug>[\w-]+)/$', views.inscripcion_cancelada, name='inscripcion-cancelada'),

)
