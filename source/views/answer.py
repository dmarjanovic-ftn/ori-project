#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui
from source.enums import *
from source.model.figures import *


class AnswerResult(QtGui.QWidget):

    def __init__(self, figures=[]):
        super(AnswerResult, self).__init__()

        self._figures = figures

        self.init()

    def init(self):
        self.setFixedSize(132, 132)
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(0, 0, 125, 125)

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

        qp.end()
