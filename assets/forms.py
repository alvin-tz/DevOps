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
    os_type = forms.ChoiceField(label="操作系统类型", choices=os_type_choice)
    os_release = forms.CharField(label="操作系统版本", widget=forms.TextInput(attrs={'class': 'form-control'}))

    hostname = forms.CharField(label="主机名", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    alias = forms.CharField(label="主机别名", widget=forms.TextInput(attrs={'class': 'form-control'}))
    extranet_IP = forms.GenericIPAddressField(label="外网IP", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    intranet_IP = forms.GenericIPAddressField(label="内网IP", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ssh_port = forms.IntegerField(label="SSH端口", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    cpu = forms.IntegerField(label="CPU数量", widget=forms.TextInput(attrs={'class': 'form-control'}))
    ram = forms.FloatField(label="内存大小(GB)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    disk = forms.FloatField(label="磁盘大小(GB)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    network_bandwidth = forms.IntegerField(label="网络带宽(Mbps)", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    ssh_user = forms.CharField(label="远程登录用户", widget=forms.TextInput(attrs={'class': 'form-control'}))

    env_choice = (
        ('mainnet', '主网环境'),
        ('testnet', '测试网环境'),
        ('develop', '开发环境'),
        ('others', '其他环境'),
    )
    system = forms.ChoiceField(label="所属环境", choices=env_choice)