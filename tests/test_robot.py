import unittest
from warehouse.exceptions import StackFullError, StackEmptyError
from warehouse.grid import Grid
from robots.robot import Robot
from warehouse.bin_stack import BinStack
from unittest.mock import MagicMock

class TestRobot(unittest.TestCase):
    def setUp(self):
        """Set up a test grid and robot before each test."""
        Grid._instance = None  # Reset singleton instance
        self.grid = Grid()
        self.grid.init_grid(3, 3, 5, entry_nodes=[], exit_nodes=[])
        self.robot = Robot(id="robot_1", x=1, y=1, grid=self.grid)

    def test_move_valid(self):
        """Test that the robot moves to a valid position."""
        self.robot.move(2, 2)
        self.assertEqual(self.robot.x, 2)
        self.assertEqual(self.robot.y, 2)

    def test_move_invalid(self):
        """Test that the robot does not move to an invalid position."""
        self.robot.move(5, 5)  # Outside grid bounds
        self.assertEqual(self.robot.x, 1)
        self.assertEqual(self.robot.y, 1)

    def test_pickup_bin_success(self):
        """Test that the robot successfully picks up a bin from a non-empty stack."""
        stack = self.grid.get_stack(1, 1)
        mock_bin = MagicMock()
        mock_bin.id = "bin_1"
        stack.add_bin(mock_bin)

        picked_bin = self.robot.pickup_bin()
        self.assertEqual(self.robot.bin, mock_bin)
        self.assertEqual(picked_bin, mock_bin)

    def test_pickup_bin_empty_stack(self):
        """Test that the robot cannot pick up a bin from an empty stack."""
        with self.assertRaises(StackEmptyError):
            self.robot.pickup_bin()

    def test_pickup_bin_already_holding(self):
        """Test that the robot cannot pick up a bin if already carrying one."""
        self.robot.bin = MagicMock()
        self.robot.pickup_bin()
        self.assertIsNotNone(self.robot.bin)

    def test_drop_bin_success(self):
        """Test that the robot successfully drops a bin onto a stack."""
        stack = self.grid.get_stack(1, 1)
        stack.add_bin = MagicMock()
        mock_bin = MagicMock()
        mock_bin.id = "bin_1"
        self.robot.bin = mock_bin

        self.robot.drop_bin()
        stack.add_bin.assert_called_with(mock_bin)
        self.assertIsNone(self.robot.bin)

    def test_drop_bin_stack_full(self):
        """Test that the robot cannot drop a bin onto a full stack."""
        stack = self.grid.get_stack(1, 1)
        stack.is_full = MagicMock(return_value=True)

        self.robot.bin = MagicMock()
        with self.assertRaises(StackFullError):
            self.robot.drop_bin()

    def test_drop_bin_no_bin(self):
        """Test that the robot cannot drop a bin if it is not carrying one."""
        self.robot.bin = None
        self.robot.drop_bin()
        self.assertIsNone(self.robot.bin)

if __name__ == '__main__':
    unittest.main()
