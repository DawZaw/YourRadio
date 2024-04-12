from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.forms import UserCreationForm
import datetime

from comments.models import Comment
from artists.models import Album
from .forms import RegisterUserForm
from .models import SiteUser


class UsersListView(ListView):
    model = SiteUser
    template_name = "users/users_list.html"

    class Meta:
        ordering = "username"

    def get_queryset(self):
        return SiteUser.objects.exclude(is_superuser=True)

from django.utils.text import slugify

class UserDetailView(DetailView):
    model = SiteUser
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/user_detail.html"

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
        
        # Comment section
        slug = slugify(self.get_object())
        comments = Comment.objects.filter(page=slug)
        paginator = Paginator(comments, 5)
        page = self.request.GET.get("page", 1)
        comments = paginator.get_page(page)
        context["comments"] = comments
        
        return context


class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = RegisterUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)


def add_album(request, **kwargs):
    if request.method == "POST":
        album = Album.objects.get(id=kwargs["album_id"])
        user = SiteUser.objects.get(id=kwargs["user_id"])
        user.favorite_albums.add(album)
        messages.info(request, "Album added to favorites.")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def remove_album(request, **kwargs):
    if request.method == "POST":
        album = Album.objects.get(id=kwargs["album_id"])
        user = SiteUser.objects.get(id=kwargs["user_id"])
        user.favorite_albums.remove(album)
        messages.info(request, "Album removed from favorites.")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
