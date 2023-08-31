from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users'),
    path('<slug:username>/', views.UserDetailView.as_view(), name='user_detail'),
]
