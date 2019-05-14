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

for row in suduku.grid:
    print("|-----------|-----------|-----------|")
    print(f"| {' | '.join([str(i) if i != 0 else ' ' for i in row])} |")

print("|-----------|-----------|-----------|")

print("""
        The Game
""")

for row in suduku.game_grid:
    print("|-----------|-----------|-----------|")
    print(f"| {' | '.join([str(i) if i != 0 else ' ' for i in row])} |")

print("|-----------|-----------|-----------|")

solver = Solve(suduku.game_grid)
result = solver.solve()

print(f"""
        Solved? {result}
""")

for row in solver.grid:
    print("|-----------|-----------|-----------|")
    print(f"| {' | '.join([str(i) if i != 0 else ' ' for i in row])} |")

print("|-----------|-----------|-----------|")
