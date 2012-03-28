from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from feincms.module.page.sitemap import PageSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

sitemaps = {'pages' : PageSitemap}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyo.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^audition/', include('auditions.urls')),
    url(r'^repertoire/', include('repertoire.urls')),
    url(r'^', include('feincms.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
            {'sitemaps': sitemaps}),

)
handler404 = 'content.views.page_not_found'

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )