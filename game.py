# Steps:
# 1)printing the game board
# 2)take player input
# 3) check for win or tie
# 4) switch the player 
# 5) check for win or tie again 

#to do:
#add a tie functionality
#use minimax algorithm 

import random
from itertools import permutations
def printBoard(board):
    x=0
    for i in range(0,9,3):
        x+=1
        print(" |".join(board[i:i+3]))
        if x!=3:
            print("__|__|__")

def checkWin(player, playerName):
    global winner
    winCombs=[[0,4,8],[6,4,2],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
    for i,j,k in permutations(player,3):
        if [i,j,k] in winCombs:
            print(playerName,"won!")
            winner=True
            break
    if winner==False and len(turn)==0:
            print("its a tie, no one won!")
def playerInput():
    global playerInputs
    global board
    no=int(input("select the position:"))
    board[no]=s
    playerInputs.append(no)
    turn.remove(no)
def compPlay():
    choice=random.choice(turn)
    turn.remove(choice)
    compInputs.append(choice)
    if s=='X':
        board[choice]="O"
    else:
        board[choice]="X"

winner=False
s=str(input("you want X or O:"))
board=["0","1","2","3","4","5","6","7","8"]
turn=[0,1,2,3,4,5,6,7,8]
playerInputs=[]
compInputs=[]
while winner==False:
    printBoard(board)
    playerInput()
    checkWin(playerInputs,"PLAYER")
    if winner==True:
        break
    compPlay()
    checkWin(compInputs,"COMPUTER")
    if winner==True:
            break