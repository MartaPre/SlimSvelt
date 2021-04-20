
from django.urls import path

from . import views

urlpatterns = [
  path('recipes/', views.RecipesListView.as_view()),
  path('recipes/<int:id>/', views.RecipesListView.as_view()),
]