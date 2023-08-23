from src import RubiksCube, BruteForceSolver


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
