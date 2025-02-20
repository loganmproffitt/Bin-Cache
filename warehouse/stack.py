from warehouse.exceptions import *

class Stack:
    def __init__(self, x, y, depth=6):
        self.x = x
        self.y = y
        self.depth = depth
        self.bin_count = 0

    def add_bin(self, bin):
        if self.is_full():
            raise StackFullError(f"Cannot add bin; stack at ({self.x}, {self.y}) is full")
        self.stack.append(bin)

    def is_full(self):
        return len(self.stack) >= self.depth
    
    def is_empty(self):
        return len(self.stack) == 0