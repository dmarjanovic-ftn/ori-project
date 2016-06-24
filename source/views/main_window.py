#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from canvas import Canvas


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(u"ORI 2016 - Baćo & dmarjanovic")
        # self.showFullScreen()
        self.showMaximized()

        dock = QtGui.QDockWidget()
        dock.setWidget(Canvas())

        # self.addDockWidget(dock)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
