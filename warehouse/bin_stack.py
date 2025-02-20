from warehouse.stack import Stack
from warehouse.exceptions import *

class BinStack(Stack):
    def __init__(self, x, y, depth):
        super().__init__(x, y, depth)

    def retrieve_bin(self):
        if self.stack:
            top_bin = self.stack.pop()
            return top_bin
        return None
    