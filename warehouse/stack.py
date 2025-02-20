from warehouse.exceptions import *
from collections import deque

class Stack:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth
        self.stack = deque()

    def add_bin(self, bin):
        if self.is_full():
            raise StackFullError(f"Cannot add bin; stack at ({self.x}, {self.y}) is full")
        self.stack.append(bin)

    def is_full(self):
        return len(self.stack) >= self.depth
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def get_bin_count(self):
        return len(self.stack)