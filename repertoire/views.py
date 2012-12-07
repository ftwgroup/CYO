from django.db.models.query_utils import Q
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from repertoire.models import *
from repertoire.forms import UploadFileForm
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.utils import simplejson

# TODO make repertoire view dynamic for all filter options

# Todo view sand urls for concert pages, artist pages, and song pages

class RepertoireView(ListView):
    """
    This class renders the repertoire
    """
    allow_empty = True
    paginate_by = 15
    context_object_name = 'repertoire_list'

    def dispatch(self, request, *args, **kwargs):
        self.filter = kwargs.get('filter', '')
        return super(RepertoireView, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        """
        Get the list of items for this view
        """
        if not self.filter:
            queryset = Concert.objects.all()
        elif self.filter == 'composer':
            queryset = Performer.objects.order_by('last_name')
        elif self.filter == 'song':
            queryset = Song.objects.order_by('title')
        elif self.filter == 'premiere':
            queryset = PerformedSong.objects.exclude(premiere='d').order_by('-concert__date_time')
        else:
            queryset = PerformedSong.objects.order_by(self.filter+'__last_name')
        return queryset

    def get_template_names(self):
        # TODO we don't want to have a template for each performer type
        if self.filter:
            return ['repertoire/concert_'+self.filter+'_list.html']
        else:
            return ['repertoire/concert_list.html']

def _parse_row(string):
    if string == '':
        return None
    else:
        return string.strip()

@staff_member_required
def upload_file(request):
    import csv
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            reader = csv.reader(file)
            for row in reader:
                if row[0] != "ID":
                    song_title = _parse_row(row[1])
                    person_first_name = _parse_row(row[2])
                    person_last_name = _parse_row(row[3])
                    person_birth_year_and_death_year = _parse_row(row[4])
                    if person_birth_year_and_death_year:
                        person_birth_year_and_death_year = person_birth_year_and_death_year.split("-")
                        person_birth_year = person_birth_year_and_death_year[0]
                        try:
                            person_birth_year = int(person_birth_year)
                        except ValueError:
                            person_birth_year = None
                        if len(person_birth_year_and_death_year) > 1:
                            person_death_year = person_birth_year_and_death_year[1]
                            try:
                                person_death_year = int(person_death_year)
                            except ValueError:
                                person_death_year = None
                    concert_title = _parse_row(row[5])
                    concert_description = _parse_row(row[6])
                    concert_abstract = _parse_row(row[7])
                    series_title = _parse_row(row[8])
                    concert_season = _parse_row(row[9])
                    if concert_season:
                        concert_season = int(concert_season) 
                    else:
                        concert_season = 0
                    concert_rough_date = _parse_row(row[10])
                    try:
                        concert_date_time = datetime.datetime.strptime(_parse_row(row[11]), "%m/%d/%Y %H:%M")
                    except:
                        pass
                    performedsong_premiere = _parse_row(row[12])
                    try:
                        concert_featured_artist_first = _parse_row(row[13]).split(",")
                    except:
                        pass
                    try:
                        concert_featured_artist_last = _parse_row(row[14]).split(",")
                    except:
                        pass
                    try:
                        featured_artist_instrument = _parse_row(row[15]).split(",")
                    except:
                        pass
                    venue_name = _parse_row(row[16])
                    performedsong_arranger_first = _parse_row(row[17])
                    performedsong_arranger_last = _parse_row(row[18])
                    performedsong_guest_artist_first = _parse_row(row[19])
                    performedsong_guest_artist_last = _parse_row(row[20])
                    guest_artist_instrument = _parse_row(row[21])
                    performedsong_soloist_first = _parse_row(row[22])
                    performedsong_soloist_last = _parse_row(row[23])
                    soloist_instrument = _parse_row(row[24])
                    val = URLValidator(verify_exists=False)
                    try:
                        val(_parse_row(row[25]))
                        concert_poster_image_url = _parse_row(row[25])
                    except ValidationError, e:
                        pass
                    try:
                        val(_parse_row(row[26]))
                        concert_photos_link = _parse_row(row[26])
                    except ValidationError, e:
                        pass
                    try:
                        val(_parse_row(row[27]))
                        concert_video_link = _parse_row(row[27])
                    except ValidationError, e:
                        pass
                    try:
                        val(_parse_row(row[28]))
                        concert_program_file_url = _parse_row(row[28])
                    except ValidationError, e:
                        pass
                    performedsong_note = _parse_row(row[29])
                    try:
                        arranger, created = Performer.objects.get_or_create(first_name=performedsong_arranger_first, last_name=performedsong_arranger_last)
                    except:
                        pass
                    try:
                        guest_artist, created = Performer.objects.get_or_create(first_name=performedsong_guest_artist_first, last_name=performedsong_guest_artist_last)
                    except:
                        pass
                    try:
                        soloist, created = Performer.objects.get_or_create(first_name=performedsong_soloist_first, last_name=performedsong_soloist_last)
                    except:
                        pass
                    try:
                        composer, created = Performer.objects.get_or_create(first_name=person_first_name, last_name=person_last_name)
                        try:
                            composer.birth_year = person_birth_year
                        except:
                            pass
                        try:
                            composer.death_year = person_death_year
                        except:
                            pass
                        composer.save()
                    except:
                        pass
                    featured_artists = []
                    for index, artist in enumerate(concert_featured_artist_first):
                        try:
                            featured_artist, created = Performer.objects.get_or_create(first_name=concert_featured_artist_first[index].strip(), last_name=concert_featured_artist_last[index].strip())
                            featured_artists.append(featured_artist)
                        except:
                            pass
                    try:  
                        song, created = Song.objects.get_or_create(title=song_title, composer=composer)
                    except:
                        pass
                    # if venue_name and venue_name != '':
                    try:
                        venue, created = Venue.objects.get_or_create(name=venue_name)
                    except:
                        pass
                    # if series_title and series_title != '':
                    try:
                        series, created = Series.objects.get_or_create(title=series_title)
                    except:
                        pass
                    # if concert_title and series and concert_season and concert_date_time:
                    try:
                        concert, created = Concert.objects.get_or_create(title=concert_title, series=series, season=concert_season, date_time=concert_date_time)
                        concert.abstract = concert_abstract
                        concert.description = concert_description
                        concert.rough_date = concert_rough_date
                        for artist in featured_artists:
                            concert.featured_artist.add(artist)
                        try:
                            concert.photos_link = concert_photos_link
                        except:
                            pass
                        try:
                            concert.video_link = concert_video_link
                        except:
                            pass
                        
                        concert.save()
                    except:
                        pass
                    try:
                        performed_song, created = PerformedSong.objects.get_or_create(song=song, concert=concert)
                        try:
                            performed_song.premiere = performedsong_premiere
                            performed_song.save()
                        except:
                            pass
                    except:
                        pass
                    try:
                        performed_song.arranger.add(arranger)
                        performed_song.guest_artist.add(guest_artist)
                        performed_song.note = performedsong_note
                        performed_song.save()
                    except:
                        pass
                    try:
                        for index, instrument in enumerate(featured_artist_instrument):
                            instrument = instrument.strip()
                            if instrument != '':
                                inst, created = Instrument.objects.get_or_create(instrument=instrument)
                                fainstrument = FeaturedArtistInstrument.objects.get_or_create(performer=featured_artists[index], performed_song=performed_song, instrument=inst)
                    except:
                        pass
                    try:
                        if guest_artist_instrument != '':
                            instrument, created = Instrument.objects.get_or_create(instrument=guest_artist_instrument) 
                            gainstrument = GuestArtistInstrument.objects.get_or_create(performer=guest_artist, performed_song=performed_song, instrument=instrument)
                    except:
                        pass
                    try:
                        if soloist_instrument != '':
                            instrument, created = Instrument.objects.get_or_create(instrument=soloist_instrument)
                            soinstrument = SoloistInstrument.objects.get_or_create(performer=soloist, performed_song=performed_song, instrument=instrument)
                    except:
                        pass
            return HttpResponseRedirect('/admin/repertoire/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', RequestContext(request, {'form': form}))

def generate_playlist(request):
    playlist = Song.objects.filter(audio_file__startswith="song_audio_file/").filter(playable=True).order_by('?')[:10]
    to_json = []
    for song in playlist:
        composer_name = "%s %s" % (song.composer.first_name, song.composer.last_name)
        to_json.append({"title":song.title, "artist": composer_name, "mp3": song.audio_file.url})
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

