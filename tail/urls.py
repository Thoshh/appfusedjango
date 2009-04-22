#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: your-name-here
# --------------------------------------------------------------------

from django.conf.urls.defaults import *
from django.conf import settings 
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
     # direct to template sample
     (r'^$',direct_to_template, {'template': 'index.html'}),
     # application url include
     (r'^log/', include('dlog.urls')),
     # Administration
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     (r'^admin/(.*)', admin.site.root),
    )


# We're going to use the Django server in development, so we'll server
# also the estatic content.
if settings.DEBUG:
	urlpatterns += patterns('',
       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
    )


