#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 16:50
# @Author  : Alvin
# @File    : routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ProtocolTypeRouter
from django.urls import path

import websocket

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("webssh/", websocket.WebSSH),
        ])
    )
})