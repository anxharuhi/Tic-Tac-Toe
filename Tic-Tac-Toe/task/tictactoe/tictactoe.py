class TicTacToe:

    def __init__(self, initial_state):
        initial_state = list(initial_state)
        self.state = []
        self.cell_count = {'X': 0, 'O': 0, '_': 0}
        for row in range(0, 3):
            self.state.append([])
            for column in range(0,3):
                self.state[row].append(initial_state.pop())
                self.cell_count[self.state[row][column]] += 1
            self.state[row].reverse()
        self.state.reverse()
        # self.state = {'n' + str(key): value for key, value in enumerate(iterable=list(initial_state), start=1)}

    def print_board(self):
        print('---------')
        for row in self.state:
            print(f'| {row[0]} {row[1]} {row[2]} |')
        print('---------')


    def evaluate_wins(self):
        x_wins = 0
        o_wins = 0
        nc = Exception('Case not covered')
        # Determine how many lines have a 3 in a row of a character
        for row in self.state:
            if row[0] == row[1] and row[1] == row[2]:
                if row[0] == 'X':
                    x_wins += 1
                else:
                    o_wins += 1
        for column in range(len(self.state[0])):
            if self.state[0][column] == self.state[1][column] and self.state[1][column] == self.state[2][column]:
                if self.state[1][column] == 'X':
                    x_wins += 1
                else:
                    o_wins += 1
        if self.state[0][0] == self.state[1][1] and self.state[1][1] == self.state[2][2]:
            if self.state[1][1] == 'X':
                x_wins += 1
            else:
                o_wins += 1
        if self.state[0][2] == self.state[1][1] and self.state[1][1] == self.state[2][0]:
            if self.state[1][1] == 'X':
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
        # raise nc

    def move(self, square):
        try:
            row, column = map(int, square.split(' '))
            assert (1 <= row <= 3 and 1 <= column <= 3)
        except ValueError:
            return [False, 'You should enter numbers!']
        except AssertionError:
            return [False, 'Coordinates should be from 1 to 3!']
        row -= 1
        column -= 1
        print('Current row: ' + str(row) + ' Current column: ' + str(column))
        row = 2 - row # Account for the weird input requirements for the exercise
        print('Current row after math: ' + str(row))
        print(f'{self.state[0]}\n{self.state[1]}\n{self.state[2]}')
        if self.state[row][column] != '_':
            return[False, 'This cell is occupied! Choose another one!']
        else:
            self.state[row][column] = 'X'
            self.cell_count['X'] += 1
            return [True, '']


if __name__ == '__main__':
    # board = TicTacToe(input())
    board = TicTacToe('XXXOO__O_')
    print(board.state)
    board.print_board()
    moved = False
    while not moved:
        moved, msg = board.move(input('Enter the coordinates: '))
        if msg != '':
            print(msg)
    board.print_board()