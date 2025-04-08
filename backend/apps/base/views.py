

# Create your views here.
from django.shortcuts import render
from django.views import View
from backend.apps.users.models import User
from backend.apps.events.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin


class home1(LoginRequiredMixin, View):
    def get(self, request):
        logged_in_user = request.user
        return render(request, 'home1.html',{"user" : logged_in_user})
 
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

class user_profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user_profile.html', {})

class profile(LoginRequiredMixin, View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'user_profile.html',{'user' : user})