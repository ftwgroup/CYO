
"""
This file handles extending the repertoire to allow the display of the featured concert boxes on the homepage.
"""
from django.views.generic.detail import DetailView
from repertoire.models import Concert


"""
Creating concert views from repertoire models here

"""

class FeaturedBoxView(DetailView):
    """
    This class was created to display a concert details page
    """
    model = Concert
    context_object_name = 'concert'
    template_name = 'featured_box_view.html'
