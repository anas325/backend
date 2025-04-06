from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
