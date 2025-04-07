

# Create your views here.
from django.shortcuts import render
from django.views import View
from backend.apps.users.models import User

class home1(View):
    def get(self, request):
        return render(request, 'home1.html',{})
class events(View):
    def get(self, request):
        return render(request, 'events.html',{})
class create_event(View):
    def get(self, request):
        return render(request, 'create_event.html',{})
class user_profile(View):
    def get(self, request):
        return render(request, 'user_profile.html',{})


class profile(View):
     def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'user_profile.html',{'user' : user})