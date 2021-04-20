from django.urls import path

from . import views

urlpatterns = [
  path('trainning_diary/', views.TrainningDiaryListView.as_view()),
  path('trainning_diary/<int:id>/', views.TrainningDiaryListView.as_view()),
]