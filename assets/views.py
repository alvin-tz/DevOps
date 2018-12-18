from django.shortcuts import render
from django.shortcuts import get_object_or_404
from assets import models
from login import models as loginmodels

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
    return render(requset, 'assets/detail.html', locals())