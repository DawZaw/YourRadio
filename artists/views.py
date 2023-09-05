import datetime
from django.shortcuts import render
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from .models import Album, Artist, Song
from comments.models import Comment


def search_view(request):
    search = request.GET.get("search")

    if search != "":
        albums = Album.objects.filter(title__istartswith=search)[:3]
        artists = Artist.objects.filter(name__istartswith=search)[:3]
    else:
        albums = None
        artists = None
    context = {'albums': albums, 'artists': artists}

    return render(request, 'partials/search_results.html', context)


class AlbumListView(ListView):
    model = Artist
    template_name = 'artists/album_list.html'

    def get_queryset(self):
        return Artist.objects.order_by('name')


class AlbumDetailView(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.object
        context["tracklist"] = album.song_set.all().order_by('no')
        total = datetime.timedelta(0, 0)
        for track in context['tracklist']:
            total += track.length
            track.length = str(track.length)[2:]
        context["total"] = total

        # Comment section
        slug = slugify(f"{album.artist.slug}-{album.slug}")
        comments = Comment.objects.filter(page=slug)
        paginator = Paginator(comments, 5)
        page = self.request.GET.get('page', 1)
        comments = paginator.get_page(page)
        context['comments'] = comments
        return context


class ArtistDetailView(DetailView):
    model = Artist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist = self.object

        # Comment section
        slug = artist.slug
        comments = Comment.objects.filter(page=slug)
        paginator = Paginator(comments, 5)
        page = self.request.GET.get('page', 1)
        comments = paginator.get_page(page)
        context['comments'] = comments
        return context
