#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('chivato.views',
    (r'^list/$', 'list'),
)