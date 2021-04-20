from django.contrib import admin
from django.urls import path,include


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('users.urls')),
  path('', include('trainning.urls')),
  path('', include('recipes.urls')),
  path('', include('dietary.urls')),
  path('', include('trainning_diary.urls')),
]