from django.contrib import admin
from django.contrib.localflavor import us
from django.contrib.localflavor.us.models import USStateField, USPostalCodeField

from django.db import models
from django.db.models.fields.related import ForeignKey
from django.template.loader import render_to_string

from django import forms

from django.utils.translation import ugettext_lazy as _
from feincms.content.application.models import ApplicationContent
from feincms.content.section.models import SectionContent
from feincms.module import page
from feincms.module.medialibrary.fields import MediaFileForeignKey
from feincms.module.medialibrary.models import MediaFile
from feincms.admin.item_editor import FeinCMSInline
from feincms.content.medialibrary.v2 import MediaFileContent, MediaFileContentInline

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent

import os.path
from string import maketrans

Page.register_extensions('datepublisher', 'navigation', 'seo', 'titles')

Page.register_templates(
        {
        'title': 'Homepage',
        'path': 'home.html',
        'regions': (
            ('rotator_images', 'Rotator Images'),
            ('featured_area', 'Featured Area'),
            ('sidebar', '(Home) Side Bar Sections')
            ),
        },
        {
        'title': 'General Content Page',
        'path': 'generic.html',
        'regions': (
            ('content_header', 'Header'),
            #('content_body', 'Body'),
            ('right_column_text', 'Body'),
            ('left_side_image', 'Image Set'),
            ('sidebar', 'Sidebar Sections', 'inherited'),
            ),
        },
        {
        'title': 'Two Text Columns',
        'path': 'two_columns.html',
        'regions': (
            ('content_header', 'Content Header'),
            ('left_column_text', 'Left Column Text'),
            ('right_column_text', 'Right Column Text'),
            ('sidebar', 'Sidebar Sections', 'inherited'),
            ),
        },
        {
        'title': 'Concert/Repertoire Application Page',
        'path': 'repertoire.html',
        'regions': (
            ('content', 'Content Section'),
            ('concert_sidebar', '(Series) Side bar Sections', 'inherited'),
            ),
        },
        {
        'title': 'Placeholder/Forwarding Page',
        'path': 'concert_info.html',
        'regions': (
            ('content', 'NO CONTENT HERE'),
            ),
        },
)

Page.create_content_type(RichTextContent)

Page.create_content_type(SectionContent, TYPE_CHOICES=(
    ('bio', _('Bio Section')),
    ('yellow', _('Yellow Header Section')),
    ))

Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('spread', _('Spread Image')),
    ('leftside', _('Leftside Image')),
    ('concertthumbnail', _('Concert Poster Image')),
    ('downloadable', _('Downloadable Image')),
    ))


Page.create_content_type(ApplicationContent, APPLICATIONS=(
    ('repertoire.concerts', 'Upcoming Concert \+ Archives'),
    ('repertoire.urls', 'Repertoire Application'),
    ('repertoire.featured_boxes', 'Featured Boxes'),
    ))

class ImageInField(FeinCMSInline):
    raw_id_fields = ('poster_thumbnail', 'img', 'section_image')


class FeaturedBoxContent(models.Model):
    """
    One block of the three.
    """
    feincms_item_editor_inline = ImageInField
    series_title = models.CharField(max_length=48)
    series_url = models.CharField(max_length=64)
    date_descriptor = models.CharField(max_length=48)
    headliner = models.CharField(max_length=48, blank=True)
    short_descriptor = models.TextField()
    poster_thumbnail = MediaFileForeignKey(MediaFile, blank=True, null=True)
    tickets_url = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.series_title, self.date_descriptor)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/featured_box.html', {'featured_box': self})

Page.create_content_type(FeaturedBoxContent, region=('featured_area',))

class ImageRotator(models.Model):
    feincms_item_editor_inline = ImageInField
    img = MediaFileForeignKey(MediaFile, blank=True, null=True)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/image_rotator.html', {'image_rotator': self})

Page.create_content_type(ImageRotator, regions=('rotator_images',))

class SponsorLogo(models.Model):
    location = models.IntegerField(verbose_name='zip (optional)',blank=True, null=True)
    name = models.CharField(max_length=128)
    type = models.CharField(verbose_name='organization type (optional)', max_length="32")
    website_url = models.URLField()
    feincms_item_editor_inline = ImageInField
    img = MediaFileForeignKey(MediaFile, blank=True, null=True)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/mediafile/sponsor_logo.html', {'sponsor_logo': self})

Page.create_content_type(SponsorLogo)
