#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from source.model.figures import Square, Circle
from source.enums import *


class Canvas(QtGui.QWidget):

    def __init__(self):
        super(Canvas, self).__init__()

        self.init()

    def init(self):

        self.setFixedSize(720, 720)
        self.setWindowTitle('Brushes')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_figures(qp)
        qp.end()

    def draw_figures(self, qp):

        square = Square(FigureType.SQUARE, FigurePosition.CENTER, FigureSize.SMALL)
        square.draw(qp, Quadrant.BOTTOM_LEFT)

        circle = Circle(FigureType.CIRCLE, FigurePosition.RIGHT, FigureSize.MEDIUM)
        circle.draw(qp, Quadrant.BOTTOM_LEFT)

        square_2 = Square(FigureType.SQUARE, FigurePosition.CENTER, FigureSize.BIG)
        square_2.draw(qp, Quadrant.TOP_LEFT)