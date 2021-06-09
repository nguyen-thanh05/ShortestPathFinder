from typing import Tuple


class Board:
    def __init__(self) -> None:
        self.SIZE = 5
        self.board = [[0] * self.SIZE for i in range(self.SIZE)]
        self.destination_x = self.SIZE - 1
        self.destination_y = self.SIZE - 1
        self.x = 0
        self.y = 0
        self.board[self.x][self.y] = "X"
        self.board[self.destination_x][self.destination_y] = "D"
        
        for i in range(self.SIZE - 1):
            self.board[i][2] = 1
    
    def getCoordinate(self) -> Tuple[int, int]:
        return self.x, self.y
    
    def getDestinationCoordinate(self) -> Tuple[int, int]:
        return self.destination_x, self.destination_y
    
    def getManhattanDistance(self) -> int:
        x, y = self.getCoordinate()
        destination_x, destination_y = self.getDestinationCoordinate()
        
        return (destination_x - x) + (destination_y - y)
        
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