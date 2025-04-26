from .models import Message
from django.http import HttpResponse , JsonResponse
from backend.apps.users.models import User
from backend.apps.events.models import Event
# Create your views here.

    

def send(request):
    message = request.POST['message']
    uid = request.POST['user_id']
    event_id = request.POST['room_id']
    user = User.objects.get(id = uid)
    event = Event.objects.get(id = event_id)

    new_message = Message.objects.create(value= message , user = user , event = event)
    new_message.save()
    return HttpResponse('Message envoyé avec succès')

def getMessages(request , id):
    messages = Message.objects.filter(event = id).order_by('date').values()
    
    for message in messages :
        message['user'] = User.objects.get(id=message['user_id']).username
        message['profile_picture'] = User.objects.get(id=message['user_id']).profile_picture.url
    
    return JsonResponse({"messages" :list(messages)}) if messages else JsonResponse({"messages" :[]})