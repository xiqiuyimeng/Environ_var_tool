# -*- coding: utf-8 -*-
from functools import wraps
import except_message
import datetime
import win32con
import win32api
_author_ = 'luwt'
_date_ = '2018/11/7 9:47'


def times_used(*dargs):
    """计算程序运行时间"""
    def times(f):
        @wraps(f)
        def count_time(*args, **kw):
            start = datetime.datetime.now()
            print("【{}】开始时间为：{}".format(dargs[0],
                                        start.strftime('%Y-%m-%d %H:%M:%S')))
            # 获取原函数返回值并返回，否则将丢失原函数返回值
            f_res = f(*args, **kw)
            end = datetime.datetime.now()
            interval = (end - start).seconds
            time_sec = datetime.timedelta(seconds=interval)
            print("【{}】结束时间：{}，耗时{}".format(dargs[0],
                                            end.strftime('%Y-%m-%d %H:%M:%S'),
                                            time_sec))
            return f_res
        return count_time
    return times


def require_admin():
    """验证当前是否有管理员权限，若没有则给出提示"""
    def admin_(f):
        @wraps(f)
        def admin(*args, **kw):
            try:
                # 尝试获取句柄，若失败则需要以管理员权限运行
                win32api.RegOpenKey(
                    win32con.HKEY_LOCAL_MACHINE,
                    r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
                    0,
                    win32con.KEY_ALL_ACCESS
                )
            except Exception as e:
                if e.args[0] == 5:
                    msg = "权限不足，无法操作，请以管理员身份运行本程序"
                else:
                    msg = "其他未知错误：{}".format(e)
                except_message.except_dialog(msg)
            f_res = f(*args, **kw)
            return f_res
        return admin
    return admin_
