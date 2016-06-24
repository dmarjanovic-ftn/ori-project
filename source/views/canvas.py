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
        fig1 = Figure(FigureType.SQUARE, FigurePosition.TOP, FigureSize.SMALL)
        fig2 = Circle(FigureType.CIRCLE, FigurePosition.RIGHT, FigureSize.MEDIUM)
        fig3 = Circle(FigureType.CIRCLE, FigurePosition.BOTTOM, FigureSize.BIG)
        fig4 = Triangle(FigureType.TRIANGLE, FigurePosition.CENTER, FigureSize.BIG, FigureOrientation.EAST)
        fig5 = Pie(FigureType.PIE, FigurePosition.CENTER, FigureSize.BIG, FigureOrientation.WEST)
        fig6 = Arrow(FigureType.ARROW, FigurePosition.RIGHT, FigureSize.SMALL, FigureOrientation.NORTH)

        figures = [fig1, fig2, fig3, fig4, fig5, fig6]

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
            else:
                figure.draw(qp, Quadrant.BOTTOM_LEFT)

            i += 1
