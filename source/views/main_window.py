#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui
from canvas import Canvas
from answer import AnswerResult
from source.consts import Sizes
from source.actions.actions import Actions


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(u"ORI 2016 - Baćo & dmarjanovic")
        # self.showMaximized()
        self.setStyleSheet("background-color: #CFD8DC;")

        panel = QtGui.QWidget()
        panel.setFixedSize(Sizes.BOX_WIDTH + 180, Sizes.BOX_HEIGHT + 150)

        buttons = QtGui.QVBoxLayout()
        accept = QtGui.QPushButton("Prihvati")
        reject = QtGui.QPushButton("Odbij")

        accept.setStyleSheet("background-color: #eee;")
        reject.setStyleSheet("background-color: #eee;")

        canvas = Canvas()

        results = QtGui.QHBoxLayout()

        answer_a = AnswerResult()
        answer_b = AnswerResult()
        answer_c = AnswerResult()
        answer_d = AnswerResult()

        results.addWidget(answer_a)
        results.addWidget(answer_b)
        results.addWidget(answer_c)
        results.addWidget(answer_d)

        accept.clicked.connect(lambda: Actions.accept_example(canvas))
        reject.clicked.connect(lambda: Actions.reject_example(canvas, answer_a, answer_b, answer_c, answer_d))

        buttons.addWidget(accept)
        buttons.addWidget(reject)
        buttons.addStretch(0)

        layout = QtGui.QGridLayout()
        layout.addWidget(canvas, 1, 0)
        layout.addLayout(buttons, 1, 1)
        layout.addLayout(results, 2, 0)

        panel.setLayout(layout)

        self.setCentralWidget(panel)
