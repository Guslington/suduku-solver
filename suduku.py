from generate import Generate
from solve import Solve

print("""
           =============+
           *   Suduku   *
           =============+
""")

suduku = Generate(Generate.EASY)
suduku.generate_grid()
suduku.setup_game_grid()

print(f"  {suduku.failures+1} attemps to generate the grid\n\n")

for row in suduku.game_grid:
    print("|-----------|-----------|-----------|")
    print(f"| {' | '.join([str(i) if i != 0 else ' ' for i in row])} |")

print("|-----------|-----------|-----------|")

solver = Solve(suduku.game_grid)
solver.brute_force()

print("""

              # Solver #

""")

for row in solver.grid:
    print("|-----------|-----------|-----------|")
    print(f"| {' | '.join([str(i) if i != 0 else ' ' for i in row])} |")

print("|-----------|-----------|-----------|")

print("""

             # Original #

""")

for row in suduku.grid:
    print("|-----------|-----------|-----------|")
    print(f"| {' | '.join([str(i) if i != 0 else ' ' for i in row])} |")

print("|-----------|-----------|-----------|")
