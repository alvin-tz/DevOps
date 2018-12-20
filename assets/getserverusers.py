#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 19:58
# @Author  : Alvin
# @File    : getserverusers.py
# from django import template
from assets.models import Server, ServerUser

from django.db.models.aggregates import Count


# register = template.Library()

# @register.simple_tag
def getserverusers(server_id):
    serverusers = ServerUser.objects.filter(server_id=server_id)
    # return Server.objects.annotate(num_serverusers=Count('serveruser')).filter(num_serverusers__gt=0)
    return serverusers