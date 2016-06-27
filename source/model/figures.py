from abc import abstractmethod
from source.enums import FigurePosition, FigureOrientation
from source.consts import *


class Figure(object):
    """
    Apstraktna klasa za podrzane objekte
    """
    def __init__(self, fig_type, position, size, orientation=None, attribute=None):
        self._type = fig_type
        self._position = position
        self._orientation = orientation
        self._size = size
        self._attribute = attribute

    # Parent je QPainter
    @abstractmethod
    def draw(self, parent, quadrant, scale=1):
        pass

    def __str__(self):
        return str(self._type.value) + "," + str(self._position.value) + "," + str(self._orientation.value) + "," \
            + str(self._size.value)

    def __repr__(self):
        return str(self._type) + "," + str(self._position)


class Square(Figure):
    """
    Klasa u kojoj iscrtavamo kvadrat
    """
    def draw(self, parent, quadrant, scale=1):

        dimension = Sizes.FIXED_FIGURE_SIZE // scale + self._size.value * Sizes.FIGURE_SIZE_PARAM // scale

        x = (Sizes.QUADRANT_WIDTH // scale) * (quadrant.value % 2)
        y = (Sizes.QUADRANT_HEIGHT // scale) * (quadrant.value // 2)
        padding = (Sizes.CELL_WIDTH // scale - dimension) // 2

        if scale == 1:
            x += padding
            y += padding
        else:
            x += 4
            y += 4

        if self._position == FigurePosition.CENTER:
            x += Sizes.CELL_WIDTH  // scale
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.TOP:
            x += Sizes.CELL_WIDTH  // scale
        elif self._position == FigurePosition.LEFT:
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.RIGHT:
            y += Sizes.CELL_HEIGHT // scale
            x += 2 * Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.BOTTOM:
            x += Sizes.CELL_WIDTH // scale
            y += 2 * Sizes.CELL_HEIGHT // scale

        parent.drawRect(x, y, dimension, dimension)


class Circle(Figure):
    """
    Klasa u kojoj iscrtavamo krug
    """
    def draw(self, parent, quadrant, scale=1):

        dimension = Sizes.FIXED_FIGURE_SIZE // scale + self._size.value * Sizes.FIGURE_SIZE_PARAM // scale

        x = (Sizes.QUADRANT_WIDTH // scale) * (quadrant.value % 2)
        y = (Sizes.QUADRANT_HEIGHT // scale) * (quadrant.value // 2)
        padding = (Sizes.CELL_WIDTH // scale - dimension) // 2

        if scale == 1:
            x += padding
            y += padding
        else:
            x += 4
            y += 4

        if self._position == FigurePosition.CENTER:
            x += Sizes.CELL_WIDTH // scale
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.TOP:
            x += Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.LEFT:
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.RIGHT:
            y += Sizes.CELL_HEIGHT // scale
            x += 2 * Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.BOTTOM:
            y += 2 * Sizes.CELL_HEIGHT // scale
            x += Sizes.CELL_WIDTH // scale

        parent.drawEllipse(x, y, dimension, dimension)


class Triangle(Figure):
    """
    Klasa u kojoj iscrtavamo trougao
    """
    def draw(self, parent, quadrant, scale=1):
        line_length = Sizes.FIXED_FIGURE_SIZE // scale + self._size.value * Sizes.FIGURE_SIZE_PARAM // scale
        triangle_height = line_length * 1.73 / 2.0

        x = (Sizes.QUADRANT_WIDTH // scale) * (quadrant.value % 2)
        y = (Sizes.QUADRANT_HEIGHT // scale) * (quadrant.value // 2)
        padding = (Sizes.CELL_WIDTH // scale - line_length) // 2

        if scale == 1:
            x += padding
            y += padding
        else:
            x += 4
            y += 4

        if self._position == FigurePosition.CENTER:
            x += Sizes.CELL_WIDTH // scale
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.TOP:
            x += Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.LEFT:
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.RIGHT:
            y += Sizes.CELL_HEIGHT // scale
            x += 2 * Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.BOTTOM:
            y += 2 * Sizes.CELL_HEIGHT // scale
            x += Sizes.CELL_WIDTH // scale

        if self._orientation == FigureOrientation.NORTH:
            parent.drawLine(x + line_length / 2, y, x + line_length, y + triangle_height)
            parent.drawLine(x + line_length, y + triangle_height, x, y + triangle_height)
            parent.drawLine(x, y + triangle_height, x + line_length / 2, y)
        elif self._orientation == FigureOrientation.EAST:
            parent.drawLine(x + line_length, y + line_length / 2, x + line_length - triangle_height, y + line_length)
            parent.drawLine(x + line_length - triangle_height, y + line_length, x + line_length - triangle_height, y)
            parent.drawLine(x + line_length - triangle_height, y, x + line_length, y + line_length / 2)
        elif self._orientation == FigureOrientation.SOUTH:
            parent.drawLine(x + line_length / 2, y + line_length, x + line_length, y + line_length - triangle_height)
            parent.drawLine(x + line_length, y + line_length - triangle_height, x, y + line_length - triangle_height)
            parent.drawLine(x, y + line_length - triangle_height, x + line_length / 2, y + line_length)
        elif self._orientation == FigureOrientation.WEST:
            parent.drawLine(x, y + line_length / 2, x + triangle_height, y + line_length)
            parent.drawLine(x + triangle_height, y + line_length, x + triangle_height, y)
            parent.drawLine(x + triangle_height, y, x, y + line_length / 2)


class Pie(Circle):
    """
    Klasa u kojoj iscrtavamo pitu
    """
    def draw(self, parent, quadrant, scale=1):

        dimension = Sizes.FIXED_FIGURE_SIZE // scale + self._size.value * Sizes.FIGURE_SIZE_PARAM // scale

        x = (Sizes.QUADRANT_WIDTH // scale) * (quadrant.value % 2)
        y = (Sizes.QUADRANT_HEIGHT // scale) * (quadrant.value // 2)
        padding = (Sizes.CELL_WIDTH // scale - dimension) // 2

        if scale == 1:
            x += padding
            y += padding
        else:
            x += 4
            y += 4

        if self._position == FigurePosition.CENTER:
            x += Sizes.CELL_WIDTH // scale
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.TOP:
            x += Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.LEFT:
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.RIGHT:
            y += Sizes.CELL_HEIGHT // scale
            x += 2 * Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.BOTTOM:
            x += Sizes.CELL_WIDTH // scale
            y += 2 * Sizes.CELL_HEIGHT // scale

        if self._orientation == FigureOrientation.NORTH:
            parent.drawPie(x, y, dimension, dimension, 6 * 360, 12 * 360)
        elif self._orientation == FigureOrientation.EAST:
            parent.drawPie(x, y, dimension, dimension, 2 * 360, 12 * 360)
        elif self._orientation == FigureOrientation.SOUTH:
            parent.drawPie(x, y, dimension, dimension, 14 * 360, 12 * 360)
        elif self._orientation == FigureOrientation.WEST:
            parent.drawPie(x, y, dimension, dimension, 10 * 360, 12 * 360)


class Line(Figure):
    """
    Klasa u kojoj iscrtavamo liniju
    """
    def draw(self, parent, quadrant, scale=1):
        line_length = Sizes.FIXED_FIGURE_SIZE // scale + self._size.value * Sizes.FIGURE_SIZE_PARAM // scale

        x = (Sizes.QUADRANT_WIDTH // scale) * (quadrant.value % 2)
        y = (Sizes.QUADRANT_HEIGHT // scale) * (quadrant.value // 2)
        padding = (Sizes.CELL_WIDTH // scale - line_length) // 2

        if self._orientation == FigureOrientation.NORTH or self._orientation == FigureOrientation.SOUTH:
            x += (Sizes.CELL_WIDTH // scale) // 2
            y += padding
        else:
            y += (Sizes.CELL_HEIGHT // scale) // 2
            x += padding

        if self._position == FigurePosition.CENTER:
            x += Sizes.CELL_WIDTH // scale
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.TOP:
            x += Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.LEFT:
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.RIGHT:
            y += Sizes.CELL_HEIGHT // scale
            x += 2 * Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.BOTTOM:
            y += 2 * Sizes.CELL_HEIGHT // scale
            x += Sizes.CELL_WIDTH // scale

        if self._orientation == FigureOrientation.WEST or self._orientation == FigureOrientation.EAST:
            parent.drawLine(x, y, x + line_length, y)
        elif self._orientation == FigureOrientation.SOUTH or self._orientation == FigureOrientation.NORTH:
            parent.drawLine(x, y, x, y + line_length)


class Arrow(Figure):
    """
    Klasa u kojoj iscrtavamo strelicu
    """
    def draw(self, parent, quadrant, scale=1):
        line_length = Sizes.FIXED_FIGURE_SIZE // scale + self._size.value * Sizes.FIGURE_SIZE_PARAM // scale

        x = (Sizes.QUADRANT_WIDTH  // scale) * (quadrant.value % 2)
        y = (Sizes.QUADRANT_HEIGHT // scale) * (quadrant.value // 2)
        padding = (Sizes.CELL_WIDTH // scale - line_length) // 2

        if self._orientation == FigureOrientation.NORTH or self._orientation == FigureOrientation.SOUTH:
            x += (Sizes.CELL_WIDTH // scale) // 2
            y += padding
        else:
            y += (Sizes.CELL_HEIGHT // scale) // 2
            x += padding

        if self._position == FigurePosition.CENTER:
            x += Sizes.CELL_WIDTH // scale
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.TOP:
            x += Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.LEFT:
            y += Sizes.CELL_HEIGHT // scale
        elif self._position == FigurePosition.RIGHT:
            y += Sizes.CELL_HEIGHT // scale
            x += 2 * Sizes.CELL_WIDTH // scale
        elif self._position == FigurePosition.BOTTOM:
            x += Sizes.CELL_WIDTH // scale
            y += 2 * Sizes.CELL_HEIGHT // scale

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
