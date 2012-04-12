from django.contrib import admin
from django.contrib.localflavor import us
from django.contrib.localflavor.us.models import USStateField, USPostalCodeField

from django.db import models
from django.db.models.fields.related import ForeignKey
from django.template.loader import render_to_string

from django import forms

from django.utils.translation import ugettext_lazy as _
from feincms.module import page
from feincms.module.medialibrary.fields import MediaFileForeignKey
from feincms.module.medialibrary.models import MediaFile
from feincms.admin.item_editor import FeinCMSInline
from feincms.content.medialibrary.v2 import MediaFileContent

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent

import os.path
from string import maketrans

Page.register_extensions('datepublisher', 'navigation', 'seo', 'titles')

Page.register_templates(
        {
        'title': 'Top-Level Page',
        'path': 'top_level.html',
        'regions': (
            ('content', 'Main Content (Yellow)'),
            ('extra_content', 'Extra Content (White)'),
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
        'title': 'Homepage',
        'path': 'home.html',
        'regions': (
            ('rotator_images', 'Rotator Images'),
            ('featured_area', 'Featured Area'),
            ('sidebar', '(Home) Side Bar Sections')
           ),
        },
        {
        'title': 'Media Page',
        'path': 'media.html',
        'regions': (
            ('content', 'Content Area'),
            ('sidebar', '(Home) Side Bar Sections')
            ),
        },
)

Page.create_content_type(RichTextContent)

Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('concertthumbnail', _('Concert Poster Image')),
    ('downloadable', _('Downloadable Image')),
))


# TODO (julian) depending on how future conversations with CYO goes, we may refactor


class ImageInField(FeinCMSInline):
    raw_id_fields = ('poster_thumbnail', 'img')

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

#    def __unicode__(self):
#        return u'%s %s' % (self.series_title, self.date_descriptor)

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

class ImageWrapped(models.Model):
    feincms_item_editor_inline = ImageInField
    img = MediaFileForeignKey(MediaFile, blank=True, null=True)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/image_wrapped.html', {'image_wrapped': self})

Page.create_content_type(ImageWrapped, regions=('content','highlight'))

class SponsorLogo(models.Model):
    location = models.IntegerField(verbose_name='zip (optional)',blank=True, null=True)
    name = models.CharField(max_length=128)
    type = models.CharField(verbose_name='organization type (optional)', max_length="32")
    website_url = models.URLField()
    feincms_item_editor_inline = ImageInField
    img = MediaFileForeignKey(MediaFile, blank=True, null=True)

    #def concert_dow(self):
    #    obj = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Sunday'}
    #    return (obj[dow] for dow in (self).concert_datetime.weekday)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('content/mediafile/sponsor_logo.html', {'sponsor_logo': self})

Page.create_content_type(SponsorLogo, regions=('content',))

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

Page.create_content_type(ConcertDetails, regions=('concert_details',))
Page.create_content_type(ConcertArchiveDetails)