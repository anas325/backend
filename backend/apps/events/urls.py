from .views import EventViewSet, TaskViewSet, ExpanseViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'expenses', ExpanseViewSet)


urlpatterns = router.urls