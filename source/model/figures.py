from abc import abstractmethod
from PySide import QtCore, QtGui


class Figure(object):
    """
    Apstraktna klasa za podrzane objekte
    """
    def __init__(self, fig_type, position, orientation, size, attribute = None):
        self._type = fig_type
        self._position = position
        self._orientation = orientation
        self._size = size
        self._attribute = attribute

    # Parent je QPainter
    @abstractmethod
    def draw(self, parent):
        pass


class Square(Figure):
    """
    Klasa u kojoj iscrtavamo kvadrat
    """
    def draw(self, parent):
        parent.drawRectangle()