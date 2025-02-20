import unittest
from warehouse.grid import Grid
from warehouse.bin_stack import BinStack
from warehouse.entry_stack import EntryStack
from warehouse.exit_stack import ExitStack

class TestGrid(unittest.TestCase):
    
    def setUp(self):
        """Set up a test grid before each test."""
        Grid._instance =None
        self.grid = Grid()
        self.x_size = 3
        self.y_size = 3
        self.depth = 5
        self.entry_nodes = [(0, 0), (1, 1)]
        self.exit_nodes = [(2, 2)]
        self.grid = Grid()
        self.grid.init_grid(self.x_size, self.y_size, self.depth, self.entry_nodes, self.exit_nodes)

    def test_grid_initialization(self):
        """Test if grid initializes with the correct dimensions."""
        expected_nodes = self.x_size * self.y_size
        self.assertEqual(len(self.grid.nodes), expected_nodes)

    def test_entry_and_exit_nodes(self):
        """Test if entry and exit nodes are correctly placed."""
        for x, y in self.entry_nodes:
            self.assertIsInstance(self.grid.get_stack(x, y), EntryStack)

        for x, y in self.exit_nodes:
            self.assertIsInstance(self.grid.get_stack(x, y), ExitStack)

    def test_bin_stack_nodes(self):
        """Test if non-entry/exit nodes are default bin stacks."""
        for x in range(self.x_size):
            for y in range(self.y_size):
                if (x, y) not in self.entry_nodes and (x, y) not in self.exit_nodes:
                    self.assertIsInstance(self.grid.get_stack(x, y), BinStack)

    def test_out_of_bounds(self):
        """Test that retrieving an out-of-bounds node returns None."""
        self.assertIsNone(self.grid.get_stack(-1, -1))
        self.assertIsNone(self.grid.get_stack(self.x_size, self.y_size))

    def test_node_connections(self):
        """Test if nodes connect correctly in the adjacency list."""
        self.grid.connect_nodes((0, 0), (0, 1))
        self.assertIn(((0, 1), 1), self.grid.adjacency_list[(0, 0)])  # Connected with weight 1
        self.assertIn(((0, 0), 1), self.grid.adjacency_list[(0, 1)])

if __name__ == '__main__':
    unittest.main()
