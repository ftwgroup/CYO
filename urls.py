from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from repertoire import models
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyo.views.home', name='home'),
    # url(r'^cyo/', include('cyo.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('feincms.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
