#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: your-name-here
# --------------------------------------------------------------------

from django.conf.urls.defaults import *
from django.conf import settings 
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
     # direct to template sample
     url(r'^$','sample.views.index', name="main-page"),
     url(r'^display/(?P<id>\d+)/$','sample.views.display', name="display-image"),
     # application url include
     #(r'^app/', include('app.urls')),
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


