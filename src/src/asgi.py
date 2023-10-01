# import os

 

# from channels.auth import AuthMiddlewareStack

# from channels.routing import ProtocolTypeRouter, URLRouter

# from channels.security.websocket import AllowedHostsOriginValidator

# from django.core.asgi import get_asgi_application

 

# from first.routing import websocket_urlpatterns

 

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

# # Initialize Django ASGI application early to ensure the AppRegistry

# # is populated before importing code that may import ORM models.

# django_asgi_app = get_asgi_application()

 

# import first.routing

 

# application = ProtocolTypeRouter(

#     {

#         "http": django_asgi_app,

#         "websocket": AllowedHostsOriginValidator(

#             AuthMiddlewareStack(URLRouter(websocket_urlpatterns))

#         ),

#     }

# )


# import os

# from channels.routing import ProtocolTypeRouter
# from django.core.asgi import get_asgi_application
# import first.routing

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         # Just HTTP for now. (We can add other protocols later.)
#         "websocket": AllowedHostsOriginValidator(
#             AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
#         ),
#     }
# )
    
import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application


#from first.routing import websocket_urlpatterns
from django.urls import path
from first.consumers import NotificationConsumer
from first.urls import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

import first.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket":AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    

        
    }
)    
    

