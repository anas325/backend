from .views import EventViewSet, TaskViewSet, ExpanseViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'expanses', ExpanseViewSet)

urlpatterns = [
    path('', views.events.as_view(), name='events'),
    path('participants/', views.participants.as_view(), name='participants'),
    path('create/', views.create_event.as_view(), name='create_event'),
    path('<int:id>/', views.detail_events.as_view(), name='detail_events'),
]



urlpatterns += router.urls