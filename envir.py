# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from envir_vars import test_slot
import os


class Ui_Form(QtWidgets.QWidget):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setObjectName("title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.title)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text = QtWidgets.QLabel(self.title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.text.setFont(font)
        self.text.setTextFormat(QtCore.Qt.AutoText)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setIndent(0)
        self.text.setObjectName("text")
        self.verticalLayout_2.addWidget(self.text)
        self.verticalLayout.addWidget(self.title)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_java = QtWidgets.QCheckBox(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.checkBox_java.setFont(font)
        self.checkBox_java.setObjectName("checkBox_java")
        self.verticalLayout_4.addWidget(self.checkBox_java)
        self.checkBox_python = QtWidgets.QCheckBox(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.checkBox_python.setFont(font)
        self.checkBox_python.setObjectName("checkBox_python")
        self.verticalLayout_4.addWidget(self.checkBox_python)
        self.checkBox_maven = QtWidgets.QCheckBox(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.checkBox_maven.setFont(font)
        self.checkBox_maven.setObjectName("checkBox_maven")
        self.verticalLayout_4.addWidget(self.checkBox_maven)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 8)
        self.horizontalLayout.addWidget(self.widget_4)
        self.line = QtWidgets.QFrame(self.widget_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setContentsMargins(80, -1, 80, -1)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.choose_file = QtWidgets.QPushButton(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.choose_file.setFont(font)
        self.choose_file.setObjectName("choose_file")
        self.verticalLayout_6.addWidget(self.choose_file)
        self.verticalLayout_5.addWidget(self.widget_7)
        self.widget = QtWidgets.QWidget(self.widget_5)
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.file_selected_area = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.file_selected_area.setFont(font)
        self.file_selected_area.setVisible(False)
        self.file_selected_area.setObjectName("file_selected_area")
        self.verticalLayout_8.addWidget(self.file_selected_area)
        self.verticalLayout_5.addWidget(self.widget)
        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 3)
        self.verticalLayout_5.setStretch(2, 5)
        self.horizontalLayout.addWidget(self.widget_5)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.output_area = QtWidgets.QTextBrowser(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.output_area.setFont(font)
        self.output_area.setObjectName("output_area")
        self.verticalLayout_7.addWidget(self.output_area)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget_3)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_7.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 存放选择结果的列表
        self.exe_list = []
        self.file_list = []

        # 点击checkBox的时候触发事件
        self.checkBox_java.stateChanged.connect(self.check_event)
        self.checkBox_python.stateChanged.connect(self.check_event)
        self.checkBox_maven.stateChanged.connect(self.check_event)

        # 选择文件路径按钮点击事件
        self.choose_file.clicked.connect(self.open_file)
        # 选择文件区域交互事件
        self.file_selected_area.textChanged.connect(self.text_change)

        # 按钮响应事件
        self.buttonBox.accepted.connect(self.check_file_param)
        self.buttonBox.rejected.connect(self.check_button)

        self.thread_ = test_slot.BackQThread()
        self.thread_.update_date.connect(self.print_log)

    def print_log(self, msg):
        self.output_area.append(msg)

    def update_text(self, msg):
        self.output_area.append(msg)

    def open_file(self):
        """选择文件路径"""
        file_name = QFileDialog.getOpenFileName(self, "请选择文件", '/')
        if file_name[0]:
            self.file_list.append(file_name[0])
            self.file_selected_area.setVisible(True)
            self.file_text_show()
            self.text_show()

    def check_event(self, checked):
        """获取选中的checkBox值，放入结果列表，并在textBrowser显示"""
        check_box = self.sender()
        if checked == QtCore.Qt.Checked:
            self.exe_list.append(check_box.text())
            self.text_show()

        if checked == QtCore.Qt.Unchecked:
            self.exe_list.remove(check_box.text())
            self.text_show()

    def file_text_show(self):
        """文件区域选择结果显示"""
        if self.file_list:
            self.file_text = "\n".join(self.file_list)
            self.file_selected_area.setText(self.file_text)

    def text_change(self):
        """当文件区域内容被修改时，同步列表和日志区"""
        text = self.file_selected_area.toPlainText()
        # 去除列表中空字符串
        self.file_list = list(filter(None, text.split("\n")))
        self.text_show()
        if 0 == len(self.file_list):
            self.file_selected_area.setVisible(False)

    def text_show(self):
        """根据结果列表显示内容，将结果列表转为字符串，如果列表为空则清空显示内容"""
        final_list = self.exe_list + self.file_list
        if final_list:
            self.check_text = "、".join(final_list)
            self.output_area.setText("已选择：{}\n点击OK进行配置，点击Cancel清除所有内容".
                                     format(self.check_text))
        else:
            self.output_area.clear()

    def check_button(self):
        """
        清除所有已选择的，列表清空需要置在最后，
        因为重置checkBox会触发check_event事件，空列表无法移除元素，会导致异常
        """
        self.output_area.clear()
        self.file_selected_area.clear()
        self.checkBox_maven.setCheckState(0)
        self.checkBox_java.setCheckState(0)
        self.checkBox_python.setCheckState(0)
        self.file_list.clear()
        self.exe_list.clear()

    def check_file_param(self):
        """检验文件列表里元素是否为文件"""
        nf_list = list(filter(lambda f: not os.path.isfile(f), self.file_list))
        if nf_list:
            msg = "系统检测：【{}】不是文件，请重新核对！".format("、".join(nf_list))
            QMessageBox.question(self, "提醒", msg, QMessageBox.Yes)
        elif 0 == len(self.exe_list) and 0 == len(self.file_list):
            msg = "请选择"
            QMessageBox.question(self, "提醒", msg, QMessageBox.Yes)
        else:
            msg = "准备就绪，确定开始配置？"
            question = QMessageBox.question(self, "提醒", msg, QMessageBox.Yes)
            if question == QMessageBox.Yes:
                self.thread_.start()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "环境变量配置工具 -- by lwt"))
        self.text.setText(_translate("Form", "欢迎使用环境变量配置工具"))
        self.label_2.setText(_translate("Form", "请选择要配置的程序："))
        self.checkBox_java.setText(_translate("Form", "Java"))
        self.checkBox_python.setText(_translate("Form", "Python"))
        self.checkBox_maven.setText(_translate("Form", "Maven"))
        self.label_3.setText(_translate("Form", "请选择要配置的文件："))
        self.choose_file.setText(_translate("Form", "请选择文件"))
        self.output_area.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
