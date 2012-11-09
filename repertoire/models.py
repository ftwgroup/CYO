from django.contrib.localflavor.us.models import USStateField
from django.db import models
from django.template.defaultfilters import slugify
from feincms.content.application import models as app_models

# TODO include tagging

CONCERT_SERIES = (
    ('RTO', 'Rock the Orchestra'),
    ('NW', 'New Works'),
    ('MAII', 'Music and Its Industry'),
)

class Series(models.Model):
    """
    This model specifies the concert series. Allowing for future series to be created.
    """
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, blank=True) # should be unique, but causes problems with migration

    class Meta:
        verbose_name_plural = "series"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Series, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    @app_models.permalink
    def get_absolute_url(self):
        return ('concert-archive', 'repertoire.concerts', (), {
            'slug': self.slug,
            })


class Venue(models.Model):
    """
    This table describes the venue for a concert.
    """
    name = models.CharField(max_length=128) #TODO (stephen) once migrations are redone, rename this colmn to title
    address1 = models.CharField(max_length=64, blank=True, null=True)
    address2 = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    state = USStateField(blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
            return self.name

    @app_models.permalink
    def get_absolute_url(self):
        return ('venue-detail', 'repertoire.urls', (), {
            'pk': self.pk,
            })


class Concert(models.Model):
    """
    This model stores concert information
    """
    title = models.CharField(max_length=60)
    short_description = models.TextField(verbose_name="Three line descriptor", null=True, blank=True)
    abstract = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    series = models.ForeignKey('Series', blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)

    rough_date = models.CharField(verbose_name="e.g. Summer 2012", max_length=32, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)

    featured_artist = models.ManyToManyField('Performer', blank=True, null=True) #TODO through PerformedSong?
    venue = models.ForeignKey('Venue', null=True)

    poster_image = models.ImageField(upload_to='concert_poster', blank=True, null=True)
    photos_link = models.URLField( blank=True, null=True)
    video_link = models.URLField( blank=True, null=True)
    program_file = models.FileField(upload_to='concert_program',  blank=True, null=True)

    class Meta:
        ordering = ['date_time']

    def __unicode__(self):
        return self.title

    @app_models.permalink
    def get_absolute_url(self):
        return ('concert-detail', 'repertoire.urls', (), {
            'pk': self.pk,
            })


class PerformedSong(models.Model):
    """
    This table joins Concert and Song
    """
    song = models.ForeignKey('Song')
    concert = models.ForeignKey('Concert', blank=True, null=True)

    arranger = models.ManyToManyField('Performer', related_name='arranger', blank=True, null=True)
    conductor = models.ManyToManyField('Performer', related_name='conductor', blank=True, null=True)
    guest_artist = models.ManyToManyField('Performer', related_name='guest_artist',verbose_name='Guest Artist' ,blank=True,
        null=True)
    soloist = models.ManyToManyField('Performer', blank=True, null=True)

    note = models.TextField(blank=True, null=True)

    PREMIERE_TAGS = (
        ('a','World Premiere'),
        ('b','US Premiere'),
        ('c','Local Premiere'),
        ('d','None'),
    )
    premiere = models.CharField(max_length=1, choices=PREMIERE_TAGS, default='d')

    def __unicode__(self):
        return "%s at %s" % (self.song.title, self.concert.title)


class Song(models.Model):
    """
    This song model stores one song performed by cyo.
    """
    title = models.CharField(max_length=48)
    composer = models.ForeignKey('Performer')
    description = models.TextField('Description of this song', blank=True, null=True)
    audio_file = models.FileField(upload_to='song_audio_file', blank=True, null=True)

    def __unicode__(self):
        return self.title

    @app_models.permalink
    def get_absolute_url(self):
        return ('song-detail', 'repertoire.urls', (), {
            'pk': self.pk,
            })


class Person(models.Model):
    """
    This model stores artist information
    """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_year = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Performer(Person):
    @app_models.permalink
    def get_absolute_url(self):
        return ('performer-detail', 'repertoire.urls', (), {
            'pk': self.pk,
            })
