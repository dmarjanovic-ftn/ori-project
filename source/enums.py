from enum import Enum


class FigureType(Enum):
    SQUARE   = 1
    CIRCLE   = 2
    TRIANGLE = 3
    PIE      = 4
    LINE     = 5
    ARROW    = 6


class FigurePosition(Enum):
    CENTER = 0
    TOP    = 1
    BOTTOM = 2
    LEFT   = 3
    RIGHT  = 4


class FigureOrientation(Enum):
    EAST  = 1
    SOUTH = 2
    WEST  = 3
    NORTH = 4


class FigureSize(Enum):
    SMALLEST = 0
    SMALL    = 1
    MEDIUM   = 2
    BIG      = 3
    BIGGEST  = 4


class Quadrant(Enum):
    TOP_LEFT     = 0
    TOP_RIGHT    = 1
    BOTTOM_LEFT  = 2
    BOTTOM_RIGHT = 3
