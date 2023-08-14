import numpy as np
import matplotlib.pyplot as plt

from ..enums import *
from ..constants import COLORS


class RubiksCube:
    def __init__(self) -> None:
        self.cube = {face: np.zeros((3, 3)) for face in CubeSide}
        self.initialize()

    def initialize(self):
        face_keys = list(self.cube.keys())
        for index, color in enumerate(COLORS):
            self.cube[face_keys[index]] = np.full((3, 3), color)

    def get_colored_face(self, face: CubeSide):
        def int_to_color(key): return color_to_string[key]
        return np.vectorize(int_to_color)(self.cube[face].copy())

    def display_face(self, face: CubeSide):
        print(face_to_string[face])
        print(self.get_colored_face(face))

    def display(self):
        for face in self.cube:
            print(face_to_string[face])
            print(self.get_colored_face(face))
            print()

    def show(self):
        spacing = f'{" " * (len(str(self.cube[CubeSide.TOP][0])) + 2)}'
        sides = list(CubeSide)
        colored_cube = {side: self.get_colored_face(side) for side in sides}
        l1 = '\n'.join(spacing + str(c) for c in colored_cube[CubeSide.TOP])
        l2 = '\n'.join('  '.join(str(colored_cube[sides[i]][j]) for i in range(
            1, 5)) for j in range(len(colored_cube[CubeSide.TOP])))
        l3 = '\n'.join(spacing + str(c) for c in colored_cube[CubeSide.BOTTOM])
        print(f'{l1}\n\n{l2}\n\n{l3}')
