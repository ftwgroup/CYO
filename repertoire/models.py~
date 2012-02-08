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

Page.register_templates({
    'title': _('Upcoming'),
    #TODO (ipsheeta) is this going to work on everyone's computer now?
    'path': 'piece.html',
    'regions': (
        ('yellow_overview', _('Overview')),
        ('white_details', _('Details')),
        ('black_sidebar', _('Sidebar'), 'inherited'),
    ),
    },
    {
    'title': _('Home Page'),
    'path': 'home.html',
    'regions': (
        ('main', _('Main Content Area')),
        ('sidebar', _('Side Bar'),)
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


