from .views import EventViewSet, TaskViewSet, expenseViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'expenses', expenseViewSet,)

urlpatterns = [
    path('', views.events.as_view(), name='events'),
    path('mine/', views.my_events.as_view(), name='my_events'),
    path('participants/', views.participants.as_view(), name='participants'),
    path('create/', views.create_event.as_view(), name='create_event'),
    path('<int:id>/', views.detail_events.as_view(), name='detail_events'),
    path('get_expenses/<int:id>/', views.event_expenses.as_view(), name='expense_api')
]



urlpatterns += router.urls