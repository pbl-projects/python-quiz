

class Sudoku:
    def __init__(self):
        self.board = [
            [0,0,4,3,0,0,2,0,9],
            [0,0,5,0,0,9,0,0,1],
            [0,7,0,0,6,0,0,4,3],
            [0,0,6,0,0,2,0,8,7],
            [1,9,0,0,0,7,4,0,0],
            [0,5,0,0,8,3,0,0,0],
            [6,0,0,0,0,0,1,0,5],
            [0,0,3,5,0,8,6,9,0],
            [0,4,2,9,1,0,3,0,0]
        ]

    def display_board(self):
        for r in range(0,9):
            for c in range(0,9):
                if self.board[r][c] == 0:
                    print(" -", end="")
                else:
                    print(" " + str(self.board[r][c]), end="")
            print()

    def play(self, row, col, val):
        row = row - 1
        col = col - 1
        if row < 0 or col < 0 or row > 8 or col > 8 or val < 1 or val > 9:
            return False
        if self.board[row][col] == 0:
            self.board[row][col] = val
            return True
        else:
            return False

    def completed(self):
        for r in range(0, 9):
            for c in range(0, 9):
                if self.board[r][c] == 0:
                    return False
        return True

    def solved(self):
        pass

print("SUDOKU v1.0")
sudoku = Sudoku()
while not sudoku.completed():
    sudoku.display_board()
    x = int(input("Row: "))
    y = int(input("Col: "))
    val = int(input("Value: "))
    if not sudoku.play(x, y, val):
        print("Wrong position")

sudoku.display_board()
if sudoku.solved():
    print("Congrats!")
else:
    print("Wrong solution")
print("Good bye!")