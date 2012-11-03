from django.contrib import admin
from models import *
from repertoire.forms import ConcertForm

class ConcertAdmin(admin.ModelAdmin):
    form = ConcertForm
    search_fields = ['title']

class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class VenueAdmin(admin.ModelAdmin):
	search_fields = ['name', 'city']

class SongAdmin(admin.ModelAdmin):
	search_fields = ['title', 'composer']

class PerformerAdmin(admin.ModelAdmin):
	search_fields = ['first_name', 'last_name', 'bio']



admin.site.register(Concert, ConcertAdmin)
admin.site.register(PerformedSong)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Venue, VenueAdmin)
