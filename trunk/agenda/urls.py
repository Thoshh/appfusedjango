#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from django.conf.urls.defaults import patterns

urlpatterns = patterns('agenda.views',
     (r'^$', 'index'),
     (r'^list/page/(?P<page>\w+)/$','index'),
     (r'^ficha/(?P<accion>\w+)/(?P<id>\d+)/$','ficha'),
     (r'^edit/(?P<id>\d+)/$','edit'),
     (r'^add/$','edit'),
     (r'^delete/(?P<id>\d+)/$','delete'),
     (r'^deleted/$','deleted'),
     (r'^lang/(?P<idioma>\w+)/$','cambiar_idioma'),
     # extjs based agenda
     (r'^tabla/$','grid_view'),
     # json
     (r'json/list/$','json_list'),
)




if __name__ == "__main__":
    pass
