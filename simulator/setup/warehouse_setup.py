import random
from warehouse.grid import Grid
from warehouse.bin import Bin
from items.items import *

class WarehouseSetup:
    def __init__(self, x_size, y_size, depth, entry_nodes, exit_nodes):
        """Initializes the grid and prepares the warehouse setup."""
        self.grid = Grid()
        self.grid.init_grid(x_size, y_size, depth, entry_nodes, exit_nodes)
        self.item_types = [Soap(), Toothbrush(), Basketball(), Baseball(), Laptop(), GPU()]
    
    def create_random_item(self):
        """Creates a random item from available item types."""
        item_type = random.choice(self.item_types)
        return item_type.create_item()

    def populate_bin(self, num_items):
        """Creates a bin and fills it with `num_items` random items."""
        bin_obj = Bin()
        for _ in range(num_items):
            bin_obj.add_item(self.create_random_item())
        return bin_obj

    def populate_grid_with_bins(self, num_bins, items_per_bin):
        """Places `num_bins` bins into randomly selected grid locations."""
        for _ in range(num_bins):
            x, y = random.randint(0, 2), random.randint(0, 2)  # Adjust range for your grid
            bin_stack = self.grid.get_stack(x, y)
            if bin_stack:
                bin_stack.add_bin(self.populate_bin(items_per_bin))
    
    def print_setup(self):
        """Prints the entire warehouse grid with stacks and bins."""
        self.grid.print_grid()
