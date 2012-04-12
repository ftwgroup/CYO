from django.contrib.localflavor import us
from django.db import models

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

    def __unicode__(self):
        return self.title
    
class Venue(models.Model):
    """
    This table describes the venue for a concert.
    """
    name = models.CharField(max_length=128)
    address1 = models.CharField(max_length=64)
    address2 = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=60)
    state = us.models.USStateField()
    zip_code = models.CharField(max_length=10)

    def __unicode__(self):
            return self.name

class Concert(models.Model):
    """
    This model stores concert information
    """
    title = models.CharField(max_length=60)
    short_description = models.TextField(verbose_name="Three line descriptor")
    description = models.TextField()
    series = models.ForeignKey('Series')
    season = models.IntegerField()

    rough_date = models.CharField(verbose_name="e.g. Summer 2012", max_length=32, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    featured_artist = models.ManyToManyField("Performer")
    venue = models.ForeignKey('Venue', null=True)

    poster = models.CharField(max_length=128, blank=True, null=True)
    media_link = models.TextField()

    def __unicode__(self):
        return self.title


class PerformedSong(models.Model):
    """
    This table joins Concert and Song
    """
    song = models.ForeignKey('Song')
    concert = models.ForeignKey('Concert')

    arranger = models.ManyToManyField('Performer', related_name='arranger', blank=True, null=True)
    conductor = models.ManyToManyField('Performer', related_name='conductor', blank=True, null=True)
    guest_artist = models.ManyToManyField('Performer', related_name='guest_artist',verbose_name='Guest Artist' ,blank=True,
        null=True)
    soloist = models.ManyToManyField('Performer', blank=True, null=True)

    SONG_TAGS = (
        ('a','World Premiere'),
        ('b','US Premiere'),
        ('c','Local Premiere'),
    )
    premiere = models.CharField(max_length=1, choices=SONG_TAGS)

    def __unicode__(self):
        return "%s at %s" % (self.song.title, self.concert.title)


class Song(models.Model):
    """
    This song model stores one song performed by cyo.
    """
    title = models.CharField(max_length=48)
    composer = models.ForeignKey('Performer')
    description = models.TextField('Description of this song')

    def __unicode__(self):
        return self.title

class Person(models.Model):
    """
    This model stores artist information
    """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Performer(Person):
    pass