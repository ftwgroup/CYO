from django.db.models.query_utils import Q
from django.http import HttpResponse
import datetime
from django.views.generic.list import ListView
from repertoire.models import Concert, ConcertSong, Song

# TODO make repertoire view dynamic for all filter options

# Todo view sand urls for concert pages, artist pages, and song pages

class RepertoireView(ListView):
    """
    This class renders the repertoire
    """
    allow_empty = True
    paginate_by = 5
    context_object_name = 'concert_list'

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
            queryset = ConcertSong.objects.order_by('song__composer__last_name')
        elif self.filter == 'song':
            queryset = ConcertSong.objects.order_by('song')
        elif self.filter == 'premiere':
            queryset = ConcertSong.objects.filter(Q(world_premiere=True)|Q(local_premiere=True))
        else:
            queryset = ConcertSong.objects.order_by(self.filter+'__last_name')
        return queryset

    def get_template_names(self):
        if self.filter:
            return ['repertoire/filtered_list.html']
        else:
            return ['repertoire/concert_list.html']