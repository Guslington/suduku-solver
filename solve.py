from itertools import product

class Solve():

    def __init__(self,grid):
        self.grid = grid
        self.inverse = []
        self.slim_inverse = []
        self.merged = []
        self.choices = {}

    def solve(self):
        for i in range(1000):
            self.add_to_grid()
            if not self.choices: return self.solved()
        return False

    def add_to_grid(self):
        self.generate_choices()
        for r,c in self.choices:
            if self.grid[r][c] != 0:
                self.choices[(r,c)] = []
            if len(self.choices[(r,c)]) == 1:
                self.grid[r][c] = self.choices[(r,c)][0]

    def generate_choices(self):
        self.choices = {}
        for row_pos,row in enumerate(self.grid):
            for col_pos,col in enumerate(row):
                if self.grid[row_pos][col_pos] == 0:
                    unique = set().union(row,self.column(col_pos),self.square(row_pos,col_pos))
                    unique.remove(0)
                    inverse = list(set(range(1,10))-unique)
                    self.choices[(row_pos,col_pos)] = inverse

    def get_inverse(self):
        for i, row in enumerate(self.grid):
            inv_row = list(set(range(1,10))-set(row))
            self.inverse.append([inv_row.pop() if j == 0 else 0 for j in row])
            self.slim_inverse.append(list(set(range(1,10))-set(row)))

    def add_grids(self):
        for i, row in enumerate(self.grid):
            self.merged.append([n+self.inverse[i][j] for j,n in enumerate(row)])

    def solved(self):
        for i, row in enumerate(self.grid):
            if not self.is_unique(row): return False

        for i in range(9):
            if not self.is_unique(self.column(i)): return False

        for i, sq in enumerate(self.squares()):
            if not self.is_unique(sq): return False

        return True

    def is_unique(self,list):
        return True if len(list) == len(set(list)) else False

    def column(self,col):
        return [i[col] for i in self.grid]

    def squares(self):
        squares = []
        for r,c in [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]:
            squares.append(self.square(r,c))
        return squares

    def square(self,row,col):
        col_start = col - col % 3
        col_end = col_start + 3
        row_start = row - row % 3
        square = []
        for i in range(3):
            square += self.grid[(row_start+i)][col_start:col_end]
        return square
