# -*- coding: UTF-8 -*-
from datetime import datetime
import subprocess
import win32con
import win32api
import os


class EnvironVars:
    """配置环境变量并备份"""
    def __init__(self):
        # 获取句柄
        self.key = win32api.RegOpenKey(
            win32con.HKEY_LOCAL_MACHINE,
            r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
            0,
            win32con.KEY_ALL_ACCESS
        )
        # path变量值
        self.path_val = win32api.RegQueryValueEx(self.key, "Path")[0]
        self.check_dict = {'Java': r'java -version',
                           'Python': r'python -V',
                           'Maven': r'mvn -v'
                           }

    def save_path_var(self):
        """备份path变量值"""
        now = datetime.now()
        # 当前路径，备份文件将存于此
        curr_path = os.path.abspath(".")
        with open("{}/原变量值.txt".format(curr_path), "a") as f:
            f.write('☆☆☆☆☆\n原变量值为：\n' + self.path_val +
                    '\n如系统异常请将原变量值复制回path变量处\n' +
                    now.strftime('%Y-%m-%d %H:%M:%S\n') + '☆☆☆☆☆\n\n')
        print('\n本次修改之前的变量值保存成功！请在桌面查看！\n\n')

    def set_app_env(self, app_path):
        """配置应用的环境变量，需要添加到Path"""
        # 向Path添加值
        try:
            win32api.RegSetValueEx(self.key,
                                   "Path",
                                   0,
                                   win32con.REG_SZ,
                                   "{}{};".format(self.path_val, app_path)
                                   )
            print('变量配置成功!')
        except Exception as e:
            print(e)

    def set_file_env(self, file_path):
        """配置单文件形式的配置文件，不需要添加到Path"""
        # 获取文件名
        try:
            file_name = os.path.basename(file_path)
            file_name_upper = os.path.splitext(file_name)[0].upper()
            # 格式化路径
            file_path = os.path.abspath(file_path)
            win32api.RegSetValueEx(self.key,
                                   file_name_upper,
                                   0,
                                   win32con.REG_SZ,
                                   file_path
                                   )
            print('\n配置文件环境变量配置成功！\n\n')
        except Exception as e:
            print(e)

    def check_var_exist(self, app_list=None, file_list=None):
        """
        检测环境变量是否已存在，
        如果path为文件夹，配置内容为程序，需判断path中是否存在该变量；
        如果path为文件，配置内容为文件，需判断文件名大写的变量是否存在，
        若存在则设置对应字典的值为true，不存在为false
        """
        app_dict = {}
        file_dict = {}
        if file_list:
            for file in file_list:
                file_name = os.path.basename(file)
                file_name_upper = os.path.splitext(file_name)[0].upper()
                file_var = win32api.RegQueryValueEx(self.key, file_name_upper)[0]
                file_dict[file] = True if file_var and file_var == file else False
        if app_list:
            for app in app_list:
                if self.check_dict[app]:
                    code = None
                    try:
                        code = subprocess.call(self.check_dict[app], shell=True)
                    except:
                        pass
                    finally:
                        # 暂时发现执行这几个查询版本号成功的code为0
                        app_dict[app] = True if code == 0 else False
        return app_dict, file_dict

