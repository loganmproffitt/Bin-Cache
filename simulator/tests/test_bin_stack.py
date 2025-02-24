import unittest
from warehouse.bin_stack import BinStack
from warehouse.bin import Bin
from warehouse.exceptions import *

class TestBinStack(unittest.TestCase):
    
    def setUp(self):
        """Runs before each test to provide a fresh BinStack instance."""
        self.stack = BinStack(0, 0, depth=3)

    def test_stack_initialization(self):
        """Test if stack initializes correctly."""
        self.assertEqual(self.stack.x, 0)
        self.assertEqual(self.stack.y, 0)
        self.assertEqual(self.stack.depth, 3)
        self.assertEqual(len(self.stack.stack), 0)  # Ensure stack is empty

    def test_add_bin(self):
        """Test adding a bin to the stack."""
        bin1 = Bin()
        self.stack.add_bin(bin1)
        
        self.assertEqual(len(self.stack.stack), 1)  # 1 bin in stack
        self.assertFalse(self.stack.is_full())  # Stack should not be full yet

    def test_stack_full(self):
        """Test if stack correctly identifies when it's full."""
        bin1 = Bin()
        bin2 = Bin()
        bin3 = Bin()
        bin4 = Bin()  # This should not fit

        self.stack.add_bin(bin1)
        self.stack.add_bin(bin2)
        self.stack.add_bin(bin3)
        
        self.assertTrue(self.stack.is_full())  # Should be full after 3 bins

        with self.assertRaises(StackFullError):
            self.stack.add_bin(bin4)

    def test_remove_bin(self):
        """Test removing a bin from the stack."""
        bin1 = Bin()
        self.stack.add_bin(bin1)
        removed_bin = self.stack.retrieve_bin()
        
        self.assertEqual(removed_bin, bin1)  # Ensure correct bin is removed
        self.assertEqual(len(self.stack.stack), 0)  # Stack should be empty

    def test_stack_lifo_behavior(self):
        """Test that stack follows LIFO (Last-In, First-Out)."""
        bin1 = Bin()
        bin2 = Bin()
        bin3 = Bin()

        self.stack.add_bin(bin1)
        self.stack.add_bin(bin2)
        self.stack.add_bin(bin3)

        self.assertEqual(self.stack.retrieve_bin(), bin3)  # Last added should be first out
        self.assertEqual(self.stack.retrieve_bin(), bin2)
        self.assertEqual(self.stack.retrieve_bin(), bin1)
        self.assertEqual(len(self.stack.stack), 0)  # Stack should now be empty

if __name__ == '__main__':
    unittest.main()
