from django.conf.urls.defaults import *
from django.conf import settings 
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     # our agenda application
     (r'^$','agenda.views.index'),
     (r'^agenda/', include('agenda.urls')),
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


