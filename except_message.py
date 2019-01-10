# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
_author_ = 'luwt'
_date_ = '2018/12/9 0:19'


class ExceptMessage:
    """自定义异常消息提示"""

    def __init__(self, msg):

        self.box = QMessageBox(QMessageBox.Critical, '警告', msg)

        # 添加按钮，可用中文
        self.yes = self.box.addButton('退出', QMessageBox.YesRole)

        # 设置消息框中内容前面的图标
        self.box.setIcon(3)

        # 显示
        self.box.show()


def except_dialog(msg):
    app = QtWidgets.QApplication(sys.argv)
    execpt_message = ExceptMessage(msg)
    sys.exit(app.exec_())

