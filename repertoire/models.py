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
from feincms import settings

import os.path
from settings import PROJECT_ROOT

Page.register_extensions('datepublisher', 'navigation', 'seo', 'titles')

Page.register_templates({
    'title': _('Upcoming'),
    #TODO (ipsheeta) is this going to work on everyone's computer now?
    'path': (os.path.join(PROJECT_ROOT, 'repertoire/templates/piece.html')),
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

CONCERT_TYPES = (
    ('NW', 'New Works'),
    ('MI', 'Music in Industry'),
    ('RO', 'Rock the Orchestra'),
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
    #TODO (ipsheeta) still an error?
    songs = models.ManyToManyField(Song)
    soloist1 = models.CharField(max_length=50, blank=True, null=True)
    soloist2 = models.CharField(max_length=50, blank=True, null=True)
    guest = models.CharField(max_length=50, blank=True, null=True)

    #TODO (Ipsheeta) is this sufficient?
    def __unicode__(self):
        return self.headline

class ContentWithConcertInfo(models.Model):
    """
    This is the content type for the concert info
    """
    concert = models.ForeignKey(ConcertInfo, verbose_name=_('concert info'))

    class Meta:
        abstract = True

    def render(self, **kwargs):
        ctx = {'content', self}
        ctx.update(kwargs)

        #TODO (julian) Needs a template file
        return render_to_string('concert_info.html', ctx)

Page.create_content_type(ContentWithConcertInfo)
