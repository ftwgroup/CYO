from django.contrib.localflavor import us
from django.db import models

# TODO include tagging

SONG_TAGS = (
    ('a','World Premiere'),
    ('b','US Premiere'),
    ('c','Local Premiere'),
)

#TODO create a special something to state 'world premeire'

class Song(models.Model):
    """
    This song model stores one song performed by cyo.
    """
    title = models.CharField(max_length=48)
    composer = models.ForeignKey('Performer')
    note = models.TextField('Song notes')

    def __unicode__(self):
        return self.title


class Concert(models.Model):
    """
    This model stores concert information
    """
    title = models.CharField(max_length=60)
    date = models.DateField()
    address1 = models.CharField(max_length=64)
    address2 = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=60)
    state = us.models.USStateField()
    zip_code = models.CharField(max_length=10)
    songs = models.ManyToManyField('Song', through="ConcertSong")

    def __unicode__(self):
        return self.title

class ConcertSong(models.Model):
    song = models.ForeignKey('Song')
    concert = models.ForeignKey('Concert')
    arranger = models.ForeignKey('Performer', related_name='arranger', blank=True, null=True)
    conductor = models.ForeignKey('Performer', related_name='conductor', blank=True, null=True)
    guest_artist = models.ForeignKey('Performer', related_name='guest_artist',verbose_name='Guest Artist' ,blank=True, null=True)
    soloist = models.ForeignKey('Performer', blank=True, null=True)
    world_premiere = models.BooleanField('World Premiere', default=False)
    local_premiere = models.BooleanField('Local Premiere', default=False)

class Person(models.Model):
    """
    This model stores composer information
    """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Performer(Person):
    pass