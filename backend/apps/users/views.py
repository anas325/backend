from django.shortcuts import render
from django.views import View
from backend.apps.users.models import User
from backend.apps.events.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin


class profile(LoginRequiredMixin, View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'user_profile.html',{'user' : user})
    
