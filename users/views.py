from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, View
import datetime

from artists.models import Album
from .models import SiteUser


class UsersListView(ListView):
    model = SiteUser
    template_name = 'users/users_list.html'

    class Meta:
        ordering = 'username'

    def get_queryset(self):
        return SiteUser.objects.exclude(is_superuser=True)


class UserDetailView(DetailView):
    model = SiteUser
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        albums = (
            SiteUser.objects.filter(username=self.get_object())
            .get()
            .favorite_albums.all()
        )
        genres_count = {}
        for album in albums:
            for genre in album.genre.all():
                g = genre.name
                genres_count[g] = genres_count.get(g, 0) + 1
        context["favorite_genres"] = sorted(
            genres_count, key=lambda item: item[1], reverse=True
        )[:4]
        return context


class LoginUser(View):
    ...
