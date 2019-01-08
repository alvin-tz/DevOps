#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 16:51
# @Author  : Alvin
# @File    : forms.py
from django import forms


class AddserverForm(forms.Form):
    os_type_choice = (
        ('Linux', 'Linux'),
        ('Windows', 'Windows'),
    )
    # os_type_choice = ('Linux', 'Windows')
    os_type = forms.ChoiceField(label="操作系统类型", choices=os_type_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    os_release = forms.CharField(label="操作系统版本", widget=forms.TextInput(attrs={'class': 'form-control'}))

    hostname = forms.CharField(label="主机名", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    alias = forms.CharField(label="主机别名", widget=forms.TextInput(attrs={'class': 'form-control'}))
    extranet_IP = forms.CharField(label="外网IP", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    intranet_IP = forms.CharField(label="内网IP", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ssh_port = forms.IntegerField(label="SSH端口", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    cpu = forms.IntegerField(label="CPU数量", widget=forms.TextInput(attrs={'class': 'form-control'}))
    ram = forms.FloatField(label="内存大小(GB)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    disk = forms.FloatField(label="磁盘大小(GB)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    network_bandwidth = forms.CharField(label="网络带宽(Mbps)", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    ssh_user_root_password = forms.CharField(label="root用户密码", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    ssh_user_other = forms.CharField(label="其他远程登录用户", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ssh_user_other_password = forms.CharField(label="其他远程用户密码", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    env_choice = (
        ('mainnet', '主网环境'),
        ('testnet', '测试网环境'),
        ('develop', '开发环境'),
        ('others', '其他环境'),
    )
    # env_choice = ('其他环境', '主网环境', '测试网环境', '开发环境')
    system = forms.ChoiceField(label="所属环境", choices=env_choice, initial='others', widget=forms.Select(attrs={'class': 'form-control'}))


# class ExecuteForm(forms.Form):
#     servers = forms.CharField(label="执行命令的服务器", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label="主机密码", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     server_id = forms.CharField(label="服务器ID")