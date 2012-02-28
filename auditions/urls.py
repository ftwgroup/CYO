from django.conf.urls.defaults import patterns, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'signup/$', 'auditions.views.signup', name='signup'),
    url(r'success/$', TemplateView.as_view(template_name='success.html'), name='success'),
)