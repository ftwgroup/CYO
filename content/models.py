from django.contrib import admin
from django.contrib.localflavor import us
from django.contrib.localflavor.us.models import USStateField, USPostalCodeField

from django.db import models
from django.template.loader import render_to_string

from django import forms

from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent
from feincms.content.medialibrary.v2 import MediaFileContent

import os.path

Page.register_extensions('datepublisher', 'navigation', 'seo', 'titles')

Page.register_templates(
        {
        'title': _('Concert Page'),
        'path': 'concert_page.html',
        'regions': (
            ('upcoming', _('Upcoming')),
            ('content', _('Content')),
            ('black_sidebar', _('Sidebar'), 'inherited'),
            ),
        },
        {
        'title': _('Article Page'),
        'path': 'article.html',
        'regions': (
            ('content', _('Content')),
            ('sidebar', _('Side Bar'),)
            ),
        },
        {
        'title': _('Homepage'),
        'path': 'home.html',
        'regions': (
            ('homepage_content', _('Homepage Content')),
            ('sidebar', _('Side Bar'),)
        ),
        },
        {
        'title': _('Bio Page'),
        'path': 'bio_page.html',
        'regions': (
            ('content', _('Content')),
            ('sidebar', _('Sidebar'), 'inherited'),
            ),
        }
)

Page.create_content_type(RichTextContent)

Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('ArticleImage', _('Article Image')),
    #TODO (Ipsheeta) define type choices
))

class ConcertDetails(models.Model):
    location = models.TextField()
    concert_datetime = models.DateTimeField()
    concert_ticket_url = models.URLField()

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/concert_detail.html', {'concert': self})

