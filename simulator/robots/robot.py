from warehouse.exceptions import StackFullError, StackEmptyError
class Robot:
    def __init__(self, id, x, y, grid):
        self.x = x
        self.y = y
        self.id = id
        self.grid = grid
        self.bin = None

    def move(self, new_x, new_y):
        if (new_x, new_y) in self.grid.nodes:
            self.x = new_x
            self.y = new_y
            print(f"Robot {self.id[:8]} moved to ({new_x}, {new_y})")
        else:
            print(f"Invalid move for Robot {self.id[:8]}")

    def pickup_bin(self):
        if self.bin is not None:
            print(f"Robot {self.id[:8]} is already carrying a bin")
            return None
        
        stack = self.grid.get_stack(self.x, self.y)
        print(f"Robot perspective of stack: {stack.stack}")

        if stack.is_empty():
            raise StackEmptyError(f"Stack at ({self.x}, {self.y}) is empty, robot cannot pick up a bin.")
                                 
        if stack:
            self.bin = stack.retrieve_bin()
            print(f"Robot {self.id[:8]} picked up bin {self.bin.id[:8]}")   
            return self.bin  
        print(f"No bins available at ({self.x}, {self.y})")
        return None
    
    def drop_bin(self):
        if self.bin is None:
            print(f"Can't drop; robot {self.id[:8]} is not carrying a bin")
            return

        stack = self.grid.get_stack(self.x, self.y)
        print(f"Stack is full: {stack.is_full()}, at {stack.get_bin_count()} with capacity {stack.depth}")
        if stack.is_full():
            raise StackFullError(f"Stack at ({self.x}, {self.y}) is full, robot cannot drop the bin.") 
    
        if stack is not None:
            stack.add_bin(self.bin)
            print(f"Robot {self.id[:8]} placed bin {self.bin.id[:8]} at ({self.x}, {self.y})")     
            self.bin = None
            return
        else:
            print(f"Can't drop bin at ({self.x}, {self.y}); stack is full")
            return
