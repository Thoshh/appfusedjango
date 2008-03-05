from django.conf.urls.defaults import *
from django.conf import settings 
urlpatterns = patterns('',
     # our agenda application
     (r'^$','agenda.views.index'),
     (r'^agenda/', include('agenda.urls')),
     # Then admin
     (r'^admin/', include('django.contrib.admin.urls')),
    )


# We're going to use the Django server in development, so we'll server
# also the estatic content.
if settings.DEBUG:
	urlpatterns += patterns('',
       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
    )


