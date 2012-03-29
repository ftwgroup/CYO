from django.conf.urls.defaults import patterns, include, url
from repertoire.views import RepertoireView

urlpatterns = patterns('',
    url(r'(?P<filter>composer)/$', RepertoireView.as_view(), name='composer-sort'),
    url(r'pages(?P<page>[0-9]+/$)', RepertoireView.as_view(), name="repertoire-view"),
    url(r'$', RepertoireView.as_view()),
    )