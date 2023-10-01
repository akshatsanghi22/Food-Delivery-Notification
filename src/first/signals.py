from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from first.models  import Notification

@receiver(post_save, sender=Notification)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # trigger notification to all consumers in the 'user-notification' group
        channel_layer = get_channel_layer()
        group_name = 'user-notifications'
        event = {
            "type": "user_joined",
            "text": instance.user_id
        }
        async_to_sync(channel_layer.group_send)(group_name, event)


###notification

from django.db.models.signals import post_save
from django.dispatch import receiver
from first.models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):


    if created:
        channel_layer = get_channel_layer()
        group_name = 'src'
        event = {
            'type': 'notify',
            'notification_id': instance.notification_id,
            'user_id': instance.user_id,
            'order_id': instance.order_id,
            'notification_text': instance.notification_text,
        }
        async_to_sync(channel_layer.group_send)(group_name,event)
