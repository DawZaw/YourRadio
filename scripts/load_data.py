from django.utils.text import slugify
from artists.models import Genre, Artist, Song, Album
import datetime
import csv


def run():
    clear_data()
    populate_artists()
    populate_albums()
    populate_songs()


def clear_data():
    Song.objects.all().delete()
    Album.objects.all().delete()
    Artist.objects.all().delete()
    Genre.objects.all().delete()


def populate_artists():
    with open("scripts/artists.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            start_year = datetime.datetime.strptime(row[1], "%Y-%m-%d")
            end_year = None
            if row[2]:
                end_year = datetime.datetime.strptime(row[2], "%Y-%m-%d")
            artist, _ = Artist.objects.get_or_create(
                name=row[0],
                start_year=start_year,
                end_year=end_year,
                photo="static/artists/"
                + slugify(f"{row[0]}", allow_unicode=True)
                + ".jpg",
                type=row[3],
                slug=slugify(row[0], allow_unicode=True),
            )
            artist.save()


def populate_albums():
    with open("scripts/albums.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            artist, _ = Artist.objects.get_or_create(name=row[1])
            release_date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
            tmp_title = row[0].replace(".", "-")
            album, _ = Album.objects.get_or_create(
                title=row[0],
                artist=artist,
                release_date=release_date,
                cover="static/albums/"
                + slugify(f"{row[1]}-{tmp_title}", allow_unicode=True)
                + ".webp",
                slug=slugify(tmp_title, allow_unicode=True),
            )
            genres = row[3].split(";")
            for genre_name in genres:
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                album.genre.add(genre)
            album.save()


def populate_songs():
    with open("scripts/songs.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            album = Album.objects.get(title=row[1])
            min, sec = row[3].split(":")
            min, sec = int(min), int(sec)
            length = datetime.timedelta(days=0, seconds=min * 60 + sec)
            song, _ = Song.objects.get_or_create(
                no=row[0],
                album=album,
                title=row[2],
                length=length,
            )
            song.save()
