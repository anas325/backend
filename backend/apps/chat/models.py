from django.db import models
from datetime import datetime


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now , blank = True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='messages_sent')
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='related_messages')
    def __str__(self):
        return self.value +f'({self.user})'
