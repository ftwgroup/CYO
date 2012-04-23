from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from feincms.content.application.models import ApplicationContent
from feincms.module.page.models import Page
from feincms.module.page.sitemap import PageSitemap
from django.contrib import admin
from django.views.generic.simple import redirect_to


admin.autodiscover()

sitemaps = {'pages' : PageSitemap}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyo.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^audition/', include('auditions.urls')),
    url(r'^repertoire/', include('repertoire.urls')),
    url(r'^concert/$', redirect_to, {'url' : '/concerts/'}),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
            {'sitemaps': sitemaps}),
    url(r'^', include('feincms.urls')),
)
handler404 = 'content.views.page_not_found'

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )