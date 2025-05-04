from rest_framework import serializers
from .models import Event
from .models import Task, Expense

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' 
class TaskSerializer(serializers.ModelSerializer):
            class Meta:
                model = Task
                fields = '__all__'

class expenseSerializer(serializers.ModelSerializer):
            class Meta:
                model = Expense
                fields = '__all__'