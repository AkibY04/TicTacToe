board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

player = "O"
ai = "X"
ai2 = "X"
player2 = "O" #= ""A###OXvarvar  

def clearBoard(board):
    board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]
#fS 
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
                print('\nCurrent slot is occupied\n')
            else:
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
                print('\nCurrent slot is occuppied\n')
            else:
                run = False
                board[int(inp)-1] = 'O'
        else:
            print('Slot is not within 1-9')

def inputAI():
    if(ai == "X"):
        bestScore =-10000 #100000  
        bestMoveIndex = -10
        for x in range(9):
            if(board[x] == '-'):
                board[x] = ai
                score = minimax(board, False)
                
                board[x] = '-'
                if(score > bestScore):
                    bestScore = score
                    bestMoveIndex = x # I - 1 - 1 - 1 - 1 O 
        board[bestMoveIndex] = ai
        ##print(bestMoveIndex)
    elif(ai == "O"):
        print(2)
        bestScore = 10000
        bestMoveIndex = 0
        for x in range(9):
            if(board[x] == '-'):
                board[x] = ai
                score = minimax(board, True)
                board[x] = '-'
                if(score < bestScore):
                    bestScore = score
                    bestMoveIndex = x
        board[bestMoveIndex] = ai
        ##print(bestMoveIndex)
     ##[]scoreE  aiARD=sbcore print(score)0score ai =  player 0score = 0score = 0 in findEmptySpot(board)\xreturn bestMoveIndexbestMove - 1  - 1 - 1 - 1 - 1- 1 - 1 - 1Indexdmaximize()score == 0 in findEmptySpot(board) in findEmptySpot(board)
    
def reverseMaximize():
    
    bestScore = -10000
    bestMoveIndex = 0
    for x in range(9):
        if(board[x] == '-'):
                board[x] = player
                score = minimax(board, False)
                board[x] = '-'
                #printBoard(board)
                if(score > bestScore):
                    bestScore = score
                    bestMoveIndex = x
    return bestScore

def reverseMinimize():
    
    bestScore = 10000
    bestMoveIndex = 0
    for x in range(9):
        if(board[x] == '-'):
            board[x] = ai
            score = minimax(board, True)
            board[x] = '-'
            if(score < bestScore):
                bestScore = score
                bestMoveIndex = x
    return bestScore #mini player
def maximize():
    
    bestScore = -10000
    bestMoveIndex = 0
    for x in range(9):
        if(board[x] == '-'):
                board[x] = ai
                score = minimax(board, False)
                board[x] = '-'
                #printBoard(board)
                if(score > bestScore):
                    bestScore = score
                    bestMoveIndex = x
    return bestScore                   


def minimize():
    
    bestScore = 10000
    bestMoveIndex = 0
    for x in range(9):
        if(board[x] == '-'):
            board[x] = player
            score = minimax(board, True)
            board[x] = '-'
            if(score < bestScore):
                bestScore = score
                bestMoveIndex = x
    return bestScore
                        
def findEmptySpot(board):
    emptySpots = []
    for x in range(9):
        if(board[x] == '-'):
            emptySpots.append(x)
    #print(emptySpots)o
    return emptySpots    
    

def calcScore():
    if(win() == 3): 
        return 5
    elif(win() == 2):
        return -5
    elif(win() == 4):
        return 0
    else:
        return -1

scores = {
    "X" 
}

def minimax(board, isMaximizing): #    C,[iif(player == "O" and winner = 2):
        #calcScore];; = player,
            #if(player == "X")= {}#if  && not 0emptySpotIndexes[i]indexOfBoardmoves.append( emptySpotIndexes[i]) board[]=ForMovesForMoves ndexndexndexfspoinputO()ts2scor10moves;else: {score: -5} checkAvailability()availreturnreturn -1 -1ning
    #if(calcScore() != -1):9\ !== null 0bestScore = 0  cal == win(board)bboardoardboardint()type(score)score = 0sscalcScore()#print(score)
    
    winner = calcScore()
    #
    if(winner != -1):
        score = calcScore()
        
        return score
    if(ai == "X"):#works when player is O        
        if(isMaximizing):
                bestScore = maximize()
        else: 
                bestScore = minimize()
        return bestScore
    else:   #;###### 
        if(isMaximizing):
            bestScore = reverseMaximize()
        else:     
            bestScore = reverseMinimize()
        return bestScore    

    

#8 ways to winboardboardgth.Player vs AI
def win():
    returnValue = 1
    if((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
        returnValue = 2
    elif((board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X')):
        returnValue = 3
    elif(len(findEmptySpot(board)) == 0):
        returnValue = 4     
    return returnValue    
        
def main():
    clearBoard(board)
    printBoard(board)

    validGame = False
    validLetter = False
    
    while(not validGame):
        inp = input("\nPlayer vs AI [1] or Player vs Player [2]? ")
        if(inp == "1"):
            validGame = True

            while(not validLetter):
                inp2 = input("\nDo you want to be X or O? ")
                if(inp2 == "X"):
                    validLetter = True
                    global player 
                    player = "X"
                    global ai 
                    ai = 'O'
                    print(ai) 
                elif(inp2 == "O"):
                    print(ai)
                    validLetter = True
                #    validLetter = True
                #    global ai 
                #    ai = "X"
                #    global player 
                #    player = "O"  
                ##/*    print(ai)  
                else:
                    print("Invalid input.")

            run = True
            while(run):
                if(player == "X" and ai == "O"):
                    inputX()  
                    printBoard(board)

                    if(win() == 3 or win() == 4):
                        break

                    inputAI()
                    printBoard(board)

                    if(win() == 2 or win() == 4):
                        break 
                elif(player == "O" and ai == "X"):
                    inputAI()
                    printBoard(board)

                    if(win() == 3 or win() == 4):
                        break

                    inputO()
                    printBoard(board)

                    if(win() == 2 or win() == 4):
                        break 
        elif(inp == "2"):
            validGame = True

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
        else: 
            print("Invalid input.")
            
    if(win() == 2):
        print('O wins!')
    elif(win() == 3):
        print('X wins!')    
    elif(win() == 4):
        print('Its a draw!')
                
if __name__ == "__main__":
    main()
