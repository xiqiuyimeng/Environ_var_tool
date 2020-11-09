# -*- coding: utf-8 -*-
_author_ = 'luwt'
_date_ = '2018/11/6 23:41'


def div_list(path_list, n):
    """将path_list进行n等分，余下放入最后一个子列表"""
    print("***************开始分割列表****************")
    print("根目录下总项目数为{}".format(len(path_list)))
    list_new = []
    if n > 0:
        paths_size = len(path_list) // n
        if paths_size > 0:
            for i in range(1, n + 1):
                if i == 1:
                    list_new.append(path_list[:paths_size])
                elif i == n:
                    list_new.append(path_list[paths_size * (i - 1):])
                else:
                    list_new.append(path_list[paths_size * (i - 1):
                                              paths_size * i])
        elif paths_size == 0:
            list_new = path_list
        print("分割列表完毕！")
    else:
        print("n <= 0，参数错误，无法分割列表")
    [print(p) for p in list_new]
    return list_new
