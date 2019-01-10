# -*- coding: utf-8 -*-
from envir_vars import environ_var as ev
_author_ = 'luwt'
_date_ = '2018/12/17 10:49'


def set_var(app_list=None, file_list=None):
    environ_vars = ev.EnvironVars()
    environ_vars.save_path_var()
    if app_list:
        for app in app_list:
            if not environ_vars.check_var_exist(app=app):
                environ_vars.set_app_env(app)
    if file_list:
        for file in file_list:
            if not environ_vars.check_var_exist(file=file):
                environ_vars.set_file_env(file)

# 先检测app和file变量是否存在，拿到检测结果，app_dict,file_dict，
# 可以把那些已经存在和不存在的分别放入两个集合中，如果不存在的为空，
# 就不用执行了，如过app不为空，取字典进行后续的搜寻，找到后进行配置，
# 已经存在的返回前台，日志打印已存在不需要配置。
