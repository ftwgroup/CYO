from django.contrib import admin
from django.contrib.localflavor import us
from django.contrib.localflavor.us.models import USStateField, USPostalCodeField

from django.db import models
from django.template.loader import render_to_string

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

#TODO (Ipsheeta) read http://www.feinheit.ch/media/labs/feincms/contenttypes.html#design-considerations-for-content-types

CONCERT_TYPES = (
    ('NW', 'New Works'),
    ('MI', 'Music in Industry'),
    ('RO', 'Rock the Orchestra'),
)

DEBUT_STATUS = (
    ('US', 'US Premiere'),
    ('WP', 'World Premiere'),
    ('OW', 'Original Work'),
)

class Song(models.Model):
    """
    Song class for the song database. Includes the :class: 'feincms.models.ExtensionMixin'
    because of the (handy) extension mechanism.
    """
    #TODO (ipsheeta) I don't think I want this relationship defined yet
    #performance = models.ManyToManyField(ConcertInfo)
    title = models.CharField(max_length=50)
    composer = models.CharField(max_length=50)
    premiered_by = models.CharField(max_length=50, blank=True, null=True)
    #TODO (julian) at some point they will want to upload the actual music for the kids
    #file = models.FileField(_('sheet music'), max_length=255, upload_to=settings.FEINCMS_MEDIALIBRARY_UPLOAD_TO)

    #TODO (Ipsheeta) is this sufficient?
    def __unicode__(self):
        return self.title

class ConcertInfo(models.Model):
    date_time = models.DateTimeField('Date and Time')
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = us.models.USStateField(blank=True, null=True)
    zipcode = us.models.USPostalCodeField(blank=True, null=True)

    headline = models.CharField(max_length=100)
    type_of_concert = models.CharField(max_length=50, choices=CONCERT_TYPES)
    debut_status = models.CharField(max_length=50, choices=DEBUT_STATUS)
    #TODO (ipsheeta) still an error?
    songs = models.ManyToManyField(Song)
    soloist1 = models.CharField(max_length=50, blank=True, null=True)
    soloist2 = models.CharField(max_length=50, blank=True, null=True)
    guest = models.CharField(max_length=50, blank=True, null=True)
    long_description = models.TextField(max_length=1000)

    #TODO (Ipsheeta) is this sufficient?
    def __unicode__(self):
        return self.headline

#class ContentWithConcertInfo(models.Model):
#    """
#    This is the content type for the concert info
#    """
#    concert = models.ForeignKey(ConcertInfo, verbose_name=_('concert info'))
#
#    class Meta:
#        abstract = True
#
#    def render(self, **kwargs):
#        ctx = {'content', self}
#        ctx.update(kwargs)
#
#        #TODO (julian) Needs a template file
#        return render_to_string('concert_info.html', {'content':self})
#
#    @property
#    def media(self):
#        return forms.Media(
#            css={'all': ('/static/css/concert_info.css',),},
#        )
#
#Page.create_content_type(ContentWithConcertInfo)

class ConcertPageContent(models.Model):
    """
    This is the text boxes for the yellow concert page info
    """
# TODO: (ipsheeta) for now just using a text field...hoping to add a richtext for each section (yellow, white, sidebar)
    content = models.TextField()

    class Meta:
        abstract = True

    def render(self, **kwargs):
        ctx = {'content', self}
        ctx.update(kwargs)
        return render_to_string('concert_page.html', {'content':self})
        
    @property
    def media(self):
        return forms.Media(
            css={'all': ('/static/css/concert_page.css',),},
        )

Page.create_content_type(ConcertPageContent)

class Slider(models.Model):
    """
    This content type creates a slider
    """
    images = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        ctx = {'content', self}
        ctx.update(kwargs)

        return render_to_string('slider.html', ctx)
