from albums.models import Song, Album
import datetime
import csv
import time


def run():
    with open('albums/songs.csv') as file:
        reader = csv.reader(file)

        Song.objects.all().delete()

        for row in reader:
            album = Album.objects.get(title=row[1])
            min, sec = row[3].split(':')
            min, sec = int(min), int(sec)
            length = datetime.timedelta(days=0, seconds=min * 60 + sec)
            print(row[2], album.title)
            song = Song(
                no=row[0],
                album=album,
                title=row[2],
                length=length,
            )
            song.save()
