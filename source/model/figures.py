from abc import abstractmethod
from PySide import QtCore, QtGui
from source.enums import FigurePosition


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