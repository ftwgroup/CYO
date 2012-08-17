from django.conf.urls.defaults import patterns
from content.views import BecomeADonor, BecomeASponsor, ProgramAds

urlpatterns = patterns('',
    (r'^become-a-donor/', BecomeADonor.as_view()),
    (r'^become-a-sponsor/', BecomeASponsor.as_view()),
    (r'^buy-program-ads/', ProgramAds.as_view()),
    )