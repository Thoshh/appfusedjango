#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: your-name-here
# --------------------------------------------------------------------

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

js_info_dict = {
    'packages': ('example','django.contrib.admin',),
}

urlpatterns = patterns('',
     # direct to template sample
     url(r'^$', 'example.views.index', name='index'),
     url(r'^thanks/$',direct_to_template, {'template': 'thanks.html'}, name='thanks'),
     # application url include
     #(r'^app/', include('app.urls')),
     # Administration
   )

urlpatterns += patterns('',
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
)

urlpatterns += patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),  )

# We're going to use the Django server in development, so we'll server
# also the estatic content.
if settings.DEBUG:
	urlpatterns += patterns('',
       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
    )


