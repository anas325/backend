

# Create your views here.
from django.shortcuts import render
from django.views import View
from backend.apps.users.models import User

class home(View):
    def get(self, request):
        return render(request, 'home1.html',{})


class profile(View):
     def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'user_profile.html',{'user' : user})