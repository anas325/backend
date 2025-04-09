from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Event, Task, Expense
from .serializers import EventSerializer, TaskSerializer, ExpanseSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
# Create your views here.
from django.views import View
from backend.apps.users.models import User
from backend.apps.events.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin

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


class events(LoginRequiredMixin, View):
    def get(self, request):
        events = Event.objects.all()
        logged_in_user = request.user
        organizer = User.objects.filter(id__in=events.values_list('organizer', flat=True))
        return render(request, 'events.html', {"events": events,
                                            "user": logged_in_user,
                                            "organizer": organizer[0]
                                            })

class create_event(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'create_event.html', {})

    
class detail_events(LoginRequiredMixin, View):
    def get(self, request, id):
        event = Event.objects.get(id=id)
        logged_in_user = request.user
        return render(request, 'detail_events.html', {"event": event,"user": logged_in_user})