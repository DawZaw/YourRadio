from django.contrib import admin
from .models import Album, Artist, Song, Genre


admin.site.register(Genre)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'artist', 'release_date')
    fields = ['cover', 'title', 'artist', 'genre', 'release_date', 'slug']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    fields = ['photo', 'name', 'start_year', 'end_year', 'type', 'slug']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album')
