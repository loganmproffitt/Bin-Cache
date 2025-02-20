from collections import defaultdict
from warehouse.bin_stack import BinStack
from warehouse.entry_stack import EntryStack
from warehouse.exit_stack import ExitStack

'''
    - Graph representation of xy plane. Can initialize to uniform shape and add non-uniform nodes.
    - Each node is assigned a stack (a column), which can represent an entry port, exit port, or normal bin stack.
    - Edges represent the paths between each node, allowing for navigation and assigned travel durations
'''

class Grid:
    _instance = None  # Singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Grid, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.nodes = {}
            self.adjacency_list = defaultdict(list)
            self._initialized = True

    @classmethod
    def reset(cls):
        """Allows tests to reset the singleton instance."""
        cls._instance = None

    def init_grid(self, x_size, y_size, depth, entry_nodes, exit_nodes):
        for x in range(x_size):
            for y in range(y_size):
                stack_type = BinStack
                if (x, y) in entry_nodes:
                    stack_type = EntryStack
                elif (x, y) in exit_nodes:
                    stack_type = ExitStack
                self.add_node(x, y, depth, stack_type)

    def add_node(self, x, y, depth, stack_type):
        #print(f"depth before: {depth}")
        if (x, y) not in self.nodes:
            self.nodes[(x, y)] = stack_type(x, y, depth)
            #print(f"DEBUG: Node ({x}, {y}) initialized with depth={depth}")
        

    def connect_nodes(self, a, b, weight=1):
        if a in self.nodes and b in self.nodes:
            self.adjacency_list[a].append((b, weight))
            self.adjacency_list[b].append((a, weight))

    def get_stack(self, x, y):
        if (x, y) in self.nodes:
            return self.nodes[(x, y)]
        else:
            print(f"Node at ({x, y}) not found.")
            return None

    def print_grid(self):
        for (x, y), node in sorted(self.nodes.items()):
            print(f"({x}, {y}): {list(node.stack)}, depths {node.depth}")