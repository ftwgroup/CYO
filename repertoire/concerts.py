from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list import ListView
from feincms.views.generic.list_detail import object_list
from repertoire.models import Concert
from django.shortcuts import get_object_or_404

"""
This file handles extending the repertoire to handle the connection from Concert objects from
the repertoire with the FeinCMS pages app.
"""


"""
Setting URL patterns here.

We want to connect a url-input with the objects that we are using in the templates filtered by
the series name.

"""
urlpatterns = patterns('',
    # concert series
    url(r'new-works/$', ListView.as_view(queryset=Concert.objects.filter(series__title="New Works").order_by('-rough_date','date_time'), template_name='concert_archive.html'),
        name='new-works'),
    url(r'rock-the-orchestra/$', ListView.as_view(queryset=Concert.objects.filter(series__title="Rock the Orchestra"), model=Concert, template_name='concert_archive.html'),
        name='rock-the-orchestra'),
    url(r'music-and-its-industry/$', ListView.as_view(queryset=Concert.objects.filter(series__title="Music and Its Industry"), model=Concert, template_name='concert_archive.html'),
        name='music-and-its-industry'),
)

"""
Creating views here

We may want to do detail views here.
"""
