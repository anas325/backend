from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('send', views.send , name ="send"),
    path('getMessages/<int:id>/', views.getMessages , name ="getMessages")
]