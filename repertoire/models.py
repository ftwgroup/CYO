from django.db import models

from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent
from feincms.content.medialibrary.v2 import MediaFileContent

Page.register_extensions('datepublisher', 'navigation', 'seo', 'titles')

Page.register_templates({
    'title': _(''),
    'path': '',
    'regions': (

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

