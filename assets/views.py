from django.shortcuts import render
from django.shortcuts import get_object_or_404
from assets import models

# Create your views here.


def index(request):

    servers = models.Server.objects.all()
    return render(request, 'assets/index.html', locals())


def dashboard(request):
    pass
    return render(request, 'assets/dashboard.html', locals())


def detail(requset, server_id):
    """
    以显示服务器类型资产详细为例，安全设备、存储设备、网络设备等参照此例。
    :param request:
    :param asset_id:
    :return:
    """
    server = get_object_or_404(models.Server, id=server_id)
    return render(requset, 'assets/detail.html', locals())