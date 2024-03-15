#Author: Josh Hodges
#Date:9NOV23
"""statement of problem: Create a game in which a
 ball bounces around the screen. user drops red
 rocks and trys to get ball to hit them. if the
 rocks get hit enough times they turn green.When the ball contacts a rock
 it will change direction by 90 degrees there is also a save counter so if 
 rocks are hit 20X or more it will set a new random direction for the ball."""
#statement of authenticity: I worked on this alone.
"""layman problem/solution: using the random import, 
i will generate a window and drop a ball of random 
color in a random location within. The user will 
then drop "rocks" in the window with the goal of 
getting the ball to hit the rocks. The ball will 
begin moving in a random direction. The rocks will change from red to 
yellow to green as the ball hits
them. the game is over when all rocks are green. """

from graphics import *
import time
import random
import math

def startGame():
    height=400
    width=400
    game=GraphWin("Drop Dem Rocks", width, height)
    game.setBackground("lime green")

    #Generate the ball
    ball=Circle(Point(random.randint(5,390),random.randint(5,390)),10)
    #Get color ints from random color
    red, green, blue=randomColor()
    ball.setFill(color_rgb(red, green, blue))
    ball.draw(game)
    #generate text for Prompt
    prompt=Text(Point(200,200),'Place 5 rocks for the ball to hit.\n click to place rock1')
    prompt.draw(game)

    #draw rocks.
    #rock1
    c1=game.getMouse()
    rock1=Rectangle(Point(c1.getX()-10,c1.getY()-10),Point(c1.getX()+10,c1.getY()+10))
    rock1.setFill("red")
    rock1.draw(game)
    #change the text 
    prompt.setText('4 Left')
    #rock2
    c2=game.getMouse()
    rock2=Rectangle(Point(c2.getX()-10,c2.getY()-10),Point(c2.getX()+10,c2.getY()+10))
    rock2.setFill("red")
    rock2.draw(game)
    #change text
    prompt.setText('3 left')
    #rock 3
    c3=game.getMouse()
    rock3=Rectangle(Point(c3.getX()-10,c3.getY()-10),Point(c3.getX()+10,c3.getY()+10))
    rock3.setFill("red")
    rock3.draw(game)
    #change text
    prompt.setText("2 rocks left")
    #rock4
    c4=game.getMouse()
    rock4=Rectangle(Point(c4.getX()-10,c4.getY()-10),Point(c4.getX()+10,c4.getY()+10))
    rock4.setFill("red")
    rock4.draw(game)
    #change text
    prompt.setText("This is the last rock. \nThe game is over when the ball turns them all green!")
    #rock 5
    c5=game.getMouse()
    rock5=Rectangle(Point(c5.getX()-10,c5.getY()-10),Point(c5.getX()+10,c5.getY()+10))
    rock5.setFill("red")
    rock5.draw(game)
    #remove text
    prompt.undraw()
    #rock centers for reference in didCollide
    rockctrlst=[c1,c2,c3,c4,c5]

    #initialize game motion statement
    win=False
    #stop gap if rocks get missed to change direction
    savior=0
    #while loop to make sure ball is not crawling
    movecheck=1
    while movecheck==1:
        randmvX=random.randint(-10,10)
        randmvY=random.randint(-10,10)
        if (randmvX<5 and randmvX>-5) or (randmvY<5 and randmvY>-5):
            movecheck=1
        else:
            movecheck=2
    #print(randmvX,randmvY)
    #initialize hit count list
    hitcnt=[0, 0, 0, 0, 0]
    #rock position reference
    rocklst=[rock1, rock2, rock3, rock4, rock5]
    #get the ball rolling
    while win==False:
        #this will signal when the game ends
        tot=0
        ball.move(randmvX,randmvY)
        #determine if ball hits vertical wall and adjust movement 
        wallbouncev=hitVert(ball,game)
        if wallbouncev==True:
            randmvX=-(randmvX)
        #determine if ball hits horizontal wall and adjust movement.
        wallbounceh=hitHorizontal(ball,game)
        if wallbounceh==True:
            randmvY=-(randmvY)
        #determine if the ball hits a rock
        rockhit,outcome, hitcnt, save=didCollide(ball,rockctrlst,hitcnt)
        #saving counter Changes the ball randomly if too many rock hits and no win.
        savior+=save
        if savior>20:
            savior=0
            movecheck=1
            while movecheck==1:
                randmvX=random.randint(-10,10)
                randmvY=random.randint(-10,10)
                if (randmvX<5 and randmvX>-5) or (randmvY<5 and randmvY>-5):
                    movecheck=1
                else:
                    movecheck=2
        #initialize position counter for rock
        rockpos=0 
        #if rock is hit       
        if rockhit==True:
            # print(hitcnt)
            #compare each item in the hit list to the rock in correlating position
            for i in hitcnt:                
                if i==1:
                    rocklst[rockpos].setFill('yellow')
                elif i==2:
                    rocklst[rockpos].setFill('green')
                if i>=2:
                    #counter that will signal the end of game when all rocks have
                    #been hit twice or more.
                    tot=tot+1                
                rockpos+=1
            #tells the ball which way to move on contact.
            if outcome==4:
                randmvY=-(randmvY)
            if outcome==3:
                randmvY=-(randmvY)
            if outcome==2:
                randmvX=-(randmvX)
            if outcome== 1:
                randmvX=-(randmvX)
        #Signals end of game
        if tot==5:
            win=True
        #movement speed
        time.sleep(.05)
        
    
    #winning notification.
    winnote=Text(Point(width/2, height/2),"congratulations!\n You win! \n Click to close")
    winnote.draw(game)
    #close window
    game.getMouse()
    game.close()

def didCollide(ball, rock, rockhitcnt):
    ballx=ball.getCenter().getX()
    bally=ball.getCenter().getY()
    #iteration counter
    count=0
    #figures out which rock was hit
    for i in rock:
        #tells if ball is in hit range.
        dist=math.sqrt((i.getX()-ballx)**2+(i.getY()-bally)**2)
        if dist<=20:
            #adjusts the appropriate place in the hit count list
            rockhitcnt[count]=int(rockhitcnt[count])+1
            #right side hit
            if ballx>i.getX() and (bally<i.getY()+10 and bally>i.getY()-10):
                return True,1,rockhitcnt, 1
            #left side hit
            if ballx<i.getX() and (bally<i.getY()+10 and bally>i.getY()-10):
                return True, 2, rockhitcnt,1
            #bottom hit
            if bally>i.getY() and (ballx<i.getX()+10 and ballx>i.getX()-10):
                return True, 3, rockhitcnt,1
            #top hit
            if bally<i.getY() and (ballx<i.getX()+10 and ballx>i.getX()-10):
                return True, 4, rockhitcnt,1
            # if rockhitcnt.count('3')==5:
            #     return 1, 5, rockhitcnt
        count=count+1    
    # print(rockhitcnt)
    #return no hit
    return False ,6,rockhitcnt,0



def hitVert(ball, win):
    #did ball hit vertical wall?
    center=ball.getCenter().getX()
    #determines if center of circle is within collision dist of side
    if center<10 or center>390:
        red, green, blue=randomColor()
        ball.setFill(color_rgb(red, green, blue))
        return True
    else:
        return False


def hitHorizontal(ball,win):
    #did ball hit horizontal wall?
    center=ball.getCenter().getY()
    #determines if center of circle is within collision dist of side
    if center<10 or center>390:
        red, green, blue=randomColor()
        ball.setFill(color_rgb(red, green, blue))
        return True
    else:
        return False


def randomColor():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    return red, green, blue



def main():
    startGame()
   

main()