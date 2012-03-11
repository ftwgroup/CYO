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
from string import maketrans

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
        'title': 'Bio Page',
        'path': 'bio_page.html',
        'regions': (
            ('content', 'Content'),
            ('images', 'Bio Images'),
            ('sidebar', '(Bio) Sidebar Sections', 'inherited'),
            ),
        },
        {
        'title': 'Concert Page',
        'path': 'concert_info.html',
        'regions': (
            ('concert_details', 'Concert Details', 'inherited'),
            ('concert_abstract', 'Concert Abstract'),
            ('content', 'Content'),
            ('concert_sidebar', '(Series) Side bar Sections', 'inherited'),
            ),
        },
        {
        'title': 'Concert Archive Page',
        'path': 'concert_archive.html',
        'regions': (
            ('concert_details', 'Concert Details', 'inherited'),
            ('concert_abstract', 'Concert Abstract', 'inherited'),
            ('content', 'Content'),
            ('archive_detail_table', 'Series Archive Table', 'inherited'),
            ('concert_sidebar', '(Series) Side bar Sections', 'inherited'),
            ),
        },
        {
        'title': 'Homepage',
        'path': 'home.html',
        'regions': (
            ('rotator_images', 'Rotator Images'),
            ('homepage_content', 'Homepage Content'),
            ('sidebar', '(Home) Side Bar Sections')
           ),
        },
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
    #concert_abstract_text = models.TextField()
    featured_artist_name = models.CharField(max_length=32)
    featured_artist_role = models.CharField(max_length=32)

    #def concert_dow(self):
    #    obj = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Sunday'}
    #    return (obj[dow] for dow in (self).concert_datetime.weekday)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/concert_detail.html', {'concertdetails': self})

class ConcertArchiveDetails(models.Model):
    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/concert_archive_detail.html', {'archived_concert': self})

Page.create_content_type(ConcertDetails)
Page.create_content_type(ConcertArchiveDetails)