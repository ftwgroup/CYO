from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView
from feincms.module.page.models import Page
from feincms.views.generic import *
from django.views.generic import TemplateView
from feincms.templatetags.feincms_thumbnail import thumbnail
from whoosh.qparser.default import QueryParser
import cyo
import content

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

def search(request):
    query = request.GET["q"]
    query_parser = QueryParser("content", schema=cyo.SiteSchema).parse(query)
    with (cyo.SiteSchema).searcher() as s:
        results = s.search(query_parser, limit=20)
    if len(results) > 0:
        max_score = max([r.score for r in results])
        max_rank = max([r.fields()["rank"] for r in results])
        polished_results = []
        for r in results:
            fields = r.fields()
            r.score = r.score/max_score
            r.rank = fields["rank"]/max_rank
            r.polished_results = r.score+r.rank
            polished_results.append(r)
            polished_results.sort(key=lambda x: x.polished_results, reverse=True)
    else:
        polished_results = []
    return render_to_response("results.html", {"q":query, "results":polished_results})
