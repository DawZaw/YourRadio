from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from albums.models import Album


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album_list"] = Album.objects.all()[:]
        return context
