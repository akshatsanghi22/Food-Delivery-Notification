from celery import Celery
import random

from celery import shared_task
import os

app= Celery('task',broker='redis://localhost:6379')

@shared_task
def test_func(self):
    for i in range(10):
        print(i)
    return('Done')    

@shared_task
def add(x, y):
    
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y )
    return total
def example_task(param1, param2):

    result = param1 + param2
    return result

def send_email_notification(subject, recipient, message):
    print(f"Sending email to {recipient}: {subject} - {message}")
    
@app.task
def send_sms_notification(phone_number, message):
    
    print(f"Sending SMS to {phone_number}: {message}")
    
@app.task
def send_push_notification(user_id, notification_data):
   
    print(f"Sending push notification to user {user_id}: {notification_data}")
           
#notification

from celery import shared_task

from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync

 

from celery import shared_task

from channels.layers import get_channel_layer

 

@shared_task

def send_realtime_notification(notification):

    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(

        "notifications_group",

        {

            "type": "send_notification",

            "message": notification,

        },

    )