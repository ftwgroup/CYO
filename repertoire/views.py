from django.http import HttpResponse
import datetime
from django.views.generic.list import ListView
from repertoire.models import Concert

# TODO make repertoire view dynamic for all filter options

class RepertoireView(ListView):
    """
    This class renders the repertoire
    """
    allow_empty = True
    paginate_by = 5

    def get_queryset(self):
        """
        Get the list of items for this view
        """
        return
