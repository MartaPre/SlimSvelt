
from django.urls import path

from . import views

urlpatterns = [
  path('recipes_user/', views.RecipesUserListView.as_view()),
  path('recipes_user/<int:id>/', views.RecipesUserListView.as_view()),
]