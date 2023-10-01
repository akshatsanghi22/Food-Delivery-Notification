from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import UserManager
import random


# Create your models here.
class Username(models.Model):
    name = models.CharField(max_length=20,default='Your name')
    user_id=models.AutoField(primary_key=True,editable=False,)
    Email=models.EmailField(max_length=254)
    password=models.CharField(max_length=30,default=random.randint(1,100))
    

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# from django.db import models

 

# class CustomUserManager(BaseUserManager):

#     def create_user(self, email, password=None, **extra_fields):

#         if not email:

#             raise ValueError('The Email field must be set')

#         email = self.normalize_email(email)

#         user = self.model(email=email, **extra_fields)

#         user.set_password(password)

#         user.save(using=self._db)

#         return user

 

#     def create_superuser(self, email, password=None, **extra_fields):

#         extra_fields.setdefault('is_staff', True)

#         extra_fields.setdefault('is_superuser', True)

 

#         return self.create_user(email, password, **extra_fields)

 

# class User(AbstractBaseUser, PermissionsMixin):

#     email = models.EmailField(unique=True)

#     first_name = models.CharField(max_length=30, blank=True)

#     last_name = models.CharField(max_length=30, blank=True)

#     date_joined = models.DateTimeField(auto_now_add=True)

#     is_active = models.BooleanField(default=True)

#     is_staff = models.BooleanField(default=False)

 

#     objects = CustomUserManager()

 

#     USERNAME_FIELD = 'email'

#     REQUIRED_FIELDS = []

 

#     def __str__(self):

#         return self.email



#EMAIL

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     otp = models.CharField(max_length=6, null=True, blank=True)
#     # Add the otp field here

#     # Add custom fields here, if needed

#     def __str__(self):
#         return self.username
    

# class Profile(models.Model):
#     user=models.OneToOneField(Username,on_delete=models.CASCADE)
#     email_token=models.CharField(max_length=200)
#     is_verified=models.BooleanField(default=False)
    
    

from datetime import datetime

#models
class Username(models.Model):
    name = models.CharField(max_length=20,default='Your name')
    user_id=models.AutoField(primary_key=True,editable=False,)
    Email=models.EmailField(max_length=254)
    password=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name    


class Orders(models.Model):
    user_id = models.ForeignKey(Username, on_delete=models.CASCADE)
    order_id = models.AutoField(editable=False,primary_key=True)
    order_date = models.DateField(auto_now=True)
    #created_time = models.TimeField(auto_now=True,default='07:50')   
    order_item=models.CharField(max_length=100,default='pizza') 
    restaurant_name=models.CharField(max_length=50, default='SST')    
    
    def __str__(self):
        return str(self.order_id)
    
class Payment(models.Model):
    payment_id=models.AutoField(editable=False,primary_key=True)
    user_id=models.ForeignKey(Username, on_delete=models.CASCADE)
    PAYMENT_STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('processing', 'Processing'),
        ('declined', 'Declined'),
    ]
    payment_status=models.CharField(max_length=10,choices=PAYMENT_STATUS_CHOICES,default='processing')
    payment_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0,)
    
    def __str__(self):
        return str(self.payment_id)
    
class Notification(models.Model):
    notification_id=models.AutoField(primary_key=True,editable=False,)
    user_id = models.ForeignKey(Username, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    # notification_receive_time=models.DateTimeField(auto_now_add=True)
    # notification_read_time=models.DateTimeField(auto_now=True)
    payment_id=models.ForeignKey(Payment,on_delete=models.CASCADE,default='DEFAULT VALUE')
    #payment_status=models.ForeignKey(Payment,on_delete=models.CASCADE,default='processing')
    notification_text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.order_id 
    def __int__(self):
        return self.payment_id
    

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import MINUTES,PeriodicTask,CrontabSchedule,PeriodicTasks
import json


# @receiver(post_save, sender=Notification)

# def notification_handler(sender, instance, created, **kwargs):
#     # call group_send function directly to send notificatoions or you can create a dynamic task in celery beat
#     if created:
#         schedule, created = CrontabSchedule.objects.get_or_create(hour=instance.created_at.hour,minute=instance.created_at.minute,day_of_month=instance.created_at.day,month_of_year=instance.created_at.month)
#         task = PeriodicTask.objects.create(crontab=schedule, name="broadcast-notification-"+str(instance.notification_id), task="notification.tasks.broadcast_notification", args=json.dumps((instance.notification_id,)))

#     #if not created: