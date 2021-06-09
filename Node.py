from typing import Tuple
from __future__ import annotations

class Node:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.next = None
        self.prev = None
        
    def getCoordinate(self) -> Tuple[int, int]:
        return self.x, self.y

    def setNext(self, next: Node) -> None:
        self.next = next
    
    def getNext(self) -> Node:
        return self.next
    
    def setPrev(self, prev: Node) -> None:
        self.prev = prev
    
    def getPrev(self) -> Node:
        return self.prev
        