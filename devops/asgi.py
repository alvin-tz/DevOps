#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 16:51
# @Author  : Alvin
# @File    : asgi.py
import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings")
django.setup()
application = get_default_application()