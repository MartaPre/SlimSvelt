
from django.urls import path

from . import views

urlpatterns = [
  path('dietary/', views.DietaryListView.as_view()),
  path('dietary/<int:id>/', views.DietaryListView.as_view()),
]