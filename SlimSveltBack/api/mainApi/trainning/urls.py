from django.urls import path

from . import views

urlpatterns = [
  path('trainning/', views.TrainningListView.as_view()),
  path('trainning/<int:id>/', views.TrainningListView.as_view()),
]