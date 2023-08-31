from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='artists'),
    path('search/', views.search_view, name='search'),
    path(
        '<slug:artist>/<slug:slug>/',
        views.AlbumDetailView.as_view(),
        name='album_detail',
    ),
    path('<slug:slug>/', views.ArtistDetailView.as_view(), name='artist_detail'),
]
