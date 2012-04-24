from django.conf.urls.defaults import patterns, include, url
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
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


class ConcertInSeriesView(DetailView):
    """
    View details for a particular season of a particular concert series.
    """
    context_object_name = 'concert'
    template_name = 'concert_in_series.html'

    def dispatch(self, request, *args, **kwargs):
        # TODO (jordan): error checking
        self.series = kwargs.get('series', None)
        self.season = int(kwargs.get('season', 0))
        return super(ConcertInSeriesView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Return the concert for the specified season of the specified series.
        """
        try:
            obj =  Concert.objects.get(series__title=self.series, season=self.season)
        except ObjectDoesNotExist:
            raise Http404(u"No concerts found matching the query")
        return obj

    def get_context_data(self, **kwargs):
        # Get default context object
        context = super(ConcertInSeriesView, self).get_context_data(**kwargs)
        # Attach the next upcoming concert to the context object
        context['upcoming_in_series'] =\
            Concert.objects.filter(series__title=self.series).latest('date_time')
        return context


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

    # View concert details within a specific series
    url(r'new-works/(?P<season>\d+)/$',
        ConcertInSeriesView.as_view(),
        {'series': 'New Works'},
        name='new-works-detail'),
    url(r'rock-the-orchestra/(?P<season>\d+)/$',
        ConcertInSeriesView.as_view(),
        {'series': 'Rock the Orchestra'},
        name='rock-the-orchestra-detail'),
    url(r'music-and-its-industry/(?P<season>\d+)/$',
        ConcertInSeriesView.as_view(),
        {'series': 'Music and Its Industry'},
        name='music-and-its-industry-detail'),

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
