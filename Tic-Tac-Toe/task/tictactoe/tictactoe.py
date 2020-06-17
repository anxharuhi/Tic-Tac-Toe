from string import Template

class TicTacToe:

    def __init__(self, initial_state):
        initial_state = list(initial_state)
        initial_state.reverse()
        self.state = {}
        for row in range(1, 4):
            self.state[row] = {}
            for column in 'ABC':
                self.state[row][column] = initial_state.pop()
        # self.state = {'n' + str(key): value for key, value in enumerate(iterable=list(initial_state), start=1)}

    def print_board(self):
        board_template = Template('| $A $B $C |')
        print('---------')
        for row in self.state:
            print(board_template.safe_substitute(self.state[row]))
        print('---------\n')


board = TicTacToe(input())
# board = TicTacToe('XXXOO__O_')
board.print_board()
