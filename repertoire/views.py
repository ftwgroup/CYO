from django.db.models.query_utils import Q
from django.http import HttpResponse
import datetime
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from repertoire.models import Concert, ConcertSong, Song, Performer

# TODO make repertoire view dynamic for all filter options

# Todo view sand urls for concert pages, artist pages, and song pages

class RepertoireView(ListView):
    """
    This class renders the repertoire
    """
    allow_empty = True
    paginate_by = 5
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
            queryset = ConcertSong.objects.filter(Q(world_premiere=True) | Q(local_premiere=True)).order_by('concert__date')
        else:
            queryset = ConcertSong.objects.order_by(self.filter+'__last_name')
        return queryset

    def get_template_names(self):
        # TODO we don't want to have a template for each performer type
        if self.filter:
            print self.filter
            return ['repertoire/concert_'+self.filter+'_list.html']
        else:
            return ['repertoire/concert_list.html']


class SongView(DetailView):
    """
    This class renders individual pages per repertiore song
    """
    model=Song
    template_name='repertoire/song_detail.html'

    def song_page(request, songname):
        return
    
class PerformerView(DetailView):
    """
    This class renders individual pages per repertiore performer
    """


class ConcertView(DetailView):
    """
    This class renders individual pages per repertiore concert
    """

class ComposerView(DetailView):
    """
    This class renders individual pages per repertiore composer
    """

