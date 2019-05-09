class Solve():

    def __init__(self,grid):
        self.grid = grid

    def solved(self):
        solved = True
        for row in self.grid:
            if 0 in row:
                solved = False
        return solved

    def column(self,col):
        return [i[col] for i in self.grid]

    def square(self,col,row):
        col_start = col - col % 3
        col_end = col_start + 3
        row_start = row - row % 3
        square = []
        for i in range(3):
            square += self.grid[(row_start+i)][col_start:col_end]
        return square

    def brute_force(self):
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if val == 0:
                    col = self.column(j)
                    square = self.square(j,i)
                    for n in list(range(1, 10)):
                        if n not in col and n not in row and n not in square:
                            self.grid[i][j] = n
                            break
