from warehouse.stack import Stack
from warehouse.exceptions import StackEmptyError

class EntryStack(Stack):
    def __init__(self, x, y, depth):
        super().__init__(x, y, depth)

    # Treat as queue
    def retrieve_bin(self):
        if self.is_empty():
            raise StackEmptyError(f"Cannot pop bin; stack at ({self.x}, {self.y}) is empty")
        top_bin = self.stack.popleft()
        return top_bin