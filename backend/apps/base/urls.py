from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home1.as_view(), name='home'),
    #path('', views.about.as_view(), name='about'),
    path('user_profile/', views.user_profile.as_view(), name='user_profile'),
    path('events/', views.events.as_view(), name='events'),
    path('create_event/', views.create_event.as_view(), name='create_event'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('user/<int:id>/', views.profile.as_view(), name='user_profile'),
]