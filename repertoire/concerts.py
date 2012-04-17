from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list import ListView
from repertoire.models import Concert

urlpatterns = patterns('',
# concert series
url(r'new-works/$', ListView.as_view(model=Concert, template_name='concert_archive.html'), name='new-works'),
url(r'rock-the-orchestra/$', ListView.as_view(model=Concert, template_name='concert_archive.html'), name='rock-the-orchestra'),
url(r'music-and-its-industry/$', ListView.as_view(model=Concert, template_name='concert_archive.html'), name='music-and-its-industry'),
)