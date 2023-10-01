from django.apps import AppConfig


class DjangoNotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first'



###notification

class NotificationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first'

    def ready(self):
        """
        Initializes the object and imports the necessary signals from the notification_app module.
        """
        import first.signals
