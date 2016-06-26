#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui
from canvas import Canvas
from source.consts import Sizes
from source.actions.actions import Actions


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(u"ORI 2016 - Baćo & dmarjanovic")
        self.showMaximized()
        self.setStyleSheet("background-color: #FFF;")

        panel = QtGui.QWidget()
        panel.setFixedSize(Sizes.BOX_WIDTH + 180, Sizes.BOX_HEIGHT)

        buttons = QtGui.QVBoxLayout()
        accept = QtGui.QPushButton("Prihvati")
        reject = QtGui.QPushButton("Odbij")

        accept.setStyleSheet("background-color: #eee;")
        reject.setStyleSheet("background-color: #eee;")

        canvas = Canvas()

        accept.clicked.connect(lambda: Actions.accept_example(canvas))
        reject.clicked.connect(lambda: Actions.reject_example(canvas))

        buttons.addWidget(accept)
        buttons.addWidget(reject)
        buttons.addStretch(0)

        layout = QtGui.QGridLayout()
        layout.addWidget(canvas, 0, 0)
        layout.addLayout(buttons, 0, 1)

        panel.setLayout(layout)

        self.setCentralWidget(panel)
