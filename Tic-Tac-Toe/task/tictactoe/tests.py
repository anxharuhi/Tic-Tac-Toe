from tictactoe import TicTacToe
from colorama import Fore

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
          f' - Actual result: {evaluate_result}\n',)
    case_number += 1
# board = TicTacToe('XOXOXOXXO_')
# board.print_board()