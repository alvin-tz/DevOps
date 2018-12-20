from django.shortcuts import render
from django.shortcuts import get_object_or_404
from assets import models
from assets import forms
from login import models as loginmodels
from assets import getserverusers

# Create your views here.


def index(request):

    servers = models.Server.objects.all()
    return render(request, 'assets/index.html', locals())


def dashboard(request):
    total = models.Server.objects.count()
    mainnet = models.Server.objects.filter(system='mainnet').count()
    testnet = models.Server.objects.filter(system='testnet').count()
    develop = models.Server.objects.filter(system='develop').count()
    others = models.Server.objects.filter(system='others').count()

    mainnet_rate = round(mainnet/total*100)
    testnet_rate = round(testnet/total*100)
    develop_rate = round(develop/total*100)
    others_rate = round(others/total*100)

    # user = loginmodels.User.objects.get()

    return render(request, 'assets/dashboard.html', locals())


def detail(requset, server_id):
    """
    以显示服务器类型资产详细为例，安全设备、存储设备、网络设备等参照此例。
    :param request:
    :param asset_id:
    :return:
    """
    server = get_object_or_404(models.Server, id=server_id)
    # serverusers = get_object_or_404(models.ServerUser, server_id=server_id)
    return render(requset, 'assets/detail.html', locals())

def addserver(request):
    if request.method == "POST":
        addserver_form = forms.AddserverForm(request.POST)
        message = ""
        if addserver_form.is_valid():    # 获取数据
            os_type = addserver_form.cleaned_data['os_type']
            os_release = addserver_form.cleaned_data['os_release']
            hostname = addserver_form.cleaned_data['hostname']
            alias = addserver_form.cleaned_data['alias']
            extranet_IP = addserver_form.cleaned_data['extranet_IP']
            intranet_IP = addserver_form.cleaned_data['intranet_IP']
            ssh_port = addserver_form.cleaned_data['ssh_port']
            cpu = addserver_form.cleaned_data['cpu']
            ram = addserver_form.cleaned_data['ram']
            disk = addserver_form.cleaned_data['disk']
            network_bandwidth = addserver_form.cleaned_data['network_bandwidth']
            ssh_user = addserver_form.cleaned_data['ssh_user']
            system = addserver_form.cleaned_data['system']

            same_alias = models.Server.objects.filter(alias = alias)
            if same_alias:  #主机别名唯一
                message = "主机别名已经存在，请重新输入！"
                return render(request, 'assets/addserver.html', locals())

            # 当一切都OK的情况下，创建新记录
            new_server = models.Server()
            new_server.os_type = os_type
            new_server.os_release = os_release
            new_server.hostname = hostname
            new_server.alias = alias
            new_server.extranet_IP = extranet_IP
            new_server.intranet_IP = intranet_IP
            new_server.ssh_port = ssh_port
            new_server.cpu = cpu
            new_server.ram = ram
            new_server.disk = disk
            new_server.network_bandwidth = network_bandwidth
            new_server.ssh_user = ssh_user
            new_server.system = system

            new_server.save()

            return render(request, 'assets/addserver.html', locals())
    addserver_form = forms.AddserverForm()
    return render(request, 'assets/addserver.html', locals())