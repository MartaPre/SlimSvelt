
from django.urls import path

from . import views

urlpatterns = [
  path('recipes_user/', views.RecipesUserListView.as_view()),
  path('recipes_user/<int:user_id>/', views.RecipesUserListView.as_view()),
]