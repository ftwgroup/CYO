from django.conf.urls.defaults import patterns, include, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from feincms.views.generic.list_detail import object_list
from repertoire.models import Concert
from django.shortcuts import get_object_or_404

"""
This file handles extending the repertoire to handle the connection from Concert objects from
the repertoire with the FeinCMS pages app.
"""


"""
Creating views here

"""

class ConcertDetailView(DetailView):
    """
    This class was created to display a concert details page
    """
    model = Concert
    context_object_name = 'concert'
    template_name = 'concert_detail.html'


"""
Setting URL patterns here.

We want to connect a url-input with the objects that we are using in the templates filtered by
the series name.

"""
urlpatterns = patterns('',
    # concert series - the url will look like this http://cyorchestra.org/concert/new-works
    # by default, these views show archive view using.
    # views are set to show objects filtered by series title and then ordered by date_time
    # may have to refactor to get url and then pass into filter to account for series other than the main three

    url(r'new-works/$', ListView.as_view(queryset=Concert.objects.filter(series__title="New Works").order_by('-season'), template_name='concert_archive.html'),
        name='new-works'),
    url(r'rock-the-orchestra/$', ListView.as_view(queryset=Concert.objects.filter(series__title="Rock the Orchestra").order_by('-season'), model=Concert, template_name='concert_archive.html'),
        name='rock-the-orchestra'),
    url(r'music-and-its-industry/$', ListView.as_view(queryset=Concert.objects.filter(series__title="Music and Its Industry").order_by('-season'), model=Concert, template_name='concert_archive.html'),
        name='music-and-its-industry'),

    # concert series archive pages- the url will look like this http://cyorchestra.org/concert/new-works/id
    # this view shows upcoming on top and concert details per season on the bottom.
    url(r'(?P<pk>\d+)/$', ConcertDetailView.as_view(), name='concert-detail'),
)
