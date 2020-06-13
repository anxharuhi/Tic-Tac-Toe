from string import Template


class TicTacToe:

    def __init__(self, initial_state):
        self.state = {'n' + str(key): value for key, value in enumerate(iterable=list(initial_state), start=1)}
        self.board = Template('---------\n'
                              '| $n1 $n2 $n3 |\n'
                              '| $n4 $n5 $n6 |\n'
                              '| $n7 $n8 $n9 |\n'
                              '---------\n')

    def print_board(self):
        print(self.board.safe_substitute(self.state))


board = TicTacToe(input())
board.print_board()
