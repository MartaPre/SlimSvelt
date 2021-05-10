
from django.urls import include, path

from . import views

urlpatterns = [
  path('getUser/', views.UsersListView.as_view()),
  path('getUser/<str:email>/', views.UsersListView.as_view()),
  path('auth/', include('rest_auth.urls')),    
  path('auth/register/', include('rest_auth.registration.urls'))
]