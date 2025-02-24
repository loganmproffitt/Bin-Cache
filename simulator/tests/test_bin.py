import unittest
import uuid
from warehouse.bin import Bin
from warehouse.exceptions import BinFullError, ItemNotFoundError

class FakeItem:
    """A simple mock item class for testing purposes."""
    def __init__(self, item_type):
        self.id = str(uuid.uuid4())
        self.item_type = item_type

class TestBin(unittest.TestCase):
    
    def setUp(self):
        """Runs before each test, initializes a bin."""
        self.bin = Bin(max_items=3)  # Set a small capacity for testing
        self.item1 = FakeItem("Soap")
        self.item2 = FakeItem("Laptop")
        self.item3 = FakeItem("Book")
    
    def test_add_item(self):
        """Test adding items to a bin."""
        self.bin.add_item(self.item1)
        self.assertEqual(self.bin.get_item_count(), 1)
    
    def test_add_item_bin_full(self):
        """Test adding an item to a full bin raises an exception."""
        self.bin.add_item(self.item1)
        self.bin.add_item(self.item2)
        self.bin.add_item(self.item3)

        with self.assertRaises(BinFullError):
            self.bin.add_item(FakeItem("Extra Item"))  # Bin is already full

    def test_remove_existing_item(self):
        """Test removing an existing item."""
        self.bin.add_item(self.item1)
        removed_item = self.bin.remove_item(self.item1.id)
        self.assertEqual(removed_item, self.item1)
        self.assertEqual(self.bin.get_item_count(), 0)  # Bin should now be empty

    def test_remove_non_existing_item(self):
        """Test removing an item that doesn't exist raises an exception."""
        self.bin.add_item(self.item1)

        with self.assertRaises(ItemNotFoundError):
            self.bin.remove_item("nonexistent_id")  # Fake ID

    def test_is_full(self):
        """Test the is_full() method."""
        self.bin.add_item(self.item1)
        self.bin.add_item(self.item2)
        self.bin.add_item(self.item3)
        self.assertTrue(self.bin.is_full())

    def test_is_empty(self):
        """Test the is_empty() method."""
        self.assertTrue(self.bin.is_empty())
        self.bin.add_item(self.item1)
        self.assertFalse(self.bin.is_empty())

if __name__ == '__main__':
    unittest.main()
