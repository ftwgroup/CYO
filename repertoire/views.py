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
    model = Concert
    paginate_by = 5