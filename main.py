# -*- coding: utf-8 -*-
from src.env_decorators.decorators import require_admin
from PyQt5 import QtWidgets
import PyQt5.sip
import sys

from src.main_window.main_window import EnvUI

_author_ = 'luwt'
_date_ = '2018/12/17 10:26'


@require_admin()
def main():
    app = QtWidgets.QApplication(sys.argv)
    screen_rect = QtWidgets.QApplication.desktop().screenGeometry()
    ui = EnvUI(screen_rect)
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
