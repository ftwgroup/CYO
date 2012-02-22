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
        'title': 'Generic Page',
        'path': 'generic.html',
        'regions': (
            ('content', 'Content'),
            ('sidebar', 'Side Bar', 'inherited')
            ),
        },
        {
        'title': 'Concert Page',
        'path': 'concert_page.html',
        'regions': (
            ('concert_details', 'Concert Details'),
            ('concert_abstract', 'Concert Abstract'),
            ('content', 'Content'),
            ('concert_sidebar', 'Series Side bar', 'inherited'),
            ),
        },
        {
        'title': 'Concert Archive Page',
        'path': 'concert_archive_page.html',
        'regions': (
            ('content', 'Content'),
            ('archive', 'Series Archive', 'inherited'),
            ('concert_sidebar', 'Series Side bar', 'inherited'),
            ),
        },
        {
        'title': 'Homepage',
        'path': 'home.html',
        'regions': (
            ('homepage_content', 'Homepage Content'),
            ('sidebar', 'Side Bar')
        ),
        },
        {
        'title': 'Bio Page',
        'path': 'bio_page.html',
        'regions': (
            ('content', 'Content'),
            ('sidebar', 'Sidebar', 'inherited'),
            ),
        }
)

Page.create_content_type(RichTextContent)

Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('ArticleImage', 'Article Image'),
    ('ConcertThumbnail', 'Concert Poster Image'),
    #TODO (Ipsheeta) define type choices
))

# TODO (julian) depending on how future conversations with CYO goes, we may refactor


class ConcertDetails(models.Model):
    location = models.TextField()
    concert_datetime = models.DateTimeField()
    concert_ticket_url = models.URLField()
    featured_artist_name = models.CharField(max_length=32)
    featured_artist_role = models.CharField(max_length=32)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/concert_detail.html', {'concert': self})

class ConcertArchiveDetails(models.Model):
    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/concert_archive_detail.html', {'archived_concert': self})

Page.create_content_type(ConcertDetails)
Page.create_content_type(ConcertArchiveDetails)