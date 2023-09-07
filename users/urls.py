from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('<slug:username>/', views.UserDetailView.as_view(), name='user_detail'),
]
