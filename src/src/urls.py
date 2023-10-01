
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.routers import DefaultRouter
from first.views import UserViewSet
from first.views import *
# from .views import webpushnotification, send_push
# from django.conf import settings
# from django.conf.urls.static import static
from first.urls import urlpatterns as first_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('first.urls')),
    # path('index/', include('first.urls')),
    # path("chat/", include("first.urls")),
    # path('verify/',include('first.urls')),
    # path('home/',include('first.urls')),
    # path('orders/', include('first.urls')),
    # path('payment/', include('first.urls')),
    # path('notification/', include('first.urls')),
    #path('register/', RegisterAPI.as_view()),
    # path('email/', include('first.urls')),
    path('home/', include(first_urls)),

    
]

router = DefaultRouter()
router.register('user',UserViewSet, basename='user')

urlpatterns += router.urls
