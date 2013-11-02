from random import shuffle

class Minimax(object):

    def __init__(self, board):
        self.board = board

    def make_pick(self):
        """
        """
        # return a first empty board space for right now
        for space in self.board.spaces:
            if not isinstance(space, Player):
                return space


class Player(object):

    def __init__(self, board, symbol, name, is_human=True, ai_strat=None):
        self.board = board
        self.symbol = symbol 
        self.name = name
        self.is_human = is_human
        self.ai_strat = ai_strat 

    def _get_player_input(self):
        """
        Gets a players input.
        """
        while True:
            try:
                space_num = int(raw_input('Space Number?'))
            except ValueError:
                print('Invalid Space Number, Please choose again')
            else:
                if self.board.is_valid_space(space_num):
                    return space_num
                print('Invalid Space Number, Please choose again')

    def make_play(self):
        """
        Puts a play on the board.  If player is human player prompt for a 
        play space, else if it is computer player, use an ai_strat to 
        determine the play.
        """
        if self.is_human:
            # prompt for user input
            space_num = self._get_player_input()
        else:
            # computer will only choose a valid space,
            # no need to validate, just mark it
            space_num = self.ai_strat.make_pick()

        self.board.mark_space(space_num, self)


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

    def get_win(self):
        """
        Checks if the board has any wins on it.
        @return tuple (winning_positions_tuple, winning_player)
        """
        # go through each winning positions and check to see if
        # any of the positions have the same player instance
        for position in self.WINNING_POSITIONS:
            if (isinstance(self.spaces[position[0]], Player) and
                self.spaces[position[0]] == self.spaces[position[1]] == self.spaces[position[2]]):

                return (position, self.spaces[position[1]])

        return False

    def is_valid_space(self, space_num):
        """
        Checks if a space is valid.
        Valid spaces must be an index in self.spaces, 
        and the space must be open.
        """
        return (space_num in range(self.NUM_SPACES) and
                self.is_space_open(space_num))

    def is_space_open(self, space_num):
        """
        Checks if a given space is open or not
        @return boolean
        """
        return not isinstance(self.spaces, Player)

    def mark_space(self, space_num, player):
        """
        Marks a space, on the board for the given player.
        @param player object Player instance
        """
        self.spaces[space_num] = player

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
    players = [
        Player(board, 'H', 'human'),
        Player(board, 'C', 'computer', is_human=False, ai_strat=Minimax(board))
    ]

    # randomly determine who goes first
    shuffle(players)

    print(board)

    # game loop
    while True:

        # each player plays until the game has a winner
        for player in players:
            print("{}'s Turn:".format(player.name))
            player.make_play()
            print(board)
            win = board.get_win()
            if win:
                print('{} Won! Game Over'.format(win[1].name))
                return


if __name__ == '__main__':
    main()
