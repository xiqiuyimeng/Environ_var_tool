# -*- coding: utf-8 -*-
import os
from multiprocessing import Pool

from envir_vars import decorators as dc
from envir_vars import dir_file_settings as df
from envir_vars import list_tools as lt
from envir_vars import pc_tools as pt

_author_ = 'luwt'
_date_ = '2018/11/6 23:50'


class FindPath:

    def __init__(self, target_path):
        self.target_path = target_path

    def get_target_path(self, file_path):
        """递归遍历，找到目标文件的路径"""
        try:
            fs = os.listdir(file_path)
            for f in fs:
                tmp_path = os.path.join(file_path, f)
                try:
                    if os.path.isdir(tmp_path):
                        if f in df.ignore_path or df.match_ignore_path(tmp_path):
                            continue
                        else:
                            self.get_target_path(tmp_path)
                    elif os.path.isfile(tmp_path):
                        for key in self.target_path.keys():
                            pattern = eval('df.PATTERN_{}'.format(key.upper()))
                            if df.match_path(tmp_path, pattern):
                                self.target_path[key].append(os.path.dirname(tmp_path))
                except OSError:
                    pass
        except OSError:
            pass

    @dc.times_used('文件遍历进程{}'.format(os.getpid()))
    def file_process(self, file_paths):
        """如果是文件就进行匹配，是文件夹准备遍历"""
        path_dict = {}
        for file_path in file_paths:
            if os.path.isdir(file_path):
                self.get_target_path(file_path)
                if self.target_path:
                    path_dict = self.target_path
            elif os.path.isfile(file_path):
                for key in self.target_path.keys():
                    pattern = eval('df.PATTERN_{}'.format(key.upper()))
                    if df.match_path(file_path, pattern):
                        path_dict[key].append(os.path.dirname(file_path))
        print('进程:{}的遍历结果是{}'.format(os.getpid(), path_dict))
        return path_dict

    def start_process(self, path_list):
        """开进程，分任务"""
        proc_results = []
        try:
            merge_paths = []
            for path in path_list:
                paths = os.listdir(path)
                # 去除根目录下不访问的目录，即在忽略列表里的
                [paths.remove(ig_path) for ig_path in df.ignore_path
                 if ig_path in paths]
                # 生成全路径
                merge_paths += [os.path.join(path, p) for p in paths]
            list_new = lt.div_list(merge_paths, pt.get_cpu_count())
            if list_new:
                p = Pool(len(list_new))
                [proc_results.append(p.apply_async(
                    self.file_process, args=(new_path,)))
                    for new_path in list_new]
                p.close()
                p.join()
        except OSError:
            pass
        return proc_results


@dc.times_used("main函数")
def main():
    path_root_list = pt.get_disk_partitions()
    print("path_root==>{}".format(path_root_list))
    path_dict = {'Java': [], 'Python': []}
    find_path = FindPath(path_dict)
    results = find_path.start_process(path_root_list)
    for k in path_dict.keys():
        for result in results:
            if result.get()[k]:
                path_dict[k].extend(result.get()[k])
        # 去重
        path_dict[k] = list(set(path_dict[k]))
    print("最终结果是：{}".format(path_dict))


if __name__ == '__main__':
    main()
