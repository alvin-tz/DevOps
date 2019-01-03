"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from login import views as views
# from assets import views as assetsviews
from django.conf.urls import include
# app_name = 'assets'

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('login/index/', views.index),
    path('login/', views.login),
    path('', views.login),
    path('login/register/', views.register),
    path('logout/', views.logout),
    path('login/captcha', include('captcha.urls')),
    path('login/confirm/', views.user_confirm),

    path('assets/', include('assets.urls'))
]
