from django.db import models
from django.urls import reverse


# Create your models here.
class Album(models.Model):
    """Model representing an album."""

    title = models.CharField(max_length=100)
    artist = models.ForeignKey(
        'Artist', on_delete=models.SET_NULL, null=True, related_name='album'
    )
    cover = models.ImageField(
        upload_to='albums/media/images/', default='albums/static/default_album.png'
    )
    genre = models.ManyToManyField('Genre')
    release_date = models.DateField()
    slug = models.SlugField(max_length=100, allow_unicode=True)

    class Meta:
        ordering = ['release_date', 'title']

    def __str__(self):
        return self.artist.name + ' - ' + self.title

    def get_absolute_url(self):
        return reverse(
            "album_detail", kwargs={"artist": self.artist.slug, "album": self.slug}
        )


class Artist(models.Model):
    name = models.CharField(max_length=100)
    active_years = models.DateField()

    ARTIST_TYPE = (('b', 'Band'), ('s', 'Solo Artist'))
    type = models.CharField(
        max_length=1,
        choices=ARTIST_TYPE,
        help_text='Artist type (Band, Solo)',
    )
    slug = models.SlugField(max_length=100, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"slug": self.slug})


class Song(models.Model):
    pos = models.IntegerField()
    title = models.CharField(max_length=100)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, allow_unicode=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"slug": self.slug})


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
