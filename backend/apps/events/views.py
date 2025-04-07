from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Event, Task, Expense
from .serializers import EventSerializer, TaskSerializer, ExpanseSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return redirect('/')  # Redirect after creating
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

class ExpanseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpanseSerializer
    permission_classes = [AllowAny]
