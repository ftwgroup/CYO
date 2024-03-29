from haystack.indexes import *
from haystack import site
from repertoire.models import *

class SeriesIndex(SearchIndex):
	text = CharField(document=True, model_attr="title")

class VenueIndex(SearchIndex):
	text = CharField(document=True, model_attr="name")

class SongIndex(SearchIndex):
	text = CharField(document=True, use_template=True)

class ConcertIndex(SearchIndex):
	text = CharField(document=True, use_template=True)

class PerformerIndex(SearchIndex):
	text = CharField(document=True, use_template=True)

site.register(Series, SeriesIndex)
site.register(Venue, VenueIndex)
site.register(Song, SongIndex)
site.register(Concert, ConcertIndex)
site.register(Performer, PerformerIndex)

