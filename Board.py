class Board:
    def __init__(self) -> None:
        self.board = []
        for i in range(20):
            myList = []
            for j in range(20):
                myList.append(0)
            self.board.append(myList)
    
    def __str__(self) -> str:
        return "123456789"