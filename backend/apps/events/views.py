from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
# views.py
from rest_framework import generics
from .models import Event, Task, Expense
from .serializers import EventSerializer, TaskSerializer, expenseSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
# Create your views here.
from django.views import View
from backend.apps.users.models import User
from backend.apps.events.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return redirect('/')  # Redirect after creating
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return redirect('/events/')  

class expenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = expenseSerializer
    def create(self, request, *args, **kwargs):
            super().create(request, *args, **kwargs)
            return redirect(f'/events/{request.data["event"]}/')  # Redirect after creating


class events(LoginRequiredMixin, View):
    def get(self, request):
        events = Event.objects.all()
        logged_in_user = request.user
        last_expenses = Expense.objects.order_by('-date')[:5]
        return render(request, 'events.html', {"events": events,
                                            "user": logged_in_user,
                                            "expenses" : last_expenses
                                            })

class my_events(LoginRequiredMixin, View):
    def get(self, request):
        events = Event.objects.filter(organizer=request.user)
        last_expenses = Expense.objects.order_by('-date')[:5]
        return render(request, 'my_events.html', {"events": events, "user": request.user,
                                            "expenses" : last_expenses})

class create_event(LoginRequiredMixin, View):
    def get(self, request): 
        events = Event.objects.all()
        return render(request, 'create_event.html', {"events": events})

    
class detail_events(LoginRequiredMixin, View):
    def get(self, request, id):
        event = Event.objects.get(id=id)
        tasks = event.tasks.all()
        participants = event.participants.all()
        participants_count = len(participants) or 0
        participants = [participant.get_self_event(id) for participant in participants]
        expenses = event.expenses.all()
        logged_in_user = request.user
        total_expenses = 0
        for expense in expenses:
            total_expenses += expense.amount
        expense_proportion = 0
        if event.target_amount:
            expense_proportion = (total_expenses / event.target_amount) * 100
        else:
            expense_proportion = 0
        return render(request, 'detail_events.html', {"event": event,
                                            "user": logged_in_user,
                                            "tasks": tasks,
                                            "participants": participants,
                                            "expenses": expenses,
                                            "total_expenses": total_expenses,
                                            "expense_proportion": int(expense_proportion),
                                            "participants_count" : participants_count
                                            })


class participants(LoginRequiredMixin, View):
    def post(self, request):
        event_id = request.POST.get('event')
        event = Event.objects.get(id=event_id)
        id = event.id
        user = request.user
        if user not in event.participants.all():
            event.participants.add(user)
            event.save()
            event.organizer.notifications.create(
                user=user,
                message=f"{user.username} has joined the event {event.name}",
            )
        return redirect(f'/events/{id}/')
    

class event_expenses(View):
    def get(self, request, id):
        expenses = Event.objects.get(id=id).expenses
        expenses_json = list(expenses.values())
        return JsonResponse(expenses_json, safe=False)

class edit_event(LoginRequiredMixin, View):
    def get(self, request, id):
        event = Event.objects.get(id=id)
        return render(request, 'edit_event.html', {"event": event})

    def post(self, request, id):
        event = Event.objects.get(id=id)
        event.name = request.POST.get('name')
        event.description = request.POST.get('description')
        event.date = request.POST.get('date') or event.date  # Use existing date if not provided
        event.location = request.POST.get('location')
        event.target_amount = request.POST.get('target_amount')

        # Validate and save the event
        try:
            event.full_clean()  # Validate fields
            event.save()
            return redirect(f'/events/{id}/')
        except ValidationError as e:
            return render(request, 'edit_event.html', {"event": event, "errors": e.messages})


