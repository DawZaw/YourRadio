from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from artists.models import Album
from django.db.models.functions import Lower


class SiteUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users/media/images/avatars/',
        default='static/img/default_user.png',
    )
    favorite_albums = models.ManyToManyField(Album, blank=True)
    follows = models.ManyToManyField('self', blank=True)

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"slug": self.username})

    def __str__(self):
        return self.username

    class Meta:
        ordering = [Lower('username')]
