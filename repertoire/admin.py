from django.contrib import admin
from models import *
from repertoire.forms import ConcertForm

class ConcertAdmin(admin.ModelAdmin):
    form = ConcertForm

class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Concert, ConcertAdmin)
admin.site.register(PerformedSong)
admin.site.register(Performer)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Song)
admin.site.register(Venue)
