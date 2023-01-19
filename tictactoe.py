board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

def clearBoard(board):
    board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2]) 
    print(board[3] + ' | ' + board[4] + ' | ' + board[5]) 
    print(board[6] + ' | ' + board[7] + ' | ' + board[8]) 
    print()

def inputX():
    run = True
    while(run):
        inp = input('Enter slot from 1-9 to input X:')
        if(not inp.isdigit()):
            print('Enter a digit from 1-9 only:')
        elif(1 <= int(inp) <= 9):
            if(board[int(inp)-1] == 'X' or board[int(inp)-1] == 'O'):
                print('Slot is occupied')
            else:
                print('Success')
                run = False
                board[int(inp)-1] = 'X'
        else:
            print('Slot is not within 1-9')

def inputO():
    run = True
    while(run):
        inp = input('Enter slot from 1-9 to input O:')
        if(not inp.isdigit()):
            print('Enter a digit from 1-9 only:')
        elif(1 <= int(inp) <= 9):
            if(board[int(inp)-1] == 'X' or board[int(inp)-1] == 'O'):
                print('Slot is occupied')
            else:
                print('Success')
                run = False
                board[int(inp)-1] = 'O'
        else:
            print('Slot is not within 1-9')

#8 ways to win
def win():
    if((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
        print('O wins')
    elif((board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X')):
        print('X wins') 
        
def main():
    clearBoard(board)
    printBoard(board)
    inputX()
    printBoard(board)
    inputO()
    printBoard(board)
    inputX()
    printBoard(board)

if __name__ == "__main__":
    main()
