from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('<int:id>/', views.profile.as_view(), name='user_profile'),
    
]