from django.conf.urls.defaults import patterns, include, url
from repertoire.views import RepertoireView

urlpatterns = patterns('',
    url(r'arranger/$', RepertoireView.as_view(), {'filter':'arranger'}, name='arranger-sort'),
    url(r'composer/$', RepertoireView.as_view(), {'filter':'composer'}, name='composer-sort'),
    url(r'guest/$', RepertoireView.as_view(), {'filter':'guest'}, name='guest-sort'),
    url(r'soloist/$', RepertoireView.as_view(), {'filter':'soloist'}, name='soloist-sort'),
    url(r'song/$', RepertoireView.as_view(), {'filter':'song'}, name='song-sort'),
    url(r'premiere/$', RepertoireView.as_view(), {'filter':'premiere'}, name='premiere-sort'),
    url(r'pages(?P<page>[0-9]+/$)', RepertoireView.as_view(), name="repertoire-view"),
    url(r'$', RepertoireView.as_view()),
    )