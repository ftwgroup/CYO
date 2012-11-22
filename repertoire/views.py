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
            print self.filter
            return ['repertoire/concert_'+self.filter+'_list.html']
        else:
            return ['repertoire/concert_list.html']

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
                    song_title = row[1]
                    person_first_name = row[2].strip()
                    person_last_name = row[3].strip()
                    person_birth_year_and_death_year = row[4].strip().split("-")
                    person_birth_year = person_birth_year_and_death_year[0]
                    try:
                        person_birth_year = int(person_birth_year)
                    except ValueError:
                        person_birth_year = 9999
                    if len(person_birth_year_and_death_year) > 1:
                        person_death_year = person_birth_year_and_death_year[1]
                        try:
                            person_death_year = int(person_death_year)
                        except ValueError:
                            person_death_year = None
                    concert_title = row[5].strip()
                    concert_description = row[6].strip()
                    concert_abstract = row[7].strip()
                    series_title = row[8].strip()
                    concert_season = row[9].strip()
                    if concert_season == "":
                        concert_season = 0
                    else:
                        concert_season = int(concert_season)
                    concert_rough_date = row[10].strip()
                    try:
                        concert_date_time = datetime.datetime.strptime(row[11].strip(), "%m/%d/%Y %H:%M")
                    except ValueError:
                        continue
                    performedsong_premiere = row[12].strip()
                    concert_featured_artist_first = row[13].split(",")
                    concert_featured_artist_last = row[14].split(",")
                    featured_artist_instrument = row[15].split(",")
                    venue_name = row[16].strip()
                    performedsong_arranger_first = row[17].strip()
                    performedsong_arranger_last = row[18].strip()
                    performedsong_guest_artist_first = row[19].strip()
                    performedsong_guest_artist_last = row[20].strip()
                    guest_artist_instrument = row[21].strip()
                    performedsong_soloist_first = row[22].strip()
                    performedsong_soloist_last = row[23].strip()
                    soloist_instrument = row[24].strip()
                    val = URLValidator(verify_exists=False)
                    try:
                        val(row[25].strip())
                        concert_poster_image_url = row[25].strip()
                    except ValidationError, e:
                        pass
                    try:
                        val(row[26].strip())
                        concert_photos_link = row[26].strip()
                    except ValidationError, e:
                        pass
                    try:
                        val(row[27].strip())
                        concert_video_link = row[27].strip()
                    except ValidationError, e:
                        pass
                    try:
                        val(row[28].strip())
                        concert_program_file_url = row[28].strip()
                    except ValidationError, e:
                        pass
                    performedsong_note = row[29].strip()
                    try:
                        arranger = Performer.objects.get(first_name=performedsong_arranger_first, last_name=performedsong_arranger_last)
                    except Performer.DoesNotExist:
                        arranger = Performer(first_name=performedsong_arranger_first, last_name=performedsong_arranger_last, birth_year=9999)
                        arranger.save()
                    try:
                        guest_artist = Performer.objects.get(first_name=performedsong_guest_artist_first, last_name=performedsong_guest_artist_last)
                    except Performer.DoesNotExist:
                        guest_artist = Performer(first_name=performedsong_guest_artist_first, last_name=performedsong_guest_artist_last, birth_year=9999)
                        guest_artist.save()
                    try:
                        soloist = Performer.objects.get(first_name=performedsong_soloist_first, last_name=performedsong_soloist_last)
                    except Performer.DoesNotExist:
                        soloist = Performer(first_name=performedsong_soloist_first, last_name=performedsong_soloist_last, birth_year=9999)
                        soloist.save()
                    try:
                        composer = Performer.objects.get(first_name=person_first_name, last_name=person_last_name)
                    except Performer.DoesNotExist:
                        composer = Performer(first_name=person_first_name, last_name=person_last_name, birth_year=person_birth_year)
                        try:
                            composer.death_year = person_death_year
                        except:
                            pass
                        composer.save()
                    featured_artists = []
                    for index, artist in enumerate(concert_featured_artist_first):
                        try:
                            featured_artist, created = Performer.objects.get_or_create(first_name=concert_featured_artist_first[index].strip(), last_name=concert_featured_artist_last[index].strip())
                            if created:
                                featured_artist.birth_year = 9999
                                featured_artist.save()
                            featured_artists.append(featured_artist)
                        except:
                            pass    
                    song, created = Song.objects.get_or_create(title=song_title, composer=composer)
                    venue, created = Venue.objects.get_or_create(name=venue_name)
                    series, created = Series.objects.get_or_create(title=series_title)
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
                    try:
                        performed_song = PerformedSong.objects.get(song=song, concert=concert)
                    except PerformedSong.DoesNotExist:
                        performed_song = PerformedSong(song=song, concert=concert, premiere=performedsong_premiere)
                        performed_song.save()
                    performed_song.arranger.add(arranger)
                    performed_song.guest_artist.add(guest_artist)
                    performed_song.note = performedsong_note
                    performed_song.save()
                    for index, instrument in enumerate(featured_artist_instrument):
                        instrument = instrument.strip()
                        if instrument != '':
                            inst, created = Instrument.objects.get_or_create(instrument=instrument)
                            fainstrument = FeaturedArtistInstrument.objects.get_or_create(performer=featured_artists[index], performed_song=performed_song, instrument=inst)
                    if guest_artist_instrument != '':
                        instrument, created = Instrument.objects.get_or_create(instrument=guest_artist_instrument) 
                        gainstrument = GuestArtistInstrument.objects.get_or_create(performer=guest_artist, performed_song=performed_song, instrument=instrument)
                    if soloist_instrument != '':
                        instrument, created = Instrument.objects.get_or_create(instrument=soloist_instrument)
                        soinstrument = SoloistInstrument.objects.get_or_create(performer=soloist, performed_song=performed_song, instrument=instrument) 
            return HttpResponseRedirect('/admin/repertoire/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', RequestContext(request, {'form': form}))

def generate_playlist(request):
    playlist = Song.objects.filter(audio_file__startswith="song_audio_file/").order_by('?')[:10]
    to_json = []
    for song in playlist:
        composer_name = "%s %s" % (song.composer.first_name, song.composer.last_name)
        to_json.append({"title":song.title, "artist": composer_name, "mp3": song.audio_file.url})
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

