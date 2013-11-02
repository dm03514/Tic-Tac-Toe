

class Player(object):

    def __init__(self, symbol, name, is_human=True):
        self.symbol = symbol 
        self.name = name
        self.is_human = is_human


class Board(object):
    NUM_SPACES = 9
    WINNING_POSITIONS = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # cols
        (0, 4, 8), (2, 4, 6) # diagonals
    )
    
    def __init__(self):
        self.spaces = list(range(self.NUM_SPACES))

    def get_legal_moves(self):
        """
        Generates a collection of all legal moves on this board.
        @return tuple of moves
        """
        pass

    def has_win(self):
        """
        Checks if the board has any wins on it.
        @return tuple (winning_positions_tuple, winning_player)
        """
        pass

    def is_space_open(self, space_num):
        """
        Checks if a given space is open or not
        @return boolean
        """
        pass

    def mark_space(self, space_num, player):
        """
        Marks a space, on the board for the given player.
        @param player object Player instance
        """
        pass

    def __str__(self):
        """
        Prints board as a grid.
        """
        return """
        |{}|
        |{}|
        |{}|
        """.format(
            '|'.join(x.symbol if isinstance(x, Player) else str(x)
                        for x in self.spaces[:3]),
            '|'.join(x.symbol if isinstance(x, Player) else str(x)
                        for x in self.spaces[3:6]),
            '|'.join(x.symbol if isinstance(x, Player) else str(x)
                        for x in self.spaces[6:9]),
        )


def main():
    board = Board()
    player_one = Player('H', 'human')
    player_two = Player('C', 'computer', is_human=False)

    # determine who goes first

    # game loop
    while True:
        pass

if __name__ == '__main__':
    main()
