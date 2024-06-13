from django.urls import path
from .views import *
from reviews.views import *

from dal import autocomplete

class MovieAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Movie.objects.all()
        if self.q:
            qs = qs.filter(title__icontains=self.q)
        return qs


urlpatterns = [
    path('<str:username>/', view_profile, name='view_profile'),
    path('', view_notifications, name='view_notifications'),
    path('search/', movie_search, name='movie_search'),
]
