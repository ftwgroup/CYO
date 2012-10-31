import haystack
haystack.autodiscover()

from haystack import indexes, site, fields
from feincms.module.page.models import Page

class PageIndex(indexes.RealTimeSearchIndex):
    """
    Index for FeinCMS Page objects

    Body is generated using a complex template which includes rendered
content
    for many content objects
    """

    url               = fields.CharField(model_attr="_cached_url")
    text              = fields.CharField(document=True, use_template=True)

    #: Currently included so we can generate search results pages without a
    # database query (Solr will include it the results):
    title             = fields.CharField(model_attr="title")

    def should_update(self, instance, **kwargs):
        return instance.is_active()

    def get_queryset(self):
        """Return a Django QuerySet used for all search-related queries. Currently we index all active pages"""
        return Page.objects.active()

    def get_updated_field(self):
        return "modification_date"

site.register(Page, PageIndex)