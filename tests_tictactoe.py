from random import choice
import unittest

from tictactoe import Board, Player


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

    def test_board_get_win_detection(self):
        """
        Tests that a board can detect when a win is present.
        """
        board = Board()
        self.assertFalse(board.get_win())

        # create a player and mark a winning move
        player = Player(board, 'H', 'human')
        winning_move = choice(board.WINNING_POSITIONS)
        for space in winning_move:
            board.spaces[space] = player
        self.assertTrue(board.get_win())
        

