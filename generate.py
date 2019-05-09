from random import choice

class Generate():

    def __init__(self):
        self.grid = []
        self.failures = 0

    def generate_grid(self):
        i=0
        while i < 9:
            row = self.generate_row()
            if not row:
                self.grid = []
                self.failures+=1
                i=0
            else:
                i+=1
                self.grid.append(row)

    def column(self,col):
        return [i[col] for i in self.grid]

    def square(self,col,row):
        start = col - col % 3
        end = start + 3
        if (row%3) == 0:
            return []
        elif (row%3) == 1:
            return self.grid[(row-1)][start:end]
        elif (row%3) == 2:
            return (self.grid[(row-1)][start:end] + self.grid[(row-2)][start:end])

    def generate_row(self):
        row = []
        failure = []
        numbers = list(range(1,10))

        while len(numbers):
            val = choice(numbers)
            col_pos = len(row)
            row_pos = len(self.grid)

            if val not in self.square(col_pos,row_pos):
                if val not in self.column(col_pos):
                    row.append(val)
                    numbers.remove(val)

            if val in numbers:
                if val not in failure:
                    failure.append(val)
            else:
                failure = []

            if numbers and len(failure) == len(numbers):
                return False

        return row

    def setup_game_grid(self):
        pass
