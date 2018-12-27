#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 18:10
# @Author  : Alvin
# @File    : server.py
from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from devops.wsgi import application

print('DevOps is running ......')

ws_server = WSGIServer(
    ('127.0.0.1', 8000),
    application,
    log=None,
    handler_class=WebSocketHandler
)

try:
    ws_server.serve_forever()
except KeyboardInterrupt:
    print('服务器关闭 ......')
    pass
