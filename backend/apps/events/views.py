from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
