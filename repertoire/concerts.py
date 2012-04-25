from django.conf.urls.defaults import patterns, include, url
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from feincms.views.generic.list_detail import object_list
from repertoire.models import Concert
from django.shortcuts import get_object_or_404

"""
This file handles extending the repertoire to handle the connection from Repertoire models into FeinCMS pages.
"""


"""
Creating concert views from repertoire models here

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
    View details for a particular season of a particular series.
    """
    context_object_name = 'concert'
    template_name = 'concert_in_series.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            # Store series-slug and season for the get_object() call
            self.slug = kwargs.get('slug', None)
            self.season = int(kwargs.get('season', 0))
        except:
            raise Http404(u"Invalid ConcertInSeriesView arguments: kwargs = %s" % repr(kwargs))
        return super(ConcertInSeriesView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        """
        Return the concert for the specified season of the specified series.
        """
        try:
            obj =  Concert.objects.get(series__slug=self.slug, season=self.season)
        except ObjectDoesNotExist:
            raise Http404(u"No concerts found matching slug='%s', season=%d" % (self.slug,self.season))
        except MultipleObjectsReturned:
            raise Http404(u"Multiple concerts matching slug='%s', season=%d" % (self.slug,self.season))
        return obj

    def get_context_data(self, **kwargs):
        context = super(ConcertInSeriesView, self).get_context_data(**kwargs)
        # Attach the next upcoming concert to the default context object
        context['upcoming'] = Concert.objects.filter(series__slug=self.slug).latest('date_time')
        return context


class ConcertArchiveView(ListView):
    """
    View all concerts for a particular series, ordered by date_time field.
    """
    template_name = 'concert_archive.html'

    def dispatch(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug', '')
        return super(ConcertArchiveView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Concert.objects.filter(series__slug=self.slug).order_by('-season')


"""
Setting URL patterns here.

We want to connect a url-input with the objects that we are using in the templates filtered by
the series name.

"""
urlpatterns = patterns('',
    # Concert series, identified by slug.  The url will look like
    #   http://cyorchestra.org/concert/series/new-works
    url(r'series/(?P<slug>[-\w]+)/$', ConcertArchiveView.as_view(), name='concert-archive'),

    # Concert series archive pages.  The url will look like
    #   http://cyorchestra.org/concert/series/new-works/season
    # This view shows the upcoming concert on top and concert details per season below.
    url(r'series/(?P<slug>[-\w]+)/(?P<season>\d+)/$', ConcertInSeriesView.as_view(), name='concert-in-series'),

    # Generic concert details page.
    #   http://cyorchestra.org/concert/id
    url(r'(?P<pk>\d+)/$', ConcertDetailView.as_view(), name='concert-detail'),
)
