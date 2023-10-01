from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


# from django import forms
# from .models import (Username,Orders,Payment,Notification)

# class usernameForm(forms.ModelForm):
#     class Meta:
#         model = Username
#         fields = ['Email', "is_verified","otp",]    


# class ordersForm(forms.ModelForm):
#     class Meta:
#         model = Orders
#         fields = [ 'order_date', "created_at"] 
        

# class paymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = ['payment_status'] 


# class notificationForm(forms.ModelForm):
#     class Meta:
#         model = Notification
#         fields = []                         

from django import forms
from .models import Username  # Use your user model

class OrderForm(forms.Form):
    user_id = forms.ModelChoiceField(queryset=Username.objects.all(), empty_label="Select a user")
    order_item = forms.CharField(max_length=100)
    restaurant_name = forms.CharField(max_length=100)
    

from django import forms
from .models import Payment,Orders

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user_id', 'payment_status', 'payment_amount']    



from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['user_id', 'order_id', 'payment_id','notification_text']        

    user_id = forms.ModelChoiceField(queryset=Username.objects.all())
    
    # Define order_id as a ChoiceField with custom choices
    #order_id = forms.ChoiceField(choices=[(order_id, order_id) for order in Orders.objects.all()])
    
    payment_id = forms.ModelChoiceField(queryset=Payment.objects.all())    