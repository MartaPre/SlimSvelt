
from django.urls import path

from . import views

urlpatterns = [
  path('ingredients/', views.IngredientsListView.as_view()),
  path('ingredients/<int:id>/', views.IngredientsListView.as_view()),
]