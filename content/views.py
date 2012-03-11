# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from feincms.module.page.models import Page

def page_not_found(request, template_name='404.html'):
    page = Page.objects.best_match_for_request(request)
    return render_to_response(template_name, {'feincms_page' : page}, context_instance=RequestContext(request))
