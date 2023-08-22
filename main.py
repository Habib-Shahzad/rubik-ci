from itertools import product
from src import RubiksCube, POSSIBLE_MOVES


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


N = 5
cube = RubiksCube()
cube.scramble(N)  # Scramble the cube with N random moves

print("Scrambled Cube: ")
cube.show()


solution = BruteForceSolver.solve(cube, N)

if solution is not None:
    cube.scramble_moves(solution)
    print()
    cube.show()
