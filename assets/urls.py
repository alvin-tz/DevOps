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
    path('detail/(?P<server_id>[0-9]+)/', views.detail, name='detail'),
    path('addserver/', views.addserver, name='addserver'),
    # path('modify/', views.modify, name='modify'),
    path('', views.dashboard),
]