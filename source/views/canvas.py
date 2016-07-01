#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from source.model.figures import *
from source.enums import *
from source.consts import *
from source.actions.actions import Actions


class Canvas(QtGui.QWidget):

    def __init__(self):
        super(Canvas, self).__init__()

        self.init()

    def init(self):
        self.setFixedSize(Sizes.BOX_WIDTH, Sizes.BOX_HEIGHT)
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(0, 0, Sizes.QUADRANT_WIDTH, Sizes.QUADRANT_HEIGHT)
        qp.drawRect(Sizes.QUADRANT_WIDTH, 0, Sizes.QUADRANT_WIDTH - 1, Sizes.QUADRANT_HEIGHT)
        qp.drawRect(0, Sizes.QUADRANT_HEIGHT, Sizes.QUADRANT_WIDTH, Sizes.QUADRANT_HEIGHT - 5)
        qp.setBrush(QtGui.QColor(165, 214, 167))
        qp.drawRect(Sizes.QUADRANT_WIDTH, Sizes.QUADRANT_HEIGHT, Sizes.QUADRANT_WIDTH - 1, Sizes.QUADRANT_HEIGHT - 5)

        mask = QtGui.QImage("..\images\question-mark.png")
        mask = mask.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        qp.drawImage(Sizes.QUADRANT_WIDTH + 85, Sizes.QUADRANT_HEIGHT + 70, mask)

        qp.setBrush(QtGui.QColor(255, 255, 255))
        pen = QtGui.QPen()
        pen.setWidthF(1.5)
        qp.setPen(pen)
        self.draw_figures(qp, Actions.figures)
        qp.end()

    @staticmethod
    def draw_figures(qp, figures):
        i = 0

        for figure in figures:
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

            if i < 2:
                figure.draw(qp, Quadrant.TOP_LEFT)
            elif i < 4:
                figure.draw(qp, Quadrant.TOP_RIGHT)
            elif i < 6:
                figure.draw(qp, Quadrant.BOTTOM_LEFT)

            i += 1
