

# Create your views here.
from django.shortcuts import render
from django.views import View
from backend.apps.users.models import User
from backend.apps.events.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin


class home1(View,LoginRequiredMixin):
    def get(self, request):
        logged_in_user = request.user
        return render(request, 'home1.html',{"user" : logged_in_user})
 
class events(View,LoginRequiredMixin):
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'events.html',{"events" : events})

class create_event(View,LoginRequiredMixin):
    def get(self, request):
        return render(request, 'create_event.html',{})

class user_profile(View,LoginRequiredMixin):
    def get(self, request):
        return render(request, 'user_profile.html',{})


class profile(View,LoginRequiredMixin):
     def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'user_profile.html',{'user' : user})