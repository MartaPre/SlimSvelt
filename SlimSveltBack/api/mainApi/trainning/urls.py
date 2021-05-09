from django.urls import path

from . import views

urlpatterns = [
  path('trainning/', views.TrainningListView.as_view()),
  path('trainning/<str:exercise_type>/', views.TrainningListView.as_view()),
  path('trainning/<str:exercise_type>/<int:trainning_id>/', views.TrainningListView.as_view()),
]