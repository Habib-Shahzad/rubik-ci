from enum import IntEnum


class CubeSide(IntEnum):
    TOP = 0
    LEFT = 1
    FRONT = 2
    RIGHT = 3
    BACK = 4
    BOTTOM = 5


face_to_string = {
    CubeSide.TOP: "Top",
    CubeSide.LEFT: "Left",
    CubeSide.FRONT: "Front",
    CubeSide.RIGHT: "Right",
    CubeSide.BACK: "Back",
    CubeSide.BOTTOM: "Bottom"
}
