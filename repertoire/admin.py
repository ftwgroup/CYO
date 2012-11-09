from django.contrib import admin
from models import *
from repertoire.forms import ConcertForm

class ConcertAdmin(admin.ModelAdmin):
	list_display = ['title', 'series', 'season', 'venue', 'date_time']
	list_filter = ['series', 'season', 'venue']
	form = ConcertForm
	search_fields = ['title']

class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class VenueAdmin(admin.ModelAdmin):
	list_display = ['name', 'address', 'city', 'state', 'zip_code']
	list_filter = ['city', 'state']
	search_fields = ['name', 'city']

	def address(self, obj):
		return '%s %s' % (obj.address1, obj.address2)
	address.admin_order_field = 'address1'

class SongAdmin(admin.ModelAdmin):
	list_display = ['title', 'composer']
	list_filter = ['composer']
	search_fields = ['title', 'composer__last_name']

class PerformerAdmin(admin.ModelAdmin):
	list_display = ['name', 'birth_to_death']
	search_fields = ['first_name', 'last_name', 'bio']

	def name(self, obj):
		return '%s %s' % (obj.first_name, obj.last_name)
	name.admin_order_field = 'last_name'

	def birth_to_death(self, obj):
		if obj.death_year:
			return '%s-%s' % (obj.birth_year, obj.death_year)
		else:
			return '%s-' % obj.birth_year
	birth_to_death.short_description = 'Birth-Death'
	birth_to_death.admin_order_field = 'birth_year'

class PerformedSongAdmin(admin.ModelAdmin):
	list_display = ['song', 'concert', 'premiere']
	list_filter = ['premiere', 'concert']
	search_fields = ['song__title', 'concert__title']

class FeaturedArtistInstrumentAdmin(admin.ModelAdmin):
	list_display = ['performer', 'performed_song', 'instrument']
	list_filter = ['instrument']
	search_fields = ['instrument__title', 'performer__last_name', 'performed_song__title']

class GuestArtistInstrumentAdmin(admin.ModelAdmin):
	list_display = ['performer', 'performed_song', 'instrument']
	list_filter = ['instrument']
	search_fields = ['instrument__title', 'performer__last_name', 'performed_song__title']

class SoloistInstrumentAdmin(admin.ModelAdmin):
	list_display = ['performer', 'performed_song', 'instrument']
	list_filter = ['instrument']
	search_fields = ['instrument__title', 'performer__last_name', 'performed_song__title']

admin.site.register(Concert, ConcertAdmin)
admin.site.register(PerformedSong, PerformedSongAdmin)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Instrument)
admin.site.register(FeaturedArtistInstrument, FeaturedArtistInstrumentAdmin)
admin.site.register(GuestArtistInstrument, GuestArtistInstrumentAdmin)
admin.site.register(SoloistInstrument, SoloistInstrumentAdmin)