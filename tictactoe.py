#Imports
import pygame
import os
pygame.font.init()

#Constants
WIDTH, HEIGHT = 1152, 557

#Setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TicTacToe")
FPS = 60

#Images
mainmenu = pygame.image.load(os.path.join('Assets', 'tictactoepng.png'))
grid = pygame.image.load(os.path.join('Assets', 'tictactoegrid.png'))
choose = pygame.image.load(os.path.join('Assets', 'tictactoechoose.png'))

circle = pygame.image.load(os.path.join('Assets', 'transparentcircle.png'))
circle = pygame.transform.scale(circle, (100,100))

cross = pygame.image.load(os.path.join('Assets', 'transparentx.png'))
cross = pygame.transform.scale(circle, (100,100))

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

def draw_window(mainMenu, playerChoose, playingGame):
    if mainMenu:
        WIN.blit(mainmenu, (0,0))
    elif playerChoose:
        WIN.blit(choose, (0,0))
    elif playingGame:
        WIN.blit(grid, (0,0))
        
def main():
    run = True
    playingGame = True
    mainMenu = True
    playerChoose = False
    
    while run:
        WIN.fill((0,0,0))
        draw_window(mainMenu, playerChoose, playingGame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            print(x, y)
            if mainMenu:
                if(x > 482 and x < 643 and y > 184 and y < 235):
                    print("First button")
                    mainMenu = False
                    playerChoose = True
                
                if(x > 482 and x < 643 and y > 258 and y < 311):
                    print("Second button")
                    mainMenu = False
                    playerChoose = True

            elif playerChoose:
                if(x > 360 and x < 530 and y > 185 and y < 340):
                    print("First button")
                    playerChoose = False
                    playingGame = True
                
                if(x > 598 and x < 783 and y > 185 and y < 340):
                    print("Second button")
                    playerChoose = False
                    playingGame = True
        
        pygame.display.update()

    pygame.quit()
    
    #Old code below
    #=============================
    # clearBoard(board)
    # printBoard(board)

    # validGame = False
    # validLetter = False
    
    # while(not validGame):
    #     inp = input("\nPlayer 1 vs AI [1] or Player 1 vs Player 2 [2]? ")
    #     if(inp == "1"):
    #         validGame = True

    #         while(not validLetter):
    #             inp2 = input("\nDo you want to be X or O Player 1? ")
    #             if(inp2 == "X" or inp2 == "x"):
    #                 validLetter = True
    #                 global player 
    #                 player = "X"
    #                 global ai 
    #                 ai = 'O'
    #                 print(ai) 
    #             elif(inp2 == "O" or inp2 == "o"):
    #                 print(ai)
    #                 validLetter = True
    #             #    validLetter = True
    #             #    global ai 
    #             #    ai = "X"
    #             #    global player 
    #             #    player = "O"  
    #             ##/*    print(ai)  
    #             else:
    #                 print("Invalid input.")

    #         run = True
    #         while(run):
    #             if(player == "X" and ai == "O"):
    #                 inputX()  
    #                 printBoard(board)

    #                 if(win() == 3 or win() == 4):
    #                     break

    #                 inputAI()
    #                 printBoard(board)

    #                 if(win() == 2 or win() == 4):
    #                     break 
    #             elif(player == "O" and ai == "X"):
    #                 inputAI()
    #                 printBoard(board)

    #                 if(win() == 3 or win() == 4):
    #                     break

    #                 inputO()
    #                 printBoard(board)

    #                 if(win() == 2 or win() == 4):
    #                     break 
    #     elif(inp == "2"):
    #         validGame = True

    #         run = True
    #         while(run):
    #             inputX()
    #             printBoard(board)

    #             if(win() == 3 or win() == 4):
    #                 break

    #             inputO()
    #             printBoard(board)

    #             if(win() == 2 or win() == 4):
    #                 break
    #     else: 
    #         print("Invalid input.")
            
    # if(win() == 2):
    #     print('O wins!')
    # elif(win() == 3):
    #     print('X wins!')    
    # elif(win() == 4):
    #     print('Its a draw!')
                
if __name__ == "__main__":
    main()
