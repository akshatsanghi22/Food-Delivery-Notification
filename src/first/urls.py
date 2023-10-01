from django.contrib import admin
from django.urls import path, include

from . import views

from first.views import * 
from django.contrib import admin
from django.urls import path
from first.models import (Username,Orders)
from first.consumers import NotificationConsumer
from . import consumers

# from first.views import user_idListView
urlpatterns = [
    #path('', views.test,name='test'),
    path("index/", views.index, name="index"),
    path("chat/<str:room_name>/", views.room, name="room"),
    #path("chat/",views.room, name='room'),
    path('', views.username, name='username'),
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/Payment/', views.payment_list, name='payment_list'),
    path('notification/', views.notification_list, name='notification_list'),
    #path('home/',views.home,name='home'),
    #path('verify/',views.verify,name='verify'),
    path('email/', sendMail),
    #path('user_name/', views.user_name, name='user_name'),
    
    
    
    path('username/',views.username,name='username'),
    path('ordertable/',views.order_table,name='order_table'),
    path('create-payment/', views.create_payment, name='create-payment'),
    #path('notifications/', views.notification_page, name='notification-page'),
    path('notificationpage/', views.notificationpage,name='notificationpage'),
    path('notification-list/',views.notification_list,name='notification-list'),
    
    #notification feature
    # path('home/',views.home,name='home'),
    # path('test/',views.test,name='home'),
    #email
    path("send-email/",views.send_email,name='send_email'),


    ###notification
    path('home/', views.home, name='home'),


   
   

]

websocket_urlpatterns = [
    path('ws/notifications', consumers.NotificationConsumer.as_asgi()),
]