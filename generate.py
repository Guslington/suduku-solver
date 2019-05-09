from random import choice, randint

class Generate():

    EASY = [4,5,6,8]
    MEDIUM = [5,6,7,9]
    HARD = [7,8,9]

    def __init__(self, dificulty):
        self.grid = []
        self.game_grid = []
        self.failures = 0
        self.dificulty = dificulty

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

    def sample(self, iterable, n):
        reservoir = []
        for t, item in enumerate(iterable):
            if t < n:
                reservoir.append(item)
            else:
                m = randint(0,t)
                if m < n:
                    reservoir[m] = item
        return reservoir

    def setup_game_grid(self):
        for row in self.grid:
            sample = self.sample(row,choice(self.dificulty))
            game_row = [i if i not in sample else 0 for i in row]
            self.game_grid.append(game_row)
