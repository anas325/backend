from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return redirect('/')  # Redirect after creating
