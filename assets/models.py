from django.db import models

# Create your models here.


class Server(models.Model):

    os_type = models.CharField('操作系统类型', max_length=64, blank=True, null=True)
    os_release = models.CharField('操作系统版本', max_length=64, blank=True, null=True)

    alias = models.CharField('主机别名', max_length=64)
    extranet_IP = models.GenericIPAddressField('外网IP', blank=True, null=True)
    intranet_IP = models.GenericIPAddressField('内网IP', blank=True, null=True)
    ssh_port = models.CharField('SSH端口', max_length=16, default=22)

    cpu = models.IntegerField('CPU数量', blank=True, null=True)
    ram = models.IntegerField('内存大小(GB)', blank=True, null=True)
    disk = models.FloatField('磁盘大小(GB)', blank=True, null=True)
    network_bandwidth = models.CharField('网络带宽(Mbps)', max_length=64, blank=True, null=True)

    ssh_user = models.TextField('远程登录用户', max_length=256, blank=True, null=True)
    modified_time = models.DateTimeField('最后修改时间', auto_now_add=True)

    system = models.CharField('所属环境', max_length=64, default='others')

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = '服务器'