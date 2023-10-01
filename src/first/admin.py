from django.contrib import admin




# Register your models here.

from .models import *
 
admin.site.register(Username) 
admin.site.register(Orders) 
admin.site.register(Notification)
admin.site.register(Payment)  


