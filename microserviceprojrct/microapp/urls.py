"""microproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'account', AccountUpdateViewSet, basename='user')

urlpatterns = [
    path('register/',register_user,name='register'),
    path('password-reset/',password_reset_mode,name='password_reset_mode'),
    path('send-otp/',send_otp,name='send_otp'),
    path('verify-otp/',verify_otp,name='verify_otp'),
    path('', include(router.urls)),

]
