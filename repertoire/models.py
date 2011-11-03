from django.contrib.localflavor import us
from django.db import models

from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent
from feincms.content.medialibrary.v2 import MediaFileContent

Page.register_extensions('datepublisher', 'navigation', 'seo', 'titles')

Page.register_templates({
    'title': _('Upcoming'),
    'path': 'piece.html',
    'regions': (
        ('yellow_overview', _('Overview')),
        ('white_details', _('Details')),
        ('black_sidebar', _('Sidebar')),
    ),
})

Page.create_content_type(RichTextContent)
Page.create_content_type(ImageContent, POSITION_CHOICES=(
    ('block', _('block')),
    #TODO (Ipsheeta) define position choices
))
Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('lightbox', _('lightbox')),
    #TODO (Ipsheeta) define type choices
))

#TODO (Ipsheeta) read http://www.feinheit.ch/media/labs/feincms/contenttypes.html#design-considerations-for-content-types

class ConcertInfo(models.Model):
    date_time = models.DateTimeField('Date and Time')
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = us.models.USStateField(blank=True, null=True)
    zipcode = us.models.USPostalCodeField(blank=True, null=True)

    title = models.CharField()

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return