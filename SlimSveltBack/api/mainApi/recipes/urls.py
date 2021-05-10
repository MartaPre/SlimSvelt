
from django.urls import path

from . import views

urlpatterns = [
  path('recipes/', views.RecipesListView.as_view()),
  path('recipes/<str:recipe_type>/', views.RecipesListView.as_view()),
  path('recipes/<str:recipe_type>/<int:recipes_id>/', views.RecipesListView.as_view()),
]