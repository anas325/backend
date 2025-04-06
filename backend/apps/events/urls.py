from .views import EventListCreate
from django.urls import path


urlpatterns = [
    path('', EventListCreate.as_view(), name='event-list-create'),
]