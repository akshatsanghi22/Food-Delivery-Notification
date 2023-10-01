from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from first.tasks import test_func
from .tasks import example_task


def test(request):
     test_func.delay()
     return HttpResponse('Done')

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset=get_user_model().objects.all()
    
def my_view(request):
    param1 = 10
    param2 = 20
    
    # Trigger the Celery task asynchronously
    task_result = example_task.delay(param1, param2)
    
    return render(request, 'my_template.html', {'task_id': task_result.id})    




def index(request):
    return render(request, "index.html")

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})




# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from first.models import Notification
from first.serializers import NotificationSerializer

#models import from urls
from first.models import *
from django.http import HttpResponse
def celery_task(request):
    return HttpResponse("celery is working")

def username_list(request):
    username=Username.objects.all()
    return render (request, 'index1.html',{'username':username})


def orders_list(request):
    print('ORDERS VIEW')
    orders=Orders.objects.all()
    return render (request, 'orders.html',{'orders':orders})


def payment_list(request):
    payment=Payment.objects.all()
    return render (request, 'payment.html',{'payment':payment})











class NotificationListView(APIView):
    def get(self, request):
        notifications = Notification.objects.filter(user=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class NotificationDetailView(APIView):
    def get(self, request, notification_id):
        try:
            notification = notification.objects.get(id=notification_id, user=request.user)
        except notification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_200_OK)


    


from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


def sendMail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = cd['message']

            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'emailform.html', {

        'form': form,
        'messageSent': messageSent,

    })
    

# # appname/views.py
# from django.shortcuts import render, redirect
# from .forms import usernameForm

# def user_name(request):
#     if request.method == 'POST':
#         form = usernameForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # Redirect to a success page
#     else:
#         form = usernameForm()
#     return render(request, 'username.html', {'form': form})



from first.models import (Username,Orders)

def username(request):
    if request.method=="POST":
        name=request.POST.get('name')
        Email=request.POST.get('Email')
        password=request.POST.get('password')    
        ins=Username(name=name,Email=Email,password=password)
        ins.save()
    return render(request,'ai.html')   


# def order_table(request):
#     if request.method=="POST":
#         user_id =request.POST.get('user_id')
#         order_item=request.POST.get('order_item')
#         restaurant_name=request.POST.get('password')    
#         ins=Username(user_id=user_id,order_item=order_item,restaurant_name=restaurant_name)
#         ins.save()
#     return render(request,'ordertable.html')   


# from django.shortcuts import render
# from .forms import OrderForm

# def order_table(request):
#     form = OrderForm()
#     return render(request, 'ordertable.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Orders
from .models import Orders 
# Import your Order model

def order_table(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            order_item = form.cleaned_data['order_item']
            restaurant_name = form.cleaned_data['restaurant_name']
           # created_time=form.cleaned_data['created_time']
            order = Orders(user_id=user_id, order_item=order_item, restaurant_name=restaurant_name)
            order.save()
            
            return redirect('create-payment')  # Redirect to a success page
    else:
        form = OrderForm()
    
    return render(request, 'ordertable.html', {'form': form})



from django.shortcuts import render, redirect
from .forms import PaymentForm

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('send_email')  # Redirect to success page
    else:
        form = PaymentForm()
    
    return render(request, 'paymenttable.html', {'form': form})


from django.shortcuts import render
from .models import Notification



from django.shortcuts import render
from first.models import Username, Orders, Payment  




from django.shortcuts import render, redirect
from .models import Username, Orders, Payment, Notification
from .forms import NotificationForm
from first.tasks import send_realtime_notification



def notification_list(request):
    notifications=Notification.objects.all()
    return render(request,'notification_list.html',{'notifications':notifications})

def notificationpage(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            order_id = form.cleaned_data['order_id']
            payment_id = form.cleaned_data['payment_id']
            notification_text = form.cleaned_data['notification_text']
           # created_time=form.cleaned_data['created_time']
            abc = Notification(user_id=user_id, order_id=order_id,payment_id=payment_id, notification_text=notification_text)
            abc.save()
            Notification.objects.create(

                user_id=user_id,
                order_id=order_id,
                payment_id=payment_id,
                notification_text=notification_text
                )
            
            return redirect('notification-list')
            
             # Redirect to a success page
    else:
        form = NotificationForm()
    
    return render(request, 'notification_page.html', {'form': form})






#email
from django.core.mail.message import EmailMultiAlternatives

from django.conf import settings

from django.template.loader import render_to_string

from django.shortcuts import redirect, render

 
def send_email(request):

    if request.method=="POST":

        email_id = request.POST.get('email_id')

        response_data = "email send to "+email_id

        email_name = email_id.split('@')

 

        email_template = render_to_string(

            'email1.html', {"username": email_name[0]})

        email_obj = EmailMultiAlternatives(

            "Email Notification Example",

            "Email Notification Example",

            settings.EMAIL_HOST_USER,

            [email_id],

        )

        email_obj.attach_alternative(email_template, 'text/html')

        email_obj.send()

        context = {"data":response_data}

        return render(request,"notification_page.html",context)

    else:

        context = {"data":"response_data"}

        return render(request,"email.html")
    




def home(request):
   
    return render(request, 'realnotification.html')