from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Album, Artist, Song


# Create your views here.
class AlbumListView(ListView):
    model = Artist
    template_name = 'albums/album_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Artist.objects.order_by('name')


class AlbumDetailView(DetailView):
    model = Album


class ArtistDetailView(DetailView):
    model = Artist
