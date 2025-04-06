from .views import EventViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', EventViewSet)

urlpatterns = router.urls