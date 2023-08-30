from django.shortcuts import render
from django.views.generic import ListView, DetailView
import datetime

from .models import Album, Artist, Song


# Create your views here.
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
        return context


class ArtistDetailView(DetailView):
    model = Artist


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def search_album(request):
    search_text = request.POST.get('search')
    if search_text != "":
        results = Album.objects.filter(title__istartswith=search_text)[:3]
    else:
        results = None
    context = {'results': results}
    return render(request, 'partials/search_results.html', context)
