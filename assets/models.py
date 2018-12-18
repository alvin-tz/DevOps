from django.db import models

# Create your models here.


class Server(models.Model):

    os_type = models.CharField(verbose_name='操作系统类型', max_length=64, blank=True, null=True)
    os_release = models.CharField(verbose_name='操作系统版本', max_length=64, blank=True, null=True)

    hostname = models.CharField(verbose_name='主机名', max_length=64, blank=True, null=True)
    alias = models.CharField(verbose_name='主机别名', max_length=64)
    extranet_IP = models.GenericIPAddressField(verbose_name='外网IP', blank=True, null=True)
    intranet_IP = models.GenericIPAddressField(verbose_name='内网IP', blank=True, null=True)
    ssh_port = models.CharField(verbose_name='SSH端口', max_length=16, default=22)

    cpu = models.IntegerField(verbose_name='CPU数量', blank=True, null=True)
    ram = models.IntegerField(verbose_name='内存大小(GB)', blank=True, null=True)
    disk = models.FloatField(verbose_name='磁盘大小(GB)', blank=True, null=True)
    network_bandwidth = models.CharField(verbose_name='网络带宽(Mbps)', max_length=64, blank=True, null=True)

    ssh_user = models.TextField(verbose_name='远程登录用户', max_length=256, blank=True, null=True)
    modified_time = models.DateTimeField(verbose_name='最后修改时间', auto_now_add=True)

    env_choice = (
        ('mainnet', '主网环境'),
        ('testnet', '测试网环境'),
        ('develop', '开发环境'),
        ('others', '其他环境'),
    )
    system = models.CharField(verbose_name='所属环境', choices=env_choice, max_length=64, default='others')

    def __str__(self):
        return '%s  [ %s ]' % (self.alias, self.hostname)

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = '服务器'