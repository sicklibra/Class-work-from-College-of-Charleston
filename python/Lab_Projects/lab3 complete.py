##Lab 3 - Graphics and accumulations
##Name:Josh Hodges
##Name:Caleb Dixon


import math

from graphics import *

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the
    square is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    #Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 3", width, height)

    #number of times user can move square
    numClicks = 5

    #create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to move Square")
    instructions.draw(win)

    #Acquire clidk points
    #builds a circle
    shape = Rectangle(Point(180, 180), Point(200,200))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click multiple times to move the
    #square
    for i in range(numClicks):
        pt = win.getMouse()
        center = shape.getCenter() #center of square

        #move amount is distance from center of circle to the
        #point where the user clicked
        dx = pt.getX() - center.getX()
        dy = pt.getY() - center.getY()
        shape2=shape.clone()
        shape2.draw(win)
        shape2.move(dx, dy)
    quit=Text(Point(200,200),"Click anywhere to quit!")
    quit.setSize(20)
    quit.draw(win)

    win.getMouse()
    win.close()

def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
            Display the perimeter and area of the rectangle in the window
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    print("Hello, rectangle")
    rect=GraphWin("Rectangle",400,400)
    rect.setBackground('light blue')
    #Prompt 
    prompt=Text(Point(200,200), 'Click two opposing corners to draw rectangle.')
    prompt.draw(rect)

    #get user input points
    p1=rect.getMouse()
    p1.draw(rect)
    p2=rect.getMouse()

    #Draw the box
    box=Rectangle(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()))
    box.setFill('light green')
    box.setOutline('black')
    box.draw(rect)

    #loose the prompt
    prompt.undraw()

    #assign variables
    length=abs(p1.getY()-p2.getY())
    width=abs(p1.getX()-p2.getX())

    #run calculations
    area=length*width
    perimeter=2*(length+width)

    #output final varibales
    output= Text(Point(200,100), 'The area of the rectangle is '+str(area)+"\n"+"the perimeter is "+str(perimeter))
    output.draw(rect)

    #close window
    rect.getMouse()
    rect.close()



def pi2():

    #Gather user input
    n = int(input("Enter the number of terms to sum: "))
    #assign loop varibales
    
    var = 1
    bottom = -1
    pi = 0
    flip = 0
    #Create flip flops inside of loop
    for i in range(n):
        var = (var + 1) % 2
        flip = (flip + 1) % 2
        
        #sequence bottom number
        bottom = 2 + bottom

        #Calculate pi
        pi = (4/bottom + pi) * flip + (pi- 4/bottom) * var

        

    #Print final output
    print("Your calculation of pi is ", pi)
    print("That is", abs(math.pi - pi), "from pi")


def anotherSeries():
    #get user input
    n = int(input("Enter the number of terms: "))
    #create list
    num =[2,4,6]

    #Run loop to locate values in list
    var = 0
    for i in range(n):
        print(num[i % 3])
        var = var+num[i%3]
        
        
    #output total 
    print("The total is", var)
    
        


def main():
    #squares()
    #rectangle()
    #pi2()
    anotherSeries()

main()
