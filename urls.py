from django.conf.urls.defaults import *
import settings
from django.contrib import admin
from views import HomeView
admin.autodiscover()

urlpatterns = patterns('',
    (r'^rss/$','views.rss'),
    (r'^$',HomeView.homepage),
    (r'^data/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^daily/', include('daily.urls')),
    (r'^feedback/', include('feedback.urls')),
    (r'^about/$',HomeView.about),
    (r'^admin/(.*)', admin.site.root),
    
    # Example:
    # (r'^whhhy/', include('whhhy.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
