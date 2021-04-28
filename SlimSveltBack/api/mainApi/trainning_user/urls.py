from django.urls import path

from . import views

urlpatterns = [
  path('trainning_user/', views.TrainningUserListView.as_view()),
  path('trainning_user/<int:id>/', views.TrainningUserListView.as_view()),
]