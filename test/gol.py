import random


class GameOfLife:
    def __init__(self, width, height, density):
        self.width = width
        self.height = height
        self.density = density
        self.board = []
        self.next = []

    def initialize(self):
        for r in range(0, self.height):
            row = []
            next_row = []
            for c in range(0, self.width):
                v = random.randint(0, 100)
                if v < self.density:
                    row.append(1)
                else:
                    row.append(0)
                next_row.append(0)
            self.board.append(row)
            self.next.append(next_row)

    def display(self):
        for r in range(0, self.height):
            for c in range(0, self.width):
                if self.board[r][c] == 0:
                    print(" -", end="")
                else:
                    print(" " + str(self.board[r][c]), end="")
            print()

    def calculate_next(self):
        for r in range(0, self.height):
            for c in range(0, self.width):
                n = self.get_neighbours(r, c)
                # print(" " + str(n), end="")
                if n == 2:
                    self.next[r][c] = self.board[r][c]
                elif n == 3:
                    self.next[r][c] = 1
                else:
                    self.next[r][c] = 0
            # print()
        for r in range(0, self.height):
            for c in range(0, self.width):
                self.board[r][c] = self.next[r][c]

    def get_neighbours(self, r, c):
        total = 0
        start_row = r - 1
        if r == 0:
            start_row = 0
        start_col = c - 1
        if c == 0:
            start_col = 0
        end_row = r + 1
        if end_row == self.height:
            end_row = r
        end_col = c + 1
        if end_col == self.width:
            end_col = c
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                if row == r and col == c:
                    pass
                else:
                    total = total + self.board[row][col]
        return total

g = GameOfLife(10, 10, 50)
g.initialize()
while True:
    g.display()
    ans = input("next? ")
    if ans == 'y':
        g.calculate_next()
    else:
        print("Bye!")
        break