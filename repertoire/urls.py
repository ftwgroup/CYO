from django.conf.urls.defaults import patterns, include, url
from repertoire.views import RepertoireView, SongView, ComposerView, ConcertView

urlpatterns = patterns('',
    url(r'concert/^$', ConcertView.as_view(), {'filter':'arranger'}, name='arranger-view'),
    url(r'composer/^$', ComposerView.as_view(), {'filter':'arranger'}, name='arranger-view'),
    #TODO Performer View
    url(r'song/(?P<songname>[a-zA-Z0-9_.-]+)/$', SongView.as_view()),

    url(r'arranger$', RepertoireView.as_view(), {'filter':'arranger'}, name='arranger-sort'),
    url(r'composer$', RepertoireView.as_view(), {'filter':'composer'}, name='composer-sort'),
    url(r'guest$', RepertoireView.as_view(), {'filter':'guest'}, name='guest-sort'),
    url(r'soloist$', RepertoireView.as_view(), {'filter':'soloist'}, name='soloist-sort'),
    url(r'song$', RepertoireView.as_view(), {'filter':'song'}, name='song-sort'),
    url(r'premiere$', RepertoireView.as_view(), {'filter':'premiere'}, name='premiere-sort'),
    url(r'$', RepertoireView.as_view(), name="default-sort"),
    )