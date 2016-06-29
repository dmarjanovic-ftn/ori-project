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
        accept = QtGui.QPushButton("Potvrdi")
        reject = QtGui.QPushButton(u"Sljedeći")
        fifty = QtGui.QPushButton("50:50")
        prob = QtGui.QPushButton(u"Pomoć prijatelja")

        accept.setStyleSheet("background-color: #eee;")
        reject.setStyleSheet("background-color: #eee;")
        fifty.setStyleSheet("background-color: #eee;")
        prob.setStyleSheet("background-color: #eee;")

        canvas = Canvas()

        results = QtGui.QHBoxLayout()

        answer_a = AnswerResult(self, "A")
        answer_b = AnswerResult(self, "B")
        answer_c = AnswerResult(self, "C")
        answer_d = AnswerResult(self, "D")

        self.answers = []
        self.answers.append(answer_a)
        self.answers.append(answer_b)
        self.answers.append(answer_c)
        self.answers.append(answer_d)

        self.checked = None

        results.addWidget(answer_a)
        results.addWidget(answer_b)
        results.addWidget(answer_c)
        results.addWidget(answer_d)

        accept.clicked.connect(lambda: Actions.accept_example(answer_a, answer_b, answer_c, answer_d))
        reject.clicked.connect(lambda: Actions.reject_example(canvas, answer_a, answer_b, answer_c, answer_d))
        fifty.clicked.connect(lambda: Actions.fifty_help(answer_a, answer_b, answer_c, answer_d))
        prob.clicked.connect(lambda: Actions.probability_help(answer_a, answer_b, answer_c, answer_d))

        buttons.addWidget(accept)
        buttons.addWidget(reject)
        buttons.addWidget(fifty)
        buttons.addWidget(prob)
        buttons.addStretch(0)

        layout = QtGui.QGridLayout()
        layout.addWidget(canvas, 1, 0)
        layout.addLayout(buttons, 1, 1)
        layout.addLayout(results, 2, 0)

        panel.setLayout(layout)

        self.setCentralWidget(panel)

        # initialize box first time
        Actions.reject_example(canvas, answer_a, answer_b, answer_c, answer_d)
