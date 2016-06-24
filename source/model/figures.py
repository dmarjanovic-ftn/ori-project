from abc import abstractmethod
from PySide import QtCore, QtGui
from source.enums import FigurePosition, FigureOrientation
from source.consts import *


class Figure(object):
    """
    Apstraktna klasa za podrzane objekte
    """
    def __init__(self, fig_type, position, size, orientation = None, attribute = None):
        self._type = fig_type
        self._position = position
        self._orientation = orientation
        self._size = size
        self._attribute = attribute

    # Parent je QPainter
    @abstractmethod
    def draw(self, parent, quadrant):
        pass


class Square(Figure):
    """
    Klasa u kojoj iscrtavamo kvadrat
    """
    def draw(self, parent, quadrant):

        dimension = 20 + self._size.value * 30

        x, y = 360 * (quadrant.value % 2), 360 * (quadrant.value // 2)
        padding = (120 - dimension) // 2

        x += padding
        y += padding

        if self._position == FigurePosition.CENTER:
            x += 120
            y += 120
        elif self._position == FigurePosition.TOP:
            x += 120
        elif self._position == FigurePosition.LEFT:
            y += 120
        elif self._position == FigurePosition.RIGHT:
            y += 120
            x += 240
        elif self._position == FigurePosition.BOTTOM:
            y += 240

        parent.drawRect(x, y, dimension, dimension)


class Circle(Figure):
    """
    Klasa u kojoj iscrtavamo krug
    """

    def draw(self, parent, quadrant):

        dimension = 20 + self._size.value * 30

        x, y = 360 * (quadrant.value % 2), 360 * (quadrant.value // 2)
        padding = (120 - dimension) // 2

        x += padding
        y += padding

        if self._position == FigurePosition.CENTER:
            x += 120
            y += 120
        elif self._position == FigurePosition.TOP:
            x += 120
        elif self._position == FigurePosition.LEFT:
            y += 120
        elif self._position == FigurePosition.RIGHT:
            y += 120
            x += 240
        elif self._position == FigurePosition.BOTTOM:
            y += 240

        parent.drawEllipse(x, y, dimension, dimension)


class Triangle(Figure):
    """
    Klasa u kojoj iscrtavamo trougao
    """

    def draw(self, parent, quadrant):
        line_length = Sizes.FIXED_FIGURE_SIZE + self._size.value * Sizes.FIGURE_SIZE_PARAM
        triangle_height = line_length * 1.73 / 2.0

        x, y = Sizes.QUADRANT_WIDTH * (quadrant.value % 2), Sizes.QUADRANT_HEIGHT * (quadrant.value // 2)
        padding = (Sizes.CELL_WIDTH - line_length) // 2

        x += padding
        y += padding

        if self._position == FigurePosition.CENTER:
            x += Sizes.CELL_WIDTH
            y += Sizes.CELL_HEIGHT
        elif self._position == FigurePosition.TOP:
            x += Sizes.CELL_WIDTH
        elif self._position == FigurePosition.LEFT:
            y += Sizes.CELL_HEIGHT
        elif self._position == FigurePosition.RIGHT:
            y += Sizes.CELL_HEIGHT
            x += 2 * Sizes.CELL_WIDTH
        elif self._position == FigurePosition.BOTTOM:
            y += 2 * Sizes.CELL_HEIGHT

        if self._orientation == FigureOrientation.NORTH:
            parent.drawLine(x + line_length/2, y, x + line_length, y + triangle_height)
            parent.drawLine(x + line_length, y + triangle_height, x, y + triangle_height)
            parent.drawLine(x, y + triangle_height, x + line_length/2, y)
        elif self._orientation == FigureOrientation.EAST:
            parent.drawLine(x + line_length, y + line_length/2, x + line_length - triangle_height, y + line_length)
            parent.drawLine(x + line_length - triangle_height, y + line_length, x + line_length - triangle_height, y)
            parent.drawLine(x + line_length - triangle_height, y, x + line_length, y + line_length/2)
        elif self._orientation == FigureOrientation.SOUTH:
            parent.drawLine(x + line_length/2, y + line_length, x + line_length, y + line_length - triangle_height)
            parent.drawLine(x + line_length, y + line_length - triangle_height, x, y + line_length - triangle_height)
            parent.drawLine(x, y + line_length - triangle_height, x + line_length/2, y + line_length)
        elif self._orientation == FigureOrientation.WEST:
            parent.drawLine(x, y + line_length/2, x + triangle_height, y + line_length)
            parent.drawLine(x + triangle_height, y + line_length, x + triangle_height, y)
            parent.drawLine(x + triangle_height, y, x, y + line_length/2)


class Pie(Circle):
    def draw(self, parent, quadrant):

        dimension = 20 + self._size.value * 30

        x, y = 360 * (quadrant.value % 2), 360 * (quadrant.value // 2)
        padding = (120 - dimension) // 2

        x += padding
        y += padding

        if self._position == FigurePosition.CENTER:
            x += 120
            y += 120
        elif self._position == FigurePosition.TOP:
            x += 120
        elif self._position == FigurePosition.LEFT:
            y += 120
        elif self._position == FigurePosition.RIGHT:
            y += 120
            x += 240
        elif self._position == FigurePosition.BOTTOM:
            y += 240

        if self._orientation == FigureOrientation.NORTH:
            parent.drawPie(x, y, dimension, dimension, 0, 12 * 360)
        elif self._orientation == FigureOrientation.EAST:
            parent.drawPie(x, y, dimension, dimension, 4 * 360, 12 * 360)
        elif self._orientation == FigureOrientation.SOUTH:
            parent.drawPie(x, y, dimension, dimension, 8 * 360, 12 * 360)
        elif self._orientation == FigureOrientation.WEST:
            parent.drawPie(x, y, dimension, dimension, 12 * 360, 12 * 360)


class Line(Figure):
    """
    Klasa u kojoj iscrtavamo liniju
    """

    def draw(self, parent, quadrant):
        line_length = Sizes.FIXED_FIGURE_SIZE + self._size.value * Sizes.FIGURE_SIZE_PARAM

        x, y = Sizes.QUADRANT_WIDTH * (quadrant.value % 2), Sizes.QUADRANT_HEIGHT * (quadrant.value // 2)
        padding = (Sizes.CELL_WIDTH - line_length) // 2

        x += padding
        y += padding

        if self._position == FigurePosition.CENTER:
            x += Sizes.CELL_WIDTH
            y += Sizes.CELL_HEIGHT
        elif self._position == FigurePosition.TOP:
            x += Sizes.CELL_WIDTH
        elif self._position == FigurePosition.LEFT:
            y += Sizes.CELL_HEIGHT
        elif self._position == FigurePosition.RIGHT:
            y += Sizes.CELL_HEIGHT
            x += 2 * Sizes.CELL_WIDTH
        elif self._position == FigurePosition.BOTTOM:
            y += 2 * Sizes.CELL_HEIGHT

        if self._orientation == FigureOrientation.WEST or self._orientation == FigureOrientation.EAST:
            parent.drawLine(x, y, x + line_length, y)
        elif self._orientation == FigureOrientation.SOUTH or self._orientation == FigureOrientation.NORTH:
            parent.drawLine(x, y, x, y + line_length)


class Arrow(Figure):
    """
    Klasa u kojoj iscrtavamo strelicu
    """

    def draw(self, parent, quadrant):
        line_length = Sizes.FIXED_FIGURE_SIZE + self._size.value * Sizes.FIGURE_SIZE_PARAM

        x, y = Sizes.QUADRANT_WIDTH * (quadrant.value % 2), Sizes.QUADRANT_HEIGHT * (quadrant.value // 2)
        padding = (Sizes.CELL_WIDTH - line_length) // 2

        x += padding
        y += padding

        if self._position == FigurePosition.CENTER:
            x += Sizes.CELL_WIDTH
            y += Sizes.CELL_HEIGHT
        elif self._position == FigurePosition.TOP:
            x += Sizes.CELL_WIDTH
        elif self._position == FigurePosition.LEFT:
            y += Sizes.CELL_HEIGHT
        elif self._position == FigurePosition.RIGHT:
            y += Sizes.CELL_HEIGHT
            x += 2 * Sizes.CELL_WIDTH
        elif self._position == FigurePosition.BOTTOM:
            y += 2 * Sizes.CELL_HEIGHT

        if self._orientation == FigureOrientation.EAST:
            parent.drawLine(x, y, x + line_length, y)
            parent.drawLine(x + line_length - 4, y - 4, x + line_length, y)
            parent.drawLine(x + line_length - 4, y + 4, x + line_length, y)
        elif self._orientation == FigureOrientation.WEST:
            parent.drawLine(x, y, x + line_length, y)
            parent.drawLine(x + 4, y - 4, x, y)
            parent.drawLine(x + 4, y + 4, x, y)
        elif self._orientation == FigureOrientation.SOUTH:
            parent.drawLine(x, y, x, y + line_length)
            parent.drawLine(x - 4, y + line_length - 4, x, y + line_length)
            parent.drawLine(x + 4, y + line_length - 4, x, y + line_length)
        elif self._orientation == FigureOrientation.NORTH:
            parent.drawLine(x, y, x, y + line_length)
            parent.drawLine(x - 4, y + 4, x, y)
            parent.drawLine(x + 4, y + 4, x, y)