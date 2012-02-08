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
            ('yellow_overview', _('Overview')),
            ('white_details', _('Details')),
            ('black_sidebar', _('Sidebar'), 'inherited'),
            ),
        },
        {
        'title': _('Aricle Page'),
        'path': 'article.html',
        'regions': (
            ('content', _('content')),
            ('sidebar', _('Side Bar'),)
            ),
        },
        {
        'title': _('Home Page'),
        'path': 'home.html',
        'regions': (
            ('main', _('Main Content Area')),
            ('sidebar', _('Side Bar'),)
        ),
        },
        {
        'title': _('Bio Page'),
        'path': 'bio_page.html',
        'regions': (
            ('white_details', _('Details')),
            ('black_sidebar', _('Sidebar'), 'inherited'),
            ),
        }
)

Page.create_content_type(RichTextContent)
Page.create_content_type(ImageContent, POSITION_CHOICES=(
    ('block', _('block')),
    #TODO (Ipsheeta) define position choices
))
Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('lightbox', _('lightbox')),
    #TODO (Ipsheeta) define type choices
))


