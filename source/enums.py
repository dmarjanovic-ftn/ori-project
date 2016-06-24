from enum import Enum


class FigureType(Enum):
    SQUARE = 1
    CIRCLE = 2
    LINE   = 3
    ARROW  = 4


class FigurePosition(Enum):
    CENTER = 0
    TOP    = 1
    BOTTOM = 2
    LEFT   = 3
    RIGHT  = 4


class FigureOrientation(Enum):
    EAST  = 1
    WEST  = 2
    SOUTH = 3
    NORTH = 4


class FigureSize(Enum):
    SMALL  = 1
    MEDIUM = 2
    BIG    = 3
