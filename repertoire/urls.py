from django.conf.urls.defaults import patterns, include, url
from django.views.generic.detail import DetailView
from repertoire.views import RepertoireView
from repertoire.models import *

urlpatterns = patterns('',
    url(r'arranger$', RepertoireView.as_view(), {'filter':'arranger'}, name='by-arranger'),
    url(r'composer$', RepertoireView.as_view(), {'filter':'composer'}, name='by-composer'),
    url(r'guest$', RepertoireView.as_view(), {'filter':'guest'}, name='by-guest'),
    url(r'soloist$', RepertoireView.as_view(), {'filter':'soloist'}, name='by-soloist'),
    url(r'song$', RepertoireView.as_view(), {'filter':'song'}, name='by-song'),
    url(r'premiere$', RepertoireView.as_view(), {'filter':'premiere'}, name='by-premiere'),

    #handle individual details per item in repertoire
    url(r'concert/(?P<pk>\d+)/$', DetailView.as_view(model=Concert), name='concert-detail'),
    url(r'performer/(?P<pk>\d+)/$', DetailView.as_view(model=Performer), name='performer-detail'),
    url(r'venue/(?P<pk>\d+)/$', DetailView.as_view(model=Venue), name='venue-detail'),
    #TODO maybe - queryset for all the concerts each song is in so that can be displayed in the view as well
    url(r'song/(?P<pk>\d+)/$', DetailView.as_view(model=Song), name='song-detail'),
    url(r'season/(?P<pk>\d+)/$', DetailView.as_view(), name='season-detail'),
    url(r'series/(?P<pk>\d+)/$', DetailView.as_view(model=Series), name='series-detail'),
    url(r'$', RepertoireView.as_view(), name='by-default'),
)