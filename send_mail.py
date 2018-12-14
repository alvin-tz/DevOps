#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 14:29
# @Author  : Alvin
# @File    : send_mail.py
import os
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'devops.settings'

if __name__ == '__main__':
    # send_mail(
    #     'devops test email',
    #     'This is a test email from DevOps!',
    #     'tz466731927@126.com',
    #     ['tangzheng@nuls.io'],
    # )
    subject, from_email, to = 'devops test email', 'tz466731927@126.com', 'tangzheng@nuls.io'
    text_content = 'This is a test email from DevOps! http://127.0.0.1:8000/login'
    html_content = '<p>This is a test email from DevOps! <a href="http://127.0.0.1:8000/login" target=blank>http://127.0.0.1:8000/login</a></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()