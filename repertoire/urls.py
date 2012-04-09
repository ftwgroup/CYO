from django.conf.urls.defaults import patterns, include, url
from repertoire.views import RepertoireView

urlpatterns = patterns('',
    url(r'arranger$', RepertoireView.as_view(), {'filter':'arranger'}, name='arranger-view'),
    url(r'composer$', RepertoireView.as_view(), {'filter':'composer'}, name='composer-view'),
    url(r'guest$', RepertoireView.as_view(), {'filter':'guest'}, name='guest-view'),
    url(r'soloist$', RepertoireView.as_view(), {'filter':'soloist'}, name='soloist-view'),
    url(r'song$', RepertoireView.as_view(), {'filter':'song'}, name='song-view'),
    url(r'premiere$', RepertoireView.as_view(), {'filter':'premiere'}, name='premiere-view'),
    url(r'$', RepertoireView.as_view(), name="default-view"),
    )