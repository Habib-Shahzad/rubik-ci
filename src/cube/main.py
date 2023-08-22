import numpy as np
from ..enums import *
from ..constants import COLORS, POSSIBLE_MOVES


class RubiksCube:
    def __init__(self, cube=None) -> None:
        if cube is None:
            self.cube = {face: np.zeros((3, 3)) for face in CubeSide}
            self.initialize()
        else:
            self.cube = {
                face: np.array(cube[face]) for face in CubeSide
            }

    def initialize(self):
        face_keys = list(self.cube.keys())
        for index, color in enumerate(COLORS):
            self.cube[face_keys[index]] = np.full((3, 3), color)

    def scramble_moves(self, moves=[]):
        for move in moves:
            self.twist(move)

    def scramble(self, n=40):
        moves = POSSIBLE_MOVES
        for _ in range(n):
            move = np.random.choice(moves)
            self.twist(move)

    def twist(self, move: str):
        if move == 'F':
            self.move_F()
        elif move == 'R':
            self.move_R()
        elif move == 'U':
            self.move_U()
        elif move == 'B':
            self.move_B()
        elif move == 'L':
            self.move_L()
        elif move == 'D':
            self.move_D()

        elif move == "F'":
            self.move_F_prime()
        elif move == "R'":
            self.move_R_prime()
        elif move == "U'":
            self.move_U_prime()
        elif move == "B'":
            self.move_B_prime()
        elif move == "L'":
            self.move_L_prime()
        elif move == "D'":
            self.move_D_prime()

    def get_colored_face(self, face: CubeSide, colored=True):
        def int_to_color(key):
            if colored:
                return color_to_string[key]
            else:
                return face_to_string[key]

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
        print()

    def is_solved(self):
        for face in self.cube:
            if len(set(self.cube[face].flatten())) != 1:
                return False
        return True


# ------------------- Moves -------------------#
# F R U B L D F' R' U' B' L' D'


    @staticmethod
    def get_moves_complement(moves):
        complement = []
        for move in moves:
            if move[-1] == "'":
                complement.append(move[:-1])
            else:
                complement.append(move + "'")
        return list(reversed(complement))

    def flip_face_vertical(self, side: CubeSide, axis=0):
        self.cube[side] = np.transpose(self.cube[side])
        self.cube[side] = np.flip(self.cube[side], axis)

    def flip_face_horizontal(self, side: CubeSide, axis=0):
        self.cube[side] = np.flip(self.cube[side], axis)
        self.cube[side] = np.transpose(self.cube[side])

    def move_F(self):
        top_row = self.cube[CubeSide.TOP][2, :].copy()
        right_col = self.cube[CubeSide.RIGHT][:, 0].copy()
        bottom_col = self.cube[CubeSide.BOTTOM][0, :].copy()
        left_col = self.cube[CubeSide.LEFT][:, 2].copy()

        self.cube[CubeSide.TOP][2, :] = left_col[::-1]
        self.cube[CubeSide.RIGHT][:, 0] = top_row
        self.cube[CubeSide.BOTTOM][0, :] = right_col[::-1]
        self.cube[CubeSide.LEFT][:, 2] = bottom_col

        self.flip_face_horizontal(CubeSide.FRONT)

    def move_F_prime(self):
        top_row = self.cube[CubeSide.TOP][2, :].copy()
        right_col = self.cube[CubeSide.RIGHT][:, 0].copy()
        bottom_col = self.cube[CubeSide.BOTTOM][0, :].copy()
        left_col = self.cube[CubeSide.LEFT][:, 2].copy()

        self.cube[CubeSide.TOP][2, :] = right_col
        self.cube[CubeSide.RIGHT][:, 0] = bottom_col[::-1]
        self.cube[CubeSide.BOTTOM][0, :] = left_col
        self.cube[CubeSide.LEFT][:, 2] = top_row[::-1]

        self.flip_face_horizontal(CubeSide.FRONT, 1)

    def move_R(self):
        top_col = self.cube[CubeSide.TOP][:, 2].copy()
        back_col = self.cube[CubeSide.BACK][:, 0].copy()
        bottom_col = self.cube[CubeSide.BOTTOM][:, 2].copy()
        front_col = self.cube[CubeSide.FRONT][:, 2].copy()

        self.cube[CubeSide.TOP][:, 2] = front_col
        self.cube[CubeSide.FRONT][:, 2] = bottom_col
        self.cube[CubeSide.BOTTOM][:, 2] = back_col[::-1]
        self.cube[CubeSide.BACK][:, 0] = top_col[::-1]

        self.flip_face_horizontal(CubeSide.RIGHT)

    def move_R_prime(self):
        top_col = self.cube[CubeSide.TOP][:, 2].copy()
        back_col = self.cube[CubeSide.BACK][:, 0].copy()
        bottom_col = self.cube[CubeSide.BOTTOM][:, 2].copy()
        front_col = self.cube[CubeSide.FRONT][:, 2].copy()

        self.cube[CubeSide.TOP][:, 2] = back_col[::-1]
        self.cube[CubeSide.BACK][:, 0] = bottom_col[::-1]
        self.cube[CubeSide.BOTTOM][:, 2] = front_col
        self.cube[CubeSide.FRONT][:, 2] = top_col

        self.flip_face_horizontal(CubeSide.RIGHT, 1)

    def move_U(self):
        front_row = self.cube[CubeSide.FRONT][0, :].copy()
        right_row = self.cube[CubeSide.RIGHT][0, :].copy()
        back_row = self.cube[CubeSide.BACK][0, :].copy()
        left_row = self.cube[CubeSide.LEFT][0, :].copy()

        self.cube[CubeSide.FRONT][0, :] = right_row
        self.cube[CubeSide.RIGHT][0, :] = back_row
        self.cube[CubeSide.BACK][0, :] = left_row
        self.cube[CubeSide.LEFT][0, :] = front_row

        self.flip_face_vertical(CubeSide.TOP, 1)

    def move_U_prime(self):
        front_row = self.cube[CubeSide.FRONT][0, :].copy()
        right_row = self.cube[CubeSide.RIGHT][0, :].copy()
        back_row = self.cube[CubeSide.BACK][0, :].copy()
        left_row = self.cube[CubeSide.LEFT][0, :].copy()

        self.cube[CubeSide.FRONT][0, :] = left_row
        self.cube[CubeSide.RIGHT][0, :] = front_row
        self.cube[CubeSide.BACK][0, :] = right_row
        self.cube[CubeSide.LEFT][0, :] = back_row

        self.flip_face_vertical(CubeSide.TOP)

    def move_B(self):
        top_row = self.cube[CubeSide.TOP][0, :].copy()
        bottom_col = self.cube[CubeSide.BOTTOM][2, :].copy()
        right_col = self.cube[CubeSide.RIGHT][:, 2].copy()
        left_col = self.cube[CubeSide.LEFT][:, 0].copy()

        self.cube[CubeSide.TOP][0, :] = right_col
        self.cube[CubeSide.RIGHT][:, 2] = bottom_col[::-1]
        self.cube[CubeSide.BOTTOM][2, :] = left_col
        self.cube[CubeSide.LEFT][:, 0] = top_row[::-1]

        self.flip_face_horizontal(CubeSide.BACK)

    def move_B_prime(self):
        top_row = self.cube[CubeSide.TOP][0, :].copy()
        bottom_col = self.cube[CubeSide.BOTTOM][2, :].copy()
        right_col = self.cube[CubeSide.RIGHT][:, 2].copy()
        left_col = self.cube[CubeSide.LEFT][:, 0].copy()

        self.cube[CubeSide.TOP][0, :] = left_col[::-1]
        self.cube[CubeSide.LEFT][:, 0] = bottom_col
        self.cube[CubeSide.BOTTOM][2, :] = right_col[::-1]
        self.cube[CubeSide.RIGHT][:, 2] = top_row

        self.flip_face_horizontal(CubeSide.BACK, 1)

    def move_L(self):
        top_col = self.cube[CubeSide.TOP][:, 0].copy()
        back_col = self.cube[CubeSide.BACK][:, 2].copy()
        bottom_col = self.cube[CubeSide.BOTTOM][:, 0].copy()
        front_col = self.cube[CubeSide.FRONT][:, 0].copy()

        self.cube[CubeSide.TOP][:, 0] = back_col[::-1]
        self.cube[CubeSide.BACK][:, 2] = bottom_col[::-1]
        self.cube[CubeSide.BOTTOM][:, 0] = front_col
        self.cube[CubeSide.FRONT][:, 0] = top_col

        self.flip_face_horizontal(CubeSide.LEFT)

    def move_L_prime(self):
        top_col = self.cube[CubeSide.TOP][:, 0].copy()
        back_col = self.cube[CubeSide.BACK][:, 2].copy()
        bottom_col = self.cube[CubeSide.BOTTOM][:, 0].copy()
        front_col = self.cube[CubeSide.FRONT][:, 0].copy()

        self.cube[CubeSide.TOP][:, 0] = front_col
        self.cube[CubeSide.FRONT][:, 0] = bottom_col
        self.cube[CubeSide.BOTTOM][:, 0] = back_col[::-1]
        self.cube[CubeSide.BACK][:, 2] = top_col[::-1]

        self.flip_face_horizontal(CubeSide.LEFT, 1)

    def move_D(self):
        front_row = self.cube[CubeSide.FRONT][2, :].copy()
        right_row = self.cube[CubeSide.RIGHT][2, :].copy()
        back_row = self.cube[CubeSide.BACK][2, :].copy()
        left_row = self.cube[CubeSide.LEFT][2, :].copy()

        self.cube[CubeSide.FRONT][2, :] = left_row
        self.cube[CubeSide.RIGHT][2, :] = front_row
        self.cube[CubeSide.BACK][2, :] = right_row
        self.cube[CubeSide.LEFT][2, :] = back_row

        self.flip_face_vertical(CubeSide.BOTTOM, 1)

    def move_D_prime(self):
        front_row = self.cube[CubeSide.FRONT][2, :].copy()
        right_row = self.cube[CubeSide.RIGHT][2, :].copy()
        back_row = self.cube[CubeSide.BACK][2, :].copy()
        left_row = self.cube[CubeSide.LEFT][2, :].copy()

        self.cube[CubeSide.FRONT][2, :] = right_row
        self.cube[CubeSide.RIGHT][2, :] = back_row
        self.cube[CubeSide.BACK][2, :] = left_row
        self.cube[CubeSide.LEFT][2, :] = front_row

        self.flip_face_vertical(CubeSide.BOTTOM)
