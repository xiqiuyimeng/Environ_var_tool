# -*- coding: utf-8 -*-
import psutil
import itertools
from decorator_demo import decorator_demo as dd
_author_ = 'luwt'
_date_ = '2018/11/6 23:35'


def get_cpu_count():
    """获取cpu逻辑核心数"""
    return psutil.cpu_count()


@dd.times
def get_disk_partitions():
    """获取磁盘盘符信息"""
    partitions = psutil.disk_partitions()
    disks = []
    disks += [pt.device for pt in partitions]
    print(disks)
    return disks


