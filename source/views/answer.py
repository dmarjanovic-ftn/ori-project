#!/usr/bin/python
# -*- coding: utf-8 -*-
import PySide
from PySide import QtGui, QtCore
from PySide.QtGui import QApplication

from source.enums import *
from source.model.figures import *
from source.enums import AnswerState


class AnswerResult(QtGui.QWidget):

    def __init__(self, parent, name, figures=[]):
        super(AnswerResult, self).__init__()

        self._parent = parent
        self._name = name
        self._figures = figures
        self.state = AnswerState.NOT_CHECKED

        self.init()

    def init(self):
        self.setFixedSize(132, 132)
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)

        if self.state == AnswerState.CHECKED:
            qp.setBrush(QtGui.QColor(255, 193, 7))
        elif self.state == AnswerState.INVALID:
            qp.setBrush(QtGui.QColor(158, 158, 158, 0.4))
        elif self.state == AnswerState.WRONG:
            qp.setBrush(QtGui.QColor(183, 28, 28))
        elif self.state == AnswerState.CORRECT:
            qp.setBrush(QtGui.QColor(76, 175, 80))
        else:
            qp.setBrush(QtGui.QColor(255, 255, 255))

        rect = PySide.QtCore.QRectF(0, 0, 125, 125)
        qp.drawRect(rect)

        for figure in self._figures:
            if figure._type == FigureType.SQUARE:
                figure.__class__ = Square
            elif figure._type == FigureType.CIRCLE:
                figure.__class__ = Circle
            elif figure._type == FigureType.TRIANGLE:
                figure.__class__ = Triangle
            elif figure._type == FigureType.PIE:
                figure.__class__ = Pie
            elif figure._type == FigureType.LINE:
                figure.__class__ = Line
            elif figure._type == FigureType.ARROW:
                figure.__class__ = Arrow

            figure.draw(qp, Quadrant.TOP_LEFT, scale=2.1)

        if self.state == AnswerState.INVALID:
            pen = QtGui.QPen(QtGui.QColor(183, 28, 28))
            pen.setWidth(2)
            qp.setPen(pen)
            qp.drawLine(2, 2, 123, 123)
            qp.drawLine(2, 123, 123, 2)
            qp.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0)))

        # draw answer name
        qp.setBrush(QtGui.QColor(0, 0, 0))
        rect = QtCore.QRectF(108, 108, 125, 125)
        qp.drawRect(rect)

        qp.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255)))
        font = qp.font()
        if self._name.endswith("%"):
            font.setPointSize(8)
            qp.setFont(font)
            qp.drawText(QtCore.QPoint(109, 123), self._name[:-1])
        else:
            font.setPointSize(18)
            qp.setFont(font)
            qp.drawText(QtCore.QPoint(113, 129), self._name)

        qp.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0)))

        qp.end()

    def mousePressEvent(self, event):
        main_window = self._parent

        if self.state == AnswerState.NOT_CHECKED:
            self.state = AnswerState.CHECKED
            self.repaint()

            if main_window.checked is not None:
                main_window.checked.state = AnswerState.NOT_CHECKED
                main_window.checked.repaint()

            main_window.checked = self

    def enterEvent(self, event):
        if self.state == AnswerState.NOT_CHECKED:
            QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def leaveEvent(self, event):
        QApplication.restoreOverrideCursor()
