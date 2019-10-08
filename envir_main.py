# -*- coding: utf-8 -*-
from envir_vars import decorators as ds
from envir_vars import envir
from PyQt5 import QtWidgets
import PyQt5.sip
import sys

_author_ = 'luwt'
_date_ = '2018/12/17 10:26'


@ds.require_admin()
def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = envir.Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
