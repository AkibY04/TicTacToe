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
            print('Enter a digit from 1-9 only')
        elif(1 <= int(inp) <= 9):
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
            print('Enter a digit from 1-9 only')
        elif(1 <= int(inp) <= 9):
            print('Success')
            run = False
            board[int(inp)-1] = 'O'
        else:
            print('Slot is not within 1-9')

#def win():
    

printBoard(board)
inputX()
printBoard(board)
inputO()
printBoard(board)