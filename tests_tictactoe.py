import unittest

from tictactoe import Board


class TestTicTacToe(unittest.TestCase):

    def test_board_print_as_grid(self):
        """
        Tests that board is printed as a grid.
        """
        board = Board()
        board_grid_str = """
        |0|1|2|
        |3|4|5|
        |6|7|8|
        """
        self.assertEqual(board_grid_str, board.__str__())
