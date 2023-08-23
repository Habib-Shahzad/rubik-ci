from itertools import product
from ..constants import POSSIBLE_MOVES
from ..cube import RubiksCube


class BruteForceSolver:

    def solve(cube: RubiksCube, N: int):
        permutations = list(product(POSSIBLE_MOVES, repeat=N))
        for move_list in permutations:
            move_list = list(move_list)
            temp_cube = RubiksCube(cube.cube)
            temp_cube.scramble_moves(move_list)
            if (temp_cube.is_solved()):
                print("Solution: ", move_list)
                return move_list

        print("No solution found")
