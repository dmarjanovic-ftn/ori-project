#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(u"ORI 2016 - Baćo & dmarjanovic")
        # self.showFullScreen()
        self.showMaximized()
