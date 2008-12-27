#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from django.conf.urls.defaults import patterns, url
from agenda import views as agenda_views

urlpatterns = patterns("",
     url(r'^$', agenda_views.index, name='agenda-index'),
     url(r'^list/page/(?P<page>\d+)/(.*)$', agenda_views.index, name="agenda-list"),
     url(r'^ficha/(?P<accion>\w+)/(?P<id>\d+)/$', agenda_views.ficha, name="agenda-ficha"),
     url(r'^edit/(?P<id>\d+)/$', agenda_views.edit, name="agenda-edit"),
     url(r'^add/$', agenda_views.edit, name="agenda-add"),
     url(r'^delete/(?P<id>\d+)/$', agenda_views.delete, name="agenda-delete"),
     url(r'^deleted/$', agenda_views.deleted, name="agenda-deleted-record"),
     url(r'^lang/(?P<idioma>\w+)/$', agenda_views.cambiar_idioma, name ="change-language"),
)

if __name__ == "__main__":
    pass
