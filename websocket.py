#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 17:24
# @Author  : Alvin
# @File    : websocket.py
from channels.generic.websocket import WebsocketConsumer
from ssh import SSH
from django.http.request import QueryDict
from assets import models
from django.utils.six import StringIO
import json
# import base64
from django.shortcuts import get_object_or_404


class WebSSH(WebsocketConsumer):
    message = {'status': 0, 'message': None}
    """
    status:
        0: ssh 连接正常, websocket 正常
        1: 发生未知错误, 关闭 ssh 和 websocket 连接
    message:
        status 为 1 时, message 为具体的错误信息
        status 为 0 时, message 为 ssh 返回的数据, 前端页面将获取 ssh 返回的数据并写入终端页面
    """

    def connect(self):
        try:
            self.accept()
            query_string = self.scope['query_string']
            connet_argv = QueryDict(query_string=query_string, encoding='utf-8')
            server_id = connet_argv.get('server_id')
            width = connet_argv.get('width')
            height = connet_argv.get('height')

            width = int(width)
            height = int(height)

            connect_info = get_object_or_404(models.Server, id=server_id)

            host = connect_info.alias
            port = connect_info.ssh_port
            user = 'root'
            # auth = ''
            pwd = connect_info.ssh_user_root_password
            # pkey = ''

            # connect_info.delete()

            # if pwd:
            #     # password = base64.b64decode(pwd).decode('utf-8')
            #     password = pwd
            # else:
            #     password = None

            self.ssh = SSH(websocker=self, message=self.message)

            self.ssh.connect(
                host=host,
                user=user,
                password=pwd,
                port=port,
                pty_width=width,
                pty_height=height
            )

            # if auth == 'key':
            #     pkey = pkey
            #     obj = StringIO()
            #     obj.write(pkey)
            #     obj.flush()
            #     obj.seek(0)
            #     self.pkey = obj
            #
            #     self.ssh.connect(
            #         host=host,
            #         user=user,
            #         password=password,
            #         pkey=self.pkey,
            #         port=port,
            #         pty_width=width,
            #         pty_height=height
            #     )
            # else:
            #     self.ssh.connect(
            #         host=host,
            #         user=user,
            #         password=password,
            #         port=port,
            #         pty_width=width,
            #         pty_height=height
            #     )
        except Exception as e:
            self.message['status'] = 1
            self.message['message'] = str(e)
            message = json.dumps(self.message)
            self.send(message)
            self.close()

    def disconnect(self, close_code):
        try:
            self.ssh.close()
        except:
            pass

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if type(data) == dict:
            status = data['status']
            if status == 0:
                data = data['data']
                self.ssh.shell(data)
            else:
                cols = data['cols']
                rows = data['rows']
                self.ssh.resize_pty(cols=cols, rows=rows)