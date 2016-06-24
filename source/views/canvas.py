#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from source.model.figures import *
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
        """
        square = Square(FigureType.SQUARE, FigurePosition.TOP, FigureSize.SMALL)
        square.draw(qp, Quadrant.BOTTOM_LEFT)

        circle = Circle(FigureType.CIRCLE, FigurePosition.RIGHT, FigureSize.MEDIUM)
        circle.draw(qp, Quadrant.BOTTOM_LEFT)

        circle_2 = Circle(FigureType.CIRCLE, FigurePosition.BOTTOM, FigureSize.BIG)
        circle_2.draw(qp, Quadrant.BOTTOM_LEFT)

        square_2 = Square(FigureType.SQUARE, FigurePosition.CENTER, FigureSize.BIG)
        square_2.draw(qp, Quadrant.TOP_LEFT)


        triangle = Triangle(FigureType.TRIANGLE, FigurePosition.CENTER, FigureSize.BIG, FigureOrientation.EAST)
        triangle.draw(qp, Quadrant.TOP_LEFT)
        triangle2 = Triangle(FigureType.TRIANGLE, FigurePosition.CENTER, FigureSize.MEDIUM, FigureOrientation.NORTH)
        triangle2.draw(qp, Quadrant.TOP_LEFT)
        triangle3 = Triangle(FigureType.TRIANGLE, FigurePosition.CENTER, FigureSize.SMALL, FigureOrientation.WEST)
        triangle3.draw(qp, Quadrant.TOP_LEFT)
        """
        # triangle4 = Triangle(FigureType.TRIANGLE, FigurePosition.CENTER, FigureSize.MEDIUM, FigureOrientation.SOUTH)
        # triangle4.draw(qp, Quadrant.TOP_LEFT)

        pie = Pie(FigureType.TRIANGLE, FigurePosition.CENTER, FigureSize.BIG, FigureOrientation.WEST)
        pie.draw(qp, Quadrant.TOP_LEFT)

        line1 = Arrow(FigureType.LINE, FigurePosition.TOP, FigureSize.BIG, FigureOrientation.WEST)
        line1.draw(qp, Quadrant.TOP_LEFT)

        line2 = Arrow(FigureType.LINE, FigurePosition.RIGHT, FigureSize.SMALL, FigureOrientation.NORTH)
        line2.draw(qp, Quadrant.TOP_LEFT)
