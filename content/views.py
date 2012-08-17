from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView
from feincms.module.page.models import Page
from feincms.views.generic import *
from django.views.generic import TemplateView

#def show_featured_box(request,template_name='featured_box.html'):
#    box = content.models.FeaturedBoxContent
#    return render_to_response(template_name, {'featured_box' : box}, context_instance=RequestContext(request))

#STATIC VIEWS
class ProgramAds(TemplateView):
    template_name="special/program_ads.html"

class BecomeASponsor(TemplateView):
    template_name="special/become_a_sponsor.html"

class BecomeADonor(TemplateView):
    template_name="special/become_a_donor.html"

def page_not_found(request, template_name='404.html'):
    page = Page.objects.best_match_for_request(request)
    return render_to_response(template_name, {'feincms_page' : page}, context_instance=RequestContext(request))
