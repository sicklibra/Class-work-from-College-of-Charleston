#Author: Josh Hodges
#Date:02NOV23
#statement of problem: 
#statement of authenticity:
#layman problem/solution:


def calculateSum(value, numIterations):
    #Create while loop that allows loop to run as long as there are iterations left
    itcounter=numIterations
    sum=0
    while itcounter > 0:
        sum += value
        itcounter-=1

    return sum

def areEqual(num1, num2):
    truth=num1==num2
    return truth

def ticTacToe():
    boardlist=boardlst()
    win=False
    print('X goes first!')
    while win==False:
        displaybrd(boardlist)
        
    #initialize try and except variable
        test=1
        while test==1:
            try:
                placex=int(input('X pick your number between 1 and 9: '))
                test=2
            except ValueError:
                print("not a valid number")

        while test==2:
            check=valid(boardlist,placex)
            if check==False:
                print("That is not a valid position!")
            else:
                play(boardlist,"X",placex)
                test=3
        displaybrd(boardlist)
        win=winner(boardlist)
        if win==True:
            break
        tie=tied(boardlist)
        if tie==True:
            print("The game is a tie")
            break

        while test==3:
            try:
                placeO=int(input('O pick your number between 1 and 9: '))
                test=4
            except ValueError:
                print("not a valid number")

        while test==4:

            check=valid(boardlist,placeO)
            if check==False:
                print("That is not a valid position!")
            else:
                play(boardlist,"O",placeO)
                test=5
        displaybrd(boardlist)
        win=winner(boardlist)

    

def boardlst():
    boardlist=['1','2','3','4','5','6','7','8','9']
    return boardlist

def displaybrd(board):
    # boardlst=boardlist
    print(board[0]+" | "+board[1]+ " | "+board[2])
    print("----------------" )
    print(board[3]+" | "+board[4]+ " | "+board[5])
    print("----------------" )
    print(board[6]+" | "+board[7]+ " | "+board[8])


def play(board, xoro, position):
    if xoro=="X" or xoro=="O":
        board[position-1]=xoro


def valid(board,position):
    if position>=1 and position<=9:
        if board[position-1]=="X" or board[position-1]=="O":
            return False
    else:
        return True

def winner(board):
    wincombo=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for i in wincombo:
        p1=board[i[0]]
        p2=board[i[1]]
        p3=board[i[2]]
        if p1==p2==p3:
            if p1=="O":
                print("congratulations player2! you win!")
            else:
                print("congratulations player1! you win!")
            return True
    return False

def tied(board):
    xs=board.count("X")
    if xs== 5: 
        return True
    else:
        return False



def main():
    print("This program calculates the sum of a number and it's self the number of times you want it to.")
    test=1
    while test==1:
        try:
            number=float(input("What number would you like summed up?: "))
            test=2
        except ValueError:
            print ("That is not a valid decimal or integer. Try again")

    while test==2:
        try:
            iteration=int(input("How many times would you like to add it?: "))
            test=3
        except ValueError:
            print("That is not a whole number please try again.")

    
    while test==3:
        try:
            compare=float(input("What do you think your sum will be?: "))
            test=4
        except ValueError:
            print("That is not a number. Try again")
    # while test==4:
    #     try:
    #         num1=float(input("What is the first number?: "))
    #         test=5
    #     except ValueError:
    #         print("That is not a number. Try again.")
    print('Now lets see if you got that right.')
    total=calculateSum(number, iteration)
    print("Your total is:",total)
    truthstatement=areEqual(total, compare)
    print('Is', total, "equal to", compare,"?:  ", truthstatement)

    ticTacToe()
main()