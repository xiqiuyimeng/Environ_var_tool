# -*- coding: utf-8 -*-
from envir_vars import environ_var as ev
from envir_vars import recur_process as rp
_author_ = 'luwt'
_date_ = '2018/12/17 10:49'


def set_var(app_list=None, file_list=None):
    environ_vars = ev.EnvironVars()
    exist_list = []
    if app_list:
        app_dict = {}
        for app in app_list:
            if environ_vars.check_var_exist(app=app):
                exist_list.append(app)
            else:
                app_dict[app] = []
        if app_dict:
            environ_vars.save_path_var()
            # 开始搜索程序目录
            res_dict = rp.main(app_dict)
            for res in res_dict.values():
                for app in res:
                    environ_vars.set_app_env(app)
    if file_list:
        for file in file_list:
            if environ_vars.check_var_exist(file=file):
                exist_list.append(file)
            else:
                environ_vars.set_file_env(file)
    return exist_list

