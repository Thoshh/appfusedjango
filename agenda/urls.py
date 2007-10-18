#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
from django.conf.urls.defaults import *

urlpatterns = patterns('agenda.views',
    # Example:
     (r'^$', 'index'),
     (r'^list/page/(?P<page>\w+)/$','index'),
     (r'^ficha/(?P<accion>\w+)/(?P<id>\d+)/$','ficha'),
     (r'^edit/(?P<id>\d+)/$','edit'),
     (r'^add/$','edit'),
    # Uncomment this for admin:
)




if __name__ == "__main__":
    pass
