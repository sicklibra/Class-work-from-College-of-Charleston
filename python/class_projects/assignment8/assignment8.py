#Author: Josh Hodges
#Date:16NOV23
#statement of problem: Create a number guessing game using binary search principles

#statement of authenticity:I worked on this alone
"""layman problem/solution:I will start by generating a random number between 1 and 100
the graphic interface will have three buttons, Guess, Quit, Play again. The game will suggest 
guesses based on previous guess that the user has made based on binary search principles."""

#for random number generator.
import random
import time
from graphics import *


width=500
height=500
game=GraphWin('Guess my number',width, height)
game.setBackground('beige')

def staticgraphics():
    #This compiles a list of all of the objects to follow the program around to clear when finished.   
    objects=[]

    prompt=Text(Point(width/2, 30),'I have chosen a number between 1 and 100, guess it.')
    prompt.draw(game)
    objects.append(prompt)
       
    guesstxt=Text(Point(100,200),'Enter your guess')
    guesstxt.draw(game)
    objects.append(guesstxt)    

    #buttons 
    stoverbx=Rectangle(Point(20,400),Point(110,450))
    stoverbx.setOutline('Black')
    stoverbx.draw(game)
    objects.append(stoverbx)

    strtovr=Text(Point(60,425), 'Start Over')
    strtovr.draw(game)
    objects.append(strtovr)

    quitbx=Rectangle(Point(480,400),Point(390,450))
    quitbx.setOutline("black")
    quitbx.draw(game)
    objects.append(quitbx)

    quit=Text(Point(435,425),'Quit!')
    quit.draw(game)
    objects.append(quit)    

    submitbx=Rectangle(Point(195,400),Point(305,450))
    submitbx.setOutline('black')
    submitbx.draw(game)
    objects.append(submitbx)

    submit=Text(Point(250,425),'Make Guess')
    submit.draw(game)
    objects.append(submit)

    return objects
    
def start(objects):
    suggestion=50
    #text boxes to be altered in the game.
    suggest=Text(Point(225,160),'I suggest'+str(suggestion))
    suggest.setTextColor('red')
    suggest.draw(game)
    objects.append(suggest)

    guessbx=Entry(Point(225,200),10)
    guessbx.draw(game)
    objects.append(guessbx)

    #generates the value to be guessed
    target=random.randint(1,100)
    
    #initialize variable to keep game rolling
    high=100
    low=1
    quitter=False
    counter=0
    while quitter==False:
        #initialize variable for while loop
        guessfail=True 
        while guessfail==True:       
            guess=guessbx.getText()
            click=False
            while click==False:                
                select=game.getMouse()

                outcome, click= selection(select)                
                if outcome=='quit':
                    #Exits the game completeley
                    return True
                elif outcome=="restart":
                    #removes all items from the window and restarts game at beginning
                    wipeout(objects)
                    return False
                elif outcome=="submit":
                    #grabs text from entry box
                    guess=guessbx.getText()
                    #verifies value provided is valid
                    test=guesstest(guess)
                    print('test',test)
                    if test==True: 
                        #triggers the sentinal in while loop                       
                        guessfail=False
                    else:
                        #generates a brief note if entry is invalid 
                        failnote=Text(Point(250,100),"Please enter a whole number")
                        failnote.draw(game)
                        time.sleep(1.5)
                        failnote.undraw()

        counter+=1
        winner=play(guess, target)       
        if winner==True:
            wipeout(objects)
            again= winning(counter,objects)
            return again               
        #Suggest calculator will return the next suggested choice based on users previous
        #guess using binary search principles
        suggestion, high, low =suggestcal(target, guess, high, low)
        #should change the suggested next guess 
        suggest.setText('I suggest'+str(suggestion))

        

       
    
def wipeout(objects):
    print(objects)
    for i in objects:
        i.undraw()
        objects.remove(i)


def guesstest(guess):
        try: 
            int(guess)
            return True
        except ValueError:                
            return False
        
#button behavior
def selection(position):
    posx=position.getX()
    posy=position.getY()
    #print(position)
    #quitter, reset, submit, click
    #submit
    if (posx>195 and posx<305)and (posy<=450 and posy>=400):
        return 'submit',  True
    #reset
    elif(posx>20 and posx<110)and (posy<=450 and posy>=400):
        return 'restart', True
    #quit
    elif(posx>390 and posx<480)and (posy<=450 and posy>=400):
        return 'quit', True
    else: 
        return False, False
    
def suggestcal(target,guess, high, low):
    guess=int(guess)
    #if the number is less than the target
    if target>guess:
        #adjust low to one above the guess
        low=guess+1
        #calculate center
        mid=(high-low)//2+guess
        return mid, high, low
    #if the number is greater than target
    if target<guess:
        #adjust the top end 
        high=guess-1
        #calculate center
        mid=(high-low)//2+low
        return mid, high, low
    
    
def play(guess, target):
    guess=int(guess)
    if  guess < target:
        outcome=Text(Point(250,300),'Too Low!')
        outcome.draw(game)
        time.sleep(2)
        outcome.undraw()
    elif guess>target:
        outcome=Text(Point(250,300),'Too high!')
        outcome.draw(game)
        time.sleep(2)
        outcome.undraw()
    else:
        #updates value of var winner to be true triggering the winner function
        return True

def winning(count,objects):
    colors=['red','orange','yellow','green','blue', 'indigo','violet']

    stoverbx=Rectangle(Point(20,400),Point(110,450))
    stoverbx.setOutline('Black')
    stoverbx.draw(game)
    objects.append(stoverbx)

    strtovr=Text(Point(60,425), 'Start Over')
    strtovr.draw(game)
    objects.append(strtovr)

    quitbx=Rectangle(Point(480,400),Point(390,450))
    quitbx.setOutline("black")
    quitbx.draw(game)
    objects.append(quitbx)

    quit=Text(Point(435,425),'Quit!')
    quit.draw(game)
    objects.append(quit)

    winner=Text(Point(250,250),'You Win!\nCongratulations!')
    winner.setSize(20)
    winner.setOutline('black')
    winner.setTextColor('white')
    winner.draw(game)
    objects.append(winner)

    countmsg=Text(Point(250,300), "you did it in "+str(count)+' guesses!')
    countmsg.draw(game)
    objects.append(countmsg)

    for i in colors:
        game.setBackground(i)
        time.sleep(.4)

    click=False
    while click==False:
        select=game.getMouse()

        outcome, click= selection(select)                
        if outcome=='quit':
            #Exits the game completeley
            return True
        elif outcome=="restart":
            #removes all items from the window and restarts game at beginning
            wipeout(objects)
            winner.undraw()
            game.setBackground('beige')
            return False
        else:
            click=False
    
    

def main():
    quits=False
    while quits==False:
        objects=staticgraphics()
        quits=start(objects)
    
    game.close()
    
        
main()
