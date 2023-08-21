from django.contrib import admin
from .models import Album, Artist, Song, Genre


# Register your models here.
admin.site.register(Genre)
admin.site.register(Song)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'artist', 'release_date')
    fields = ['cover', 'title', 'artist', 'genre', 'release_date', 'slug']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    fields = ['name', 'active_years', 'type', 'slug']
