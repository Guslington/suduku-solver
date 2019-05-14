from itertools import product

class Solve():

    def __init__(self,grid):
        self.grid = grid
        self.choices = {}

    def solve(self):
        """
        Solve the puzzle by looping over the rules engine n times
        until a solved puzzled is produced or the puzzle cannot have
        further progress made.
        returns boolean
        """
        for i in range(100):
            self.rules()
            if not self.choices: return self.solved()
        return False

    def rules(self):
        """
        Rules engine to determine whether
        the number fits within it's box
        """
        self.generate_choices()
        for r,c in self.choices:
            """
            RULE 1
            is there is only one choice?
            """
            if len(self.choices[(r,c)]) == 1:
                self.grid[r][c] = self.choices[(r,c)][0]
            """
            RULE 2
            is there a unique choice amongst the row,
            column and square in this list?
            """
            unique = self.unique_choice(r,c)
            if unique:
                self.grid[r][c] = unique[0]


    def generate_choices(self):
        """
        Generates a dictionary of possible choices
        for each remaining position on the grid
        """
        self.choices = {}
        for row_pos,row in enumerate(self.grid):
            for col_pos,col in enumerate(row):
                if self.grid[row_pos][col_pos] == 0:
                    unique = set().union(row,self.column(col_pos),self.square(row_pos,col_pos))
                    unique.remove(0)
                    inverse = list(set(range(1,10))-unique)
                    self.choices[(row_pos,col_pos)] = inverse

    def unique_choice(self,row,col):
        """
        return a list of unique choices amongst the
        row, column and square for a given position
        return list
        """
        position = self.choices[(row,col)]
        unique = []
        unique += self.unique_row(row,col)
        unique += self.unique_column(row,col)
        unique += self.unique_square(row,col)

        return [i for i in position if i not in unique]

    def solved(self):
        """
        Checks to see if the puzzle has been solved correctly
        return boolean
        """
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

    def unique_row(self,row,col):
        rows = []
        for r in range(9):
            if r != row:
                if (r,col) in self.choices:
                    rows += self.choices[(r,col)]
        return list(set(rows))

    def unique_column(self,row,col):
        columns = []
        for c in range(9):
            if c != col:
                if (row,c) in self.choices:
                    columns += self.choices[(row,c)]
        return list(set(columns))

    def unique_square(self,row,col):
        col_start = col - col % 3
        row_start = row - row % 3
        squares = []
        for r in range(3):
            for c in range(3):
                rs = row_start+r
                cs = col_start+c
                if rs != row and cs != col:
                    if (rs,cs) in self.choices:
                        squares += self.choices[(rs,cs)]
        return list(set(squares))
