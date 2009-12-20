#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns("log.views",
    url(r'^$', 'index', name='main-log'),
    url(r'^time/([-+]{0,1}\d)*$', 'current_time', name='curent_time'),
)
