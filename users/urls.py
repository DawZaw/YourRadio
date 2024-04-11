from django.urls import path, include
from . import views

app_name = "users"
urlpatterns = [
    path("", views.UsersListView.as_view(), name="users"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("<slug:username>/", views.UserDetailView.as_view(), name="user_detail"),
    path("<int:user_id>/add_album/<int:album_id>", views.add_album, name="add_album"),
    path(
        "<int:user_id>/remove_album/<int:album_id>",
        views.remove_album,
        name="remove_album",
    ),
]
