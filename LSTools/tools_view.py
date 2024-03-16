# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QDesktopWidget


class Ui_mainWindow(object):
    def __init__(self, bts_info: list):
        # 获取系统分辨率
        screen_width, screen_height = self.sys_resolution if self.sys_resolution != "" else (1920, 1080)
        # 获取比例

        self.with_scale = int(screen_width / 1920)
        self.height_scale = int(screen_height / 1080)
        self.bts_info = bts_info

    @property
    def sys_resolution(self):
        import subprocess
        resolution = ""
        output = subprocess.check_output(
            ["powershell", "(Get-WmiObject -Class Win32_VideoController).VideoModeDescription"])
        lines = output.decode("latin-1").split("\n")
        if lines:
            first_line = lines[0].strip()
            if first_line:
                resolution = first_line.split(" x ")[0:2]
                return int(resolution[0]), int(resolution[1])
        return resolution


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 500)
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 700, 40))
        self.bts = []
        generate_xy = self.generate_control_xy()
        for i, _ in enumerate(self.bts_info):
            x, y = next(generate_xy)
            self.bts.append(QtWidgets.QPushButton(self.centralwidget))
            self.bts[i].setGeometry(QtCore.QRect(x, y, 120, 40))
        mainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(mainWindow)
    def generate_control_xy(self):
        start_x = 50
        start_y = 100
        while True:
            yield int(start_x * self.with_scale), int(start_y * self.height_scale)
            if start_x + 190 >= 800:
                start_y += 70
                start_x = 50
            else:
                start_x += 190


    def show_result(self, func):
        result = func()
        self.toast = str(result)

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800 * self.with_scale, 500 * self.height_scale)
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 700, 40))
        self.bts = []
        generate_xy = self.generate_control_xy()
        for i, _ in enumerate(self.bts_info):
            x, y = next(generate_xy)
            self.bts.append(QtWidgets.QPushButton(self.centralwidget))
            self.bts[i].setGeometry(QtCore.QRect(x, y, 120 * self.with_scale, 40 * self.height_scale))
        mainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(mainWindow)


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Tools"))
        self.label.setText(_translate("mainWindow", "TextLabel"))
        for i, bt in enumerate(self.bts):
            bt.setText(_translate("mainWindow", self.bts_info[i]["text"]))


if __name__ == '__main__':
    pass

