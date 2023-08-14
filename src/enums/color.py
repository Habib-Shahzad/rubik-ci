from enum import IntEnum


class Color(IntEnum):
    WHITE = 0
    ORANGE = 1
    GREEN = 2
    RED = 3
    BLUE = 4
    YELLOW = 5


color_to_string = {
    Color.WHITE: "W",
    Color.GREEN: "G",
    Color.RED: "R",
    Color.BLUE: "B",
    Color.ORANGE: "O",
    Color.YELLOW: "Y"
}
