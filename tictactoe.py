def printboard(board):
    print(board['A1'] + ' | ' + board['A2'] + '| ' + board['A3'] )
    print('--+--+--')
    print(board['B1'] + ' | ' + board['B2'] + '| ' + board['B3'] )
    print('--+--+--')
    print(board['C1'] + ' | ' + board['C2'] + '| ' + board['C3'] )



def main():
    board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
             'B1': ' ', 'B2': ' ', 'B3': ' ',
             'C1': ' ', 'C2': ' ', 'C3': ' ', }
    turn = 'x'
    for i in range(9):
        printboard(board)
        print('turn for X')
        move = input()
        board[move] = turn
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

if __name__ == '__main__':
    main()
