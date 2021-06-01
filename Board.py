from typing import Tuple


class Board:
    def __init__(self) -> None:
        self.board = [[0] * 20 for i in range(20)]
        self.destination_x = 19
        self.destination_y = 19
        self.x = 0
        self.y = 0
        self.board[self.x][self.y] = "X"
        self.board[self.destination_x][self.destination_y] = "D"
    
    def getCoordinate(self) -> Tuple(int, int):
        return self.x, self.y
    
    def getDestinationCoordinate(self) -> Tuple(int, int):
        return self.destination_x, self.destination_y
    
    def getBoard(self):
        return self.board
    
    def __str__(self) -> str:
        string = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    string += "  " + " |"
                else:
                    string += " " + str(self.board[i][j]) + " |"
            string += "\n" + "-" * 4 * len(self.board) + "\n"
        return string