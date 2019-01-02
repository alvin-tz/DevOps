from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from assets import models
from assets import forms
# from django.forms import formset_factory
# from login import models as loginmodels
# from assets import getserverusers

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
    # serverusers = models.ServerUser.objects.filter(server_id=server_id)
    return render(requset, 'assets/detail.html', locals())

def addserver(request):
    if request.method == "POST":
        addserver_form = forms.AddserverForm(request.POST)
        # addserveruser_formset = formset_factory(forms.AddserverUserForm, extra=5,)
        # formset = addserveruser_formset(request.POST, prefix="form")
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
            ssh_user_root_password = addserver_form.cleaned_data['ssh_user_root_password']
            ssh_user_other = addserver_form.cleaned_data['ssh_user_other']
            ssh_user_other_password = addserver_form.cleaned_data['ssh_user_other_password']
            system = addserver_form.cleaned_data['system']

            # user = formset.cleaned_data['user']
            # password = formset.cleaned_data['password']

            same_alias = models.Server.objects.filter(alias=alias)
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
            new_server.ssh_user_root_password = ssh_user_root_password
            new_server.ssh_user_other = ssh_user_other
            new_server.ssh_user_other_password = ssh_user_other_password
            new_server.system = system

            new_server.save()

            return redirect('assets:index')
    addserver_form = forms.AddserverForm()
    return render(request, 'assets/addserver.html', locals())

def modify(request, server_id):
    server = get_object_or_404(models.Server, id=server_id)

    if request.method == "POST":
        server_form = forms.AddserverForm(request.POST)
        message = ""
        if server_form.is_valid():
            server.os_type = request.POST['os_type']
            server.os_release = request.POST['os_release']
            server.hostname = request.POST['hostname']
            server.alias = request.POST['alias']
            server.extranet_IP = request.POST['extranet_IP']
            server.intranet_IP = request.POST['intranet_IP']
            server.ssh_port = request.POST['ssh_port']
            server.cpu = request.POST['cpu']
            server.ram = request.POST['ram']
            server.disk = request.POST['disk']
            server.network_bandwidth = request.POST['network_bandwidth']
            server.ssh_user_root_password = request.POST['ssh_user_root_password']
            server.ssh_user_other = request.POST['ssh_user_other']
            server.ssh_user_other_password = request.POST['ssh_user_other_password']
            server.system = request.POST['system']

            server.save()

            return redirect('assets:detail', server_id=server_id)
        else:
            message = "信息有误，请重新填写！"
            return render(request, 'assets/modify.html', locals())
    else:
        # print(server.os_type)
        server_form = forms.AddserverForm()
        context = {'server': server, 'server_form': server_form}
        return render(request, 'assets/modify.html', context)



def deleteserver(request, server_id):
    server = models.Server.objects.filter(id=server_id)
    server.delete()
    servers = models.Server.objects.all()
    return render(request, 'assets/index.html', locals())




from dwebsocket.decorators import accept_websocket, require_websocket
from django.http import HttpResponse

@accept_websocket
def connect(request):
    if not request.is_websocket():
        try:
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'assets/index.html')
    else:
        for message in request.websocket:
            request.websocket.send(message)


@accept_websocket
def echo(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'assets/index.html')
    else:
        for message in request.websocket:
            request.websocket.send(message)#发送消息到客户端


# def webssh(request):
#     return render(request, 'assets/webssh.html')


# import gevent
# from gevent.socket import wait_read, wait_write
# import paramiko
# import json
#
# class WSSHBridge:
#     """
#     桥接websocket和SSH的核心类
#     """
#     def __init__(self, websocket, user):
#         self.user = user
#         self._websocket = websocket
#         self._tasks = []
#         self.trans = None
#         self.channel = None
#         self.cptext = ''
#         self.cmd_string = ''
#
#     def open(self, host_ip, port, username=None, password=None):
#         """        建立SSH连接        """
#         try:
#             self.trans = paramiko.Transport(host_ip, port)
#             self.trans.start_client()
#             self.trans.auth_password(username=username, password=password)
#             channel = self.trans.open_session()
#             channel.get_pty()
#             self.channel = channel
#         except Exception as e:
#             self._websocket.send(json.dumps({"error": e}))
#             raise
#
#     def _forward_inbound(self, channel):
#         """        正向数据转发，websocket ->  ssh        """
#         try:
#             while True:
#                 data = self._websocket.receive()
#
#                 if not data:
#                     return
#                 data = json.loads(str(data))
#
#                 # data["data"] = data["data"] + "2"
#
#                 if "data" in data:
#                     self.cmd_string += data["data"]
#                     channel.send(data["data"])
#         finally:
#             self.close()
#
#     def _forward_outbound(self, channel):
#         """        反向数据转发，ssh -> websocket        """
#         try:
#             while True:
#                 wait_read(channel.fileno())
#
#                 data = channel.recv(65535)
#                 if not len(data):
#                     return
#
#                 self._websocket.send(json.dumps({"data": data.decode()}))
#         finally:
#             self.close()
#
#     def _bridge(self, channel):
#         """        桥接websocket和ssh        """
#         channel.setblocking(False)
#         channel.settimeout(0.0)
#         self._tasks = [
#             gevent.spawn(self._forward_inbound, channel),
#             gevent.spawn(self._forward_outbound, channel),
#         ]
#         gevent.joinall(self._tasks)
#
#     def close(self):
#         """        结束桥接会话        """
#         gevent.killall(self._tasks, block=True)
#         self._tasks = []
#
#     def shell(self):
#         """        启动一个shell通信界面        """
#         self.channel.invoke_shell()
#         self._bridge(self.channel)
#         self.channel.close()
#
#
# @login_required(login_url='/login/')
# def connect(request, server_id):
#     # 如果当前请求,不是websocket请求则退出
#     if not request.environ.get("wsgi.websocket"):
#         return HttpResponse("错误，非websocket请求")
#
#     server = get_object_or_404(models.Server, id=server_id)
#     try:
#         host_ip = server.alias
#     except Exception as e:
#         message = "无效的账户，或者无权访问" + str(e)
#         return HttpResponse("请求主机异常"+message)
#     port = server.ssh_port
#     username = 'root'
#     # password = request.GET['ssh_user_root_password']
#     print(username, request.META.get("REMOTE_ADDR"))
#     message = "来自{remote}的请求 尝试连接 -> {username}@{hostname} <{ip}:{port}>".format(
#         remote=request.META.get("REMOTE_ADDR"),  # 请求地址
#         username=username,
#         hostname=host_ip,
#         ip=host_ip,
#         port=port,
#     )
#
#     bridge = WSSHBridge(request.environ.get('wsgi.websocket'), request.user)
#
#     try:
#         bridge.open(
#             host_ip=host_ip,
#             port=port,
#             username=username,
#             password=server.ssh_user_root_password
#         )
#     except Exception as e:
#         message = '尝试连接{0}的过程中发生错误：\n {1}'.format(host_ip, e)
#         print(message)
#         return HttpResponse("错误！无法建立SSH连接！")
#     print(request.GET.get("copytext"))
#     bridge.shell()
#
#     request.environ.get('wsgi.websocket').close()
#     print('用户断开连接.....')
#     return HttpResponse("200, ok")
