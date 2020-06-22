from tictactoe import TicTacToe
from colorama import Fore
from dataclasses import dataclass


@dataclass
class Movement:
    initial: str
    input: dict
    output: str


def test_win_conditions():
    test_win_cases = {'XXXOO__O_': 'X wins', 'XOXOXOXXO': 'X wins', 'XOOOXOXXO': 'O wins',
                      'XOXOOXXXO': 'Draw', 'XO_OOX_X_': 'Game not finished', 'XO_XO_XOX': 'Impossible',
                      '_O_X__X_X': 'Impossible', '_OOOO_X_X': 'Impossible'}
    case_number = 1

    for case in test_win_cases:
        board = TicTacToe(case)
        evaluate_result = board.evaluate_wins()
        test_pass = Fore.RED + 'FAIL' + Fore.RESET
        if evaluate_result == test_win_cases[case]:
            test_pass = Fore.GREEN + 'PASS' + Fore.RESET
        print(f'Case {case_number}\n'
              f'----------------\n'
              f'{test_pass}\n'
              f' - Expected result: {test_win_cases[case]}\n'
              f' - Actual result: {evaluate_result}\n', )
        case_number += 1


def test_board_movement():
    error_messages = {'occupied': 'This cell is occupied! Choose another one!',
                      'numbers': 'You should enter numbers!',
                      'coordinates': 'Coordinates should be from 1 to 3!'}
    test_movements_cases = [Movement('X_X_O____', {'1 1': ''}, 'X_X_O_X__'),  # 1
                            Movement('_XXOO_OX_', {'1 3': ''}, 'XXXOO_OX_'),  # 2
                            Movement('_XXOO_OX_', {'3 1': ''}, '_XXOO_OXX'),  # 3
                            Movement('_XXOO_OX_', {'3 2': ''}, '_XXOOXOX_'),  # 4
                            Movement('_XXOO_OX_', {'1 1': error_messages['occupied'], '1 3': ''}, 'XXXOO_OX_'),  # 5
                            Movement('_XXOO_OX_',
                                     {'one': error_messages['numbers'], 'one three': error_messages['numbers'],
                                      '1 3': ''}, 'XXXOO_OX_'),  # 6
                            Movement('_XXOO_OX_',
                                     {'4 1': error_messages['coordinates'], '1 4': error_messages['coordinates'],
                                      '1 3': ''}, 'XXXOO_OX_')]  # 7
    case_number = 1

    for case in test_movements_cases:
        test_pass = Fore.RED + 'FAIL' + Fore.RESET
        try:
            board = TicTacToe(case.initial)
            for movement in case.input:
                moved, msg = board.move(movement)
                assert msg == case.input[movement]
            assert case.output == repr(board)
            test_pass = Fore.GREEN + 'PASS' + Fore.RESET
        except AssertionError:
            # noinspection PyUnboundLocalVariable
            print(f'Case {case_number}\n'
                  f'----------------\n'
                  f'{test_pass}\n'
                  f' - Input: {movement}\n'
                  f' - Expected message: {repr(case.input[movement])}\n'
                  f' - Actual message: {repr(msg)}\n'
                  f' - Expected board: {case.output}\n'
                  f' - Actual board: {repr(board)}\n')
        else:
            test_pass = Fore.GREEN + 'PASS' + Fore.RESET
            print(f'Case {case_number}\n'
                  f'----------------\n'
                  f'{test_pass}\n'
                  f' - Expected board: {case.output}\n'
                  f' - Actual board: {repr(board)}\n')
        finally:
            case_number += 1


if __name__ == '__main__':
    print('-----------------------')
    print('| ' + Fore.BLUE + 'Win Condition tests' + Fore.RESET + ' |')
    print('-----------------------\n')
    test_win_conditions()
    print('\n')
    print('-------------------------')
    print('| ' + Fore.BLUE + 'Player movement tests' + Fore.RESET + ' |')
    print('-------------------------\n')
    test_board_movement()

# board = TicTacToe('XOXOXOXXO_')
# board.print_board()
