def my_winning_move(board):
    copy_board = board.copy()
    for i in range(1, 10):
        if copy_board[str(i)] == '   ':
            copy_board[str(i)] = ' o '
            if winning(copy_board, 'o'):
                return i
            else:
                copy_board[str(i)] = '   '
    return None


def his_winning_move(board):
    copy_board = board.copy()
    for i in range(1, 10):
        if copy_board[str(i)] == '   ':
            copy_board[str(i)] = ' x '
            if winning(copy_board, 'x'):
                return i
            else:
                copy_board[str(i)] = '   '
    return None


def comp_move(turn, board):
    if turn == 0:
        print("Here's my move!\n")
        for i in [9, 3, 1, 7]:
            if board[str(i)] == ' x ':
                board['5'] = ' o '
                print_board(board)
                return

        board['1'] = ' o '
        print_board(board)
        return
    else:
        if board == {'1': ' x ', '2': '   ', '3': '   ', '4': '   ', '5': ' o ', '6': '   ', '7': '   ', '8': '   ', '9': ' x '} or board == {'1': '   ', '2': '   ', '3': ' x ', '4': '   ', '5': ' o ', '6': '   ', '7': ' x ', '8': '   ', '9': '   '}:
            board['2'] = ' o '
            print("Here's my move!\n")
            print_board(board)
            return
        i = my_winning_move(board)
        if i is not None:
            print("Here's my move!\n")
            board[str(i)] = ' o '
            print_board(board)
            return
        i = his_winning_move(board)
        if i is not None:
            print("Here's my move!\n")
            board[str(i)] = ' o '
            print_board(board)
            return
        else:
            for i in [1, 3, 7, 9]:
                if board[str(i)] == '   ':
                    board[str(i)] = ' o '
                    print("Here's my move!\n")
                    print_board(board)
                    return
            for i in [2, 4, 5, 6, 8]:
                if board[str(i)] == '   ':
                    board[str(i)] = ' o '
                    print("Here's my move!\n")
                    print_board(board)
                    return


def select_opponent():
    opponent = input('Select opponent\n1. AI\n2. Player2\nChoose: ')
    if opponent == '1' or opponent == 'AI':
        return 'ai'
    elif opponent == '2' or opponent == 'Player2':
        return 'player'
    else:
        return select_opponent()


def board_full(board):
    for value in board.values():
        if value == '   ':
            return False
    return True


def start_game(opponent):
    board = {'1': '   ', '2': '   ', '3': '   ', '4': '   ', '5': '   ', '6': '   ', '7': '   ', '8': '   ', '9': '   '}
    print('Good Luck!\nThis is the index\n')
    index_board = {'1': ' 1 ', '2': ' 2 ', '3': ' 3 ', '4': ' 4 ', '5': ' 5 ', '6': ' 6 ', '7': ' 7 ', '8': ' 8 ', '9': ' 9 '}
    print_board(index_board)
    print("press 'q' anytime to quit the game")
    if opponent == 'ai':
        turn = 0
        run = True
        while run:
            if not board_full(board):
                run = player_move(board)
                if not run:
                    break
                if winning(board, 'x'):
                    print('You Win!')
                    run = False
                    break
                comp_move(turn, board)
                if winning(board, 'o'):
                    print('You Lose!')
                    run = False
                    break
                turn = turn + 1
            else:
                print("It's a Draw!")
                run = False
    else:
        run = True
        while run:
            if not board_full(board):
                run = player_move(board)
                if not run:
                    break
                if winning(board, 'x'):
                    print('Player 1 Wins!')
                    run = False
                    break
                if not board_full(board):
                    run = player_move(board, 'o')
                    if not run:
                        break
                    if winning(board, 'o'):
                        print('Player 2 Wins!')
                        run = False
                        break
            else:
                print("It's a Draw!")
                run = False


def print_board(board):
    for j in range(1, 4):
        print('           ', end='')
        for x in range(3 * (j - 1) + 1, 3 * j + 1):
            if x % 3 != 0:
                print(board[str(x)], end=' | ')
            else:
                print(board[str(x)], end='\n')
        if j % 3 != 0:
            print('           ----|-----|----')
    print('\n')


def player_move(board, symbol='x'):
    move = input('where do you want to place ' + symbol + ' (choose from 1 to 9): ')
    print('\n')
    if move == 'q':
        return False
    if move in board.keys():
        if board[move] == '   ':
            board[move] = ' ' + symbol + ' '
            print_board(board)
            return True
        else:
            print('that space is already occupied!')
            return player_move(board)
    else:
        print('not a valid input! Select from numbers 1 to 9!')
        return player_move(board)


def ask_continue():
    ask = input('continue playing? (y/n): ')
    if ask == 'y':
        return True
    elif ask == 'n':
        return False
    else:
        return ask_continue()


def winning(board, symbol):
    if (board['1'] == (' ' + symbol + ' ') and board['2'] == (' ' + symbol + ' ') and board['3'] == (' ' + symbol + ' ')) or (
            board['4'] == (' ' + symbol + ' ') and board['5'] == (' ' + symbol + ' ') and board['6'] == (' ' + symbol + ' ')) or (
            board['7'] == (' ' + symbol + ' ') and board['8'] == (' ' + symbol + ' ') and board['9'] == (' ' + symbol + ' ')) or (
            board['1'] == (' ' + symbol + ' ') and board['4'] == (' ' + symbol + ' ') and board['7'] == (' ' + symbol + ' ')) or (
            board['2'] == (' ' + symbol + ' ') and board['5'] == (' ' + symbol + ' ') and board['8'] == (' ' + symbol + ' ')) or (
            board['3'] == (' ' + symbol + ' ') and board['6'] == (' ' + symbol + ' ') and board['9'] == (' ' + symbol + ' ')) or (
            board['1'] == (' ' + symbol + ' ') and board['5'] == (' ' + symbol + ' ') and board['9'] == (' ' + symbol + ' ')) or (
            board['3'] == (' ' + symbol + ' ') and board['5'] == (' ' + symbol + ' ') and board['7'] == (' ' + symbol + ' ')):
        return True


def main():
    print('Hey Player!\nWelcome to Tic Tak Toe!\n')
    opponent = select_opponent()
    print('\nStarting game!\nPlayer1: x\nPayer2: o\n')
    start_game(opponent)


main()








