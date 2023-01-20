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
#S
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
                print('Current slot is occupied')
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
                print('Current slot is occuppied')
            else:
                print('Success')
                run = False
                board[int(inp)-1] = 'O'
        else:
            print('Slot is not within 1-9')

def findEmptySpot(board):
    emptySpots = []
    for x in range(9):
        if(board[x] == '-'):
            emptySpots.append(x)
    return emptySpots    

def calcScore():
    if(win(board) == 3): 
        return -5
    elif(win(board) == 2):
        return 5
    elif(win(board) == 4):
        return 0
    else:
        return -1

def minimax(board, player): #    C,[i]#if 0emptySpotIndexes[i]indexOfBoardmoves.append( emptySpotIndexes[i]) board[]=ForMovesForMoves ndexndexndexfspoinputO()ts2scor10moves;else: {score: -5} checkAvailability()availreturnreturn -1 -1ning
    #if(calcScore() != -1):
        
    emptySpotIndexes = findEmptySpot(board)
    score = []
    moves = []
    for i in emptySpotIndexes.length:
        
        if(player == aiPlayer):
            board[emptySpotIndexes[i]] = 'O'
            score.append(calcScore())
            minimax(board, player)
    return moves[]    
    
#def max(board) #avail


#8 ways to win
def win(board):
    returnValue = 1
    if((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
        returnValue = 2
    elif((board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X')):
        returnValue = 3
    elif(findEmptySpot(board).length == 0):
        returnValue = 4     
    return returnValue    
        
def main():
    clearBoard(board)
    printBoard(board)
    run = True
    while(run):
        inputX()
        printBoard(board)
        if(win() == 3 or win() == 4):
            break
        inputO()
        printBoard(board)
        if(win() == 2 or win() == 4):
            break
        
    if(win() == 2):
        print('O wins')
    elif(win() == 3):
        print('X wins')    
    elif(win() == 4):
        print('Its a draw!')
                
if __name__ == "__main__":
    main()
