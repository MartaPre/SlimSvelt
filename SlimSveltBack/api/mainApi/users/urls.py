
from django.urls import path

from . import views

urlpatterns = [
  path('users/', views.UsersListView.as_view()),
  path('users/<int:id>/', views.UsersListView.as_view()),
]