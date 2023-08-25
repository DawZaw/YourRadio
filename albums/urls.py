from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='albums'),
    path(
        '<slug:artist>/<slug:slug>/',
        views.AlbumDetailView.as_view(),
        name='album_detail',
    ),
    path('search_album/', views.search_album, name="search_album"),
]
