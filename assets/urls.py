#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 18:01
# @Author  : Alvin
# @File    : urls.py
# from django.conf.urls import url
from django.urls import path
from assets import views
app_name = 'assets'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/<server_id>/', views.detail, name='detail'),
    path('addserver/', views.addserver, name='addserver'),
    path('modify/<server_id>', views.modify, name='modify'),
    path('deleteserver/<server_id>', views.deleteserver, name='deleteserver'),
    path('', views.dashboard),
    # path('webssh/<server_id>', views.connect, name='connect'),
]