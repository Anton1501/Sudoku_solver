#sudoku = [ ["1", "0", "9"],
#           [1, ..., 9],
#           [1, ..., 9],
#           [1, ..., 9],
#           [1, ..., 9],
#           [1, ..., 9],
#           [1, ..., 9],
#           [1, ..., 9],
#           [1, ..., 9]
# ]
#            List[List[str]]

import kivy
from array import *


sudoku = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
]

valid_sudoku = [  
            ["6", "3", "9", "5", "7", "4", "1", "8", "2"],
            ["5", "4", "1", "8", "2", "9", "3", "7", "6"],
            ["7", "8", "2", "6", "1", "3", "9", "5", "4"],
            ["1", "9", "8", "4", "6", "7", "5", "2", "3"],
            ["3", "6", "5", "9", "8", "2", "4", "1", "7"],
            ["4", "2", "7", "1", "3", "5", "8", "6", "9"],
            ["9", "5", "6", "7", "4", "8", "2", "3", "1"],
            ["8", "1", "3", "2", "9", "6", "7", "4", "5"],
            ["2", "7", "4", "3", "5", "1", "6", "9", "8"]
]

class Sudoku:
    def __init__(self, sudoku):
        self.soduku = sudoku 

    def solve(self):
        pass
    
    def sudoku_right(self, board: list[list[str]]) -> bool:
        found = set()
    
        for i in range(9): # spalte
            for j in range(9): # zeile
                value = board[i][j]

                if value != "0":
                    row = f"row-{i}-{value}"
                    col = f"col-{j}-{value}"
                    box = f"box-{i//3}-{j//3}-{value}"

                if row in found or col in found or box in found:
                    return False

                else:
                    found.add(row)
                    found.add(col)
                    found.add(box)

        return True    


    def display(self):
        for i in sudoku:
            print(f"{i}\n")
        
class App:

    def __init__(self):
         pass

    def start(self):
        print("App has started ...")
        

    def stop(self):
        print("App has stopped...")