from generate import Generate

print("""
           =============+
           *   Suduku   *
           =============+
""")

suduku = Generate()
suduku.generate_grid()
suduku.setup_game_grid()

print(f"  {suduku.failures+1} attemps to generate the grid\n\n")

for row in suduku.grid:
    print("|-----------|-----------|-----------|")
    print(f"| {' | '.join([str(i) for i in row])} |")

print("|-----------|-----------|-----------|")
