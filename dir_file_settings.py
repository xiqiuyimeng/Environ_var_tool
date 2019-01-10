# -*- coding: utf-8 -*-
import re
_author_ = 'luwt'
_date_ = '2018/11/7 0:10'

# [^a-z]+?是为了避免匹配到jre
PATTERN_JAVA = r'.*jdk([^a-z]+?)(bin\\java.exe)'
PATTERN_PYTHON = r'.*\\python.exe|.*\\pip(\d*).exe'
PATTERN_MAVEN = r'.*apache-maven(.*bin\\mvn.cmd)'
PATTERN_IGNORE = r'.*Local\\Application Data'


def match_path(tmp_path, pattern_):
    """对tmp_path进行正则匹配(忽略大小写)"""
    pattern = re.compile(pattern_, re.I)
    return pattern.search(tmp_path)


def match_ignore_path(tmp_path):
    """快捷方式引用，遍历无意义"""
    pattern = re.compile(PATTERN_IGNORE, re.I)
    return pattern.search(tmp_path)


# 忽略列表，或太大没意义，或无权访问
ignore_path = ['Windows', 'System Volume Information', 'Recovery',
               'Documents and Settings', 'Config.Msi', 'Windows.old']




