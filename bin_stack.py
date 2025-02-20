from collections import deque
from stack import Stack

class BinStack(Stack):
    def __init__(self, x, y, depth):
        super().__init__(x, y, depth)
        self.stack = deque()