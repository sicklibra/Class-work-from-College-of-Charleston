## Josh Hodges
## lab2.py

#import 
import math
import time
from graphics import*
#Calculate the average of a group of numbers per assignment instructions
def average():
    print("Finds average")
    quant=int(input("How many grades will be included in the average?:"))

    #initialize values
    hwtot=0
    place=0
    for grades in range (quant):
        #specifies the assignment number to be entered
        place=place+1
        #accumulates the total value of the homework
        hwtot=hwtot+float(input("Enter your grade on HW"+str(grades+1)+": "))

    #output of the average as calculated below
    avg=hwtot/quant
    print("Your average is:", round(avg,2))

def newton():
    #this program approximates the square root of a number using sir Isaac Newtons method.
    #accepts the number to be approximated and the number of times it is to be refined.
    valinit=int(input("What number would you like the approximation of the square root of?: "))
    cycle=int(input("How many times would you like to improve the appoximation?: "))

    #loop that runs the specified number of times for the approximation
    #initialize separation of initial input and variable to be calculated
    approx=valinit/2
    for approximation in range(cycle):
        approx=(approx+(valinit/approx))/2
    
    #output of the approximate square root 
    print("The approximate square root of", valinit, "is",approx)

#create sequence that moves integers up two every other iteration.
def sequence():
    terms=int(input("how many terms in the series would you like?"))
    #initialize input
    accum=1
    var=1
    for sequence in range(terms):
       #by alternating between even and odd this equasion works like a flip flop gate
       #if i need to skip the initial flop i could initialize var as an odd #
       var=(var+1)%2
       #by printing the value before the calculation, it allows me to utilize 1 as an initial value. 
       #print(accum)
       accum=(var+var)+accum
       print(accum)


#this evaluates the value of pi
def pi():
    n=int(input("how many iterations would you like to see of pi?: "))

    #the loop 
    #initialize variables
    var=0
    var1=1
    accumtop=0
    accumbot=1
    piit=1
    for piloop in range(n):
        #create flip flops
        var=(var+1)%2
        var1=(var1+1)%2
        #create variable for numerator
        accumtop=(var+var)+accumtop
        #print(accumtop)
        #create variable for denominator
        accumbot=(var1+var1)+accumbot
        #print(accumbot)
        piit=(accumtop/accumbot)*piit

    piapprox=piit*2
    print("Given the number of iterations you specified pi is",piapprox)


def house():
    #open window to the right color
    win=GraphWin("House", 1200, 720)
    win.setBackground("lightblue")

    #create Rectangle for base of house
    rect1=Rectangle(Point(300,720),Point(900,420))
    rect1.setOutline("black")
    rect1.setFill("red")
    rect1.draw(win) 

    #create door
    door=Rectangle(Point(550,720),Point(650,520))
    door.setFill("blue")
    door.setOutline("black")
    door.draw(win)

    #create knob
    knob=Circle(Point(630,620), 10)
    knob.setFill("yellow")
    knob.draw(win)

    #roof work
    roof=Polygon(Point(600,50),Point(300,420),Point(900,420),Point(600,50))
    roof.setFill("beige")
    roof.setOutline("black")
    roof.draw(win)


    #make window close when clicked by the mouse. 
    win.getMouse()
    win.close()
def main():
    average()
    newton()
    sequence()
    pi()
    house()

main()