# accounts/utils.py

import random
import string
from django.core.mail import send_mail
from django.conf import settings

# def generate_otp(length=6):
#     characters = string.digits
#     otp = ''.join(random.choice(characters) for _ in range(length))
#     return otp

def send_email_token(email, token):
    try:
        
        subject = 'Your Account need to be verified'
        message = f'Click on the link to verify http://127.0.0.1:8000/verify/{token}/'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list) 
    
    except Exception as e:
        return False
    
    return True