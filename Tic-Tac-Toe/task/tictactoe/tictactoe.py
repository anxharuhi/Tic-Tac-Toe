from string import Template


class TicTacToe:

    def __init__(self, initial_state):
        initial_state = list(initial_state)
        initial_state.reverse()
        self.state = {}
        self.cell_count = {'X': 0, 'O': 0, '_': 0}
        for row in range(1, 4):
            self.state[row] = {}
            for column in 'ABC':
                self.state[row][column] = initial_state.pop()
                self.cell_count[self.state[row][column]] += 1
        # self.state = {'n' + str(key): value for key, value in enumerate(iterable=list(initial_state), start=1)}

    def print_board(self):
        # pass
        board_template = Template('| $A $B $C |')
        print('---------')
        for row in self.state:
            # pass
            print(board_template.safe_substitute(self.state[row]))
        print('---------')
        print(self.evaluate_wins())

    def evaluate_wins(self):
        x_wins = 0
        o_wins = 0
        nc = Exception('Case not covered')
        # Determine how many lines have a 3 in a row of a character
        for row in self.state:
            if self.state[row]['A'] == self.state[row]['B'] and self.state[row]['A'] == self.state[row]['C']:
                if self.state[row]['A'] == 'X':
                    x_wins += 1
                else:
                    o_wins += 1
        for column in 'ABC':
            if self.state[1][column] == self.state[2][column] and self.state[1][column] == self.state[3][column]:
                if self.state[1][column] == 'X':
                    x_wins += 1
                else:
                    o_wins += 1
        if self.state[1]['A'] == self.state[2]['B'] and self.state[1]['A'] == self.state[3]['C']:
            if self.state[1]['A'] == 'X':
                x_wins += 1
            else:
                o_wins += 1
        if self.state[1]['C'] == self.state[2]['B'] and self.state[1]['A'] == self.state[3]['A']:
            if self.state[3]['A'] == 'X':
                x_wins += 1
            else:
                o_wins += 1
        # A game is in an impossible state if a player has more than 1 extra move
        # or if the board has multiple 3 in a rows.
        if abs(self.cell_count['X'] - self.cell_count['O']) > 1:
            return 'Impossible'
        if x_wins + o_wins > 1:
            return 'Impossible'
        # If we are not in an impossible state, return the winner, if any
        if x_wins > o_wins:
            return 'X wins'
        elif o_wins > x_wins:
            return 'O wins'
        # And finally check if the game has not finished or if it is a draw based on empty spaced
        if self.cell_count['_'] > 0:
            return 'Game not finished'
        elif self.cell_count['_'] == 0:
            return 'Draw'
        raise nc


if __name__ == '__main__':
    board = TicTacToe(input())
    board.print_board()