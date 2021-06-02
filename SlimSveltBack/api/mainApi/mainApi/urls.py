from django.contrib import admin
from django.urls import path,include



urlpatterns = [
  path('admin/', admin.site.urls),
  path('admin_tools_stats/', include('admin_tools_stats.urls')),
  path('', include('users.urls')),
  path('', include('trainning.urls')),
  path('', include('recipes.urls')),
  path('', include('recipes_user.urls')),
  path('', include('ingredients.urls')),
  path('', include('trainning_user.urls')),
]