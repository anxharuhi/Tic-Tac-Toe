class TicTacToe:

    board_states = {'xwin': 'X wins', 'owin': 'O wins', 'draw': 'Draw',
                    'impossible': 'Impossible', 'notfinished': 'Game not finished'}

    def __init__(self, initial_state):
        initial_state = list(initial_state)
        self.state = []
        self.cell_count = {'X': 0, 'O': 0, '_': 0}
        self.player = 'X'
        for row in range(0, 3):
            self.state.append([])
            for column in range(0,3):
                self.state[row].append(initial_state.pop())
                self.cell_count[self.state[row][column]] += 1
            self.state[row].reverse()
        self.state.reverse()

    def evaluate_wins(self):
        x_wins = 0
        o_wins = 0
        nc = Exception('Case not covered')
        # Determine how many lines have a 3 in a row of a character
        for row in self.state:
            if row[0] == row[1] and row[1] == row[2]:
                if row[0] == 'X':
                    x_wins += 1
                elif row[0] == 'O':
                    o_wins += 1
        for column in range(len(self.state[0])):
            if self.state[0][column] == self.state[1][column] and self.state[1][column] == self.state[2][column]:
                if self.state[1][column] == 'X':
                    x_wins += 1
                elif self.state[1][column] == 'O':
                    o_wins += 1
        if self.state[0][0] == self.state[1][1] and self.state[1][1] == self.state[2][2]:
            if self.state[1][1] == 'X':
                x_wins += 1
            elif self.state[1][1] == 'O':
                o_wins += 1
        if self.state[0][2] == self.state[1][1] and self.state[1][1] == self.state[2][0]:
            if self.state[1][1] == 'X':
                x_wins += 1
            elif self.state[1][1] == 'O':
                o_wins += 1
        # A game is in an impossible state if a player has more than 1 extra move
        # or if the board has multiple 3 in a rows.
        if abs(self.cell_count['X'] - self.cell_count['O']) > 1:
            return self.board_states['impossible']
        if x_wins + o_wins > 1:
            return self.board_states['impossible']
        # If we are not in an impossible state, return the winner, if any
        if x_wins > o_wins:
            return self.board_states['xwin']
        elif o_wins > x_wins:
            return self.board_states['owin']
        # And finally check if the game has not finished or if it is a draw based on empty spaced
        if self.cell_count['_'] > 0:
            return self.board_states['notfinished']
        elif self.cell_count['_'] == 0:
            return self.board_states['draw']
        raise nc

    def move(self, square):
        try:
            column, row = map(int, square.split(' '))
            assert (1 <= row <= 3 and 1 <= column <= 3)
        except ValueError:
            return [False, 'You should enter numbers!']
        except AssertionError:
            return [False, 'Coordinates should be from 1 to 3!']
        row -= 1
        column -= 1
        row = 2 - row # Account for the weird input requirements for the exercise
        if self.state[row][column] != '_':
            return[False, 'This cell is occupied! Choose another one!']
        else:
            self.state[row][column] = self.player
            self.cell_count[self.player] += 1
            self.cell_count['_'] -= 1
            return [True, '']

    def play(self):
        win = self.board_states['notfinished']
        players = {'X': 'O', 'O': 'X'}
        while win == self.board_states['notfinished']:
            print(self)
            moved = False
            while not moved:
                moved, msg = board.move(input('Enter the coordinates: '))
                if msg != '':
                    print(msg)
            self.player = players[self.player]
            win = self.evaluate_wins()
        print(self)
        print(win)

    def __str__(self):
        board_str = '---------\n'
        for row in self.state:
            board_str += (f'| {row[0]} {row[1]} {row[2]} |\n')
        board_str += ('---------')
        return board_str

    def __repr__(self):
        board_repr = ''
        for row in self.state:
            board_repr += ''.join(row)
        return board_repr

if __name__ == '__main__':
    # board = TicTacToe(input())
    board = TicTacToe('_________')
    board.play()

