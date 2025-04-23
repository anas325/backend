

# Create your views here.
from django.shortcuts import render
from django.views import View
from backend.apps.users.models import User
from backend.apps.events.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin


class home1(LoginRequiredMixin, View):
    def get(self, request):
        all_events = Event.objects.all()
        logged_in_user = request.user
        upcomming_events = [event for event in all_events if (logged_in_user in event.participants.all() or logged_in_user == event.organizer)]
        event_count = len(upcomming_events)
        paticipants = [event.participants.all() for event in all_events]
        participant_count = len(set(participant for sublist in paticipants for participant in sublist))
        total_expenses = sum(logged_in_user.payed_expenses.filter(event__in=all_events).values_list('amount', flat=True))

        return render(request, 'home1.html',{"user" : logged_in_user,
                                            "event_count": event_count,
                                            "participant_count": participant_count,
                                            "total_expenses": total_expenses,
                                            "events": upcomming_events[-4:-1] if len(upcomming_events) > 4 else upcomming_events,
                                            })

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



class profile(LoginRequiredMixin, View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'user_profile.html',{'user' : user})
    
class detail_events(LoginRequiredMixin, View):
    def get(self, request, id):
        event = Event.objects.get(id=id)
        logged_in_user = request.user
        return render(request, 'detail_events.html', {"event": event,
                                                    "user": logged_in_user
                                                    })
    
class notification(LoginRequiredMixin, View):
    def get(self, request):
        logged_in_user = request.user
        notifications = logged_in_user.notifications.all().order_by('-created_at')
        return render(request, 'notifications.html', {"user": logged_in_user,
                                                    "notifications": notifications,
                                                    })
    def post(self, request):
        logged_in_user = request.user
        notification_id = request.POST.get('notification_id')
        notification = logged_in_user.notifications.get(id=notification_id)
        notification.is_read = True
        notification.save()
        notifications = logged_in_user.notifications.all().order_by('-created_at')
        
        return render(request, 'notifications.html', {
            "user": logged_in_user,
            "notifications": notifications,
        })


