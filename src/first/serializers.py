from rest_framework import serializers
from django.contrib.auth import get_user_model
from . models import Username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Username
        
        fields =['email','password','is_verified']
        

# serializers.py models 

from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

        