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

class PersonIndex(SearchIndex):
	text = CharField(document=True, use_template=True)
	# first_name = CharField(model_attr="first_name")
	# bio = CharField(model_attr="bio")

site.register(Series, SeriesIndex)
site.register(Venue, VenueIndex)
site.register(Song, SongIndex)
site.register(Concert, ConcertIndex)
site.register(Person, PersonIndex)

