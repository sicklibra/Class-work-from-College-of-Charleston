## Lab8.py
##
## Name 1:Josh Hodges
##
## Name 2:Tyler Martin
##

from graphics import *
from math import sqrt 


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
        
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] **2

def sumList(nums):
    Sum = sum(nums)
    return Sum
        
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

    
def testTens():
    values = [5, 2, -3]
    print(values)
    addTen(values)
    print(values)
    
def writeSumOfSquares():
    #nums = [3,5.7,2]
    #strList = ["3","5.7","2"]

    
    inFile = str(input("What is the Name of the File to Input: "))
    inFile = open(inFile, "r")

    outFile = open("output.txt", "w")
    
    output = ""
    for line in inFile.readlines():
       
        strList = line.split(" ")
        print(strList)
        
        toNumbers(strList)
        nums = strList
        print(nums)
        
        squareEach(nums)
        Sum = sumList(nums)
        print(Sum)
        
        #output = output + str(Sum)+ "\n"
        print("Sum of Square=",Sum, "\n", file=outFile)

    print('your file has been processed! check', outFile,"for results.")
    
    #outFile.write("Sum of Squares =," output,)

    

    
    """ 
    nums = [3,5.7,2]
    #strList = ["3","5.7","2"]
    
    #nums = toNumbers(strList)
    #print(strList)
    
    print(nums)
    squareEach(nums)
    print(nums)

    Sum = sumList(nums)
    print(Sum)
    """
    
    
def starter():
    """
    Ask for a wrestler's weight and number of wins, determine whether
    the wrestler is a starter.
    """
    #get weight and wins input
    weight=float(input("What is the weight of the wrestler?: "))
    numWins=int(input("How many wins does the wrestler have?: "))
    #determine if the wrestler meats the easiest criteria.
    if weight>199 or numWins>20:
        print('This wrestler is eligable to be a starter')
    #does wrestler meet the weight range?
    elif weight>=150 and weight<160:
        #if within weight range, do they have wins necessary
        if numWins>=5:
            print('This wrestler is eligable to be a starter!')
        else:
            print('Sorry your wrestler does not fit the bill! :(')
    else:
         print('Sorry your wrestler does not fit the bill! :(')
        




def testTens():
    values = [5, 2, -3]
    print(values)
    addTen(values)
    print(values)

def circleOverlap():
    """
    Draw two circles and determine whether they overlap.
    """
    #Build window
    winHeight = 400
    winWidth = 400
    win = GraphWin("Overlapping circles", winHeight, winWidth)

    #Text area for instructions for user
    instruct = Text(Point(winWidth/2, winHeight-10), "")
    instruct.draw(win)

    #Get center point and x/y for center
    instruct.setText("To draw a circle, click the centerpoint for the circle")
    center = win.getMouse()
    center.draw(win)
    cX = center.getX()
    cY = center.getY()

    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle.")
    border = win.getMouse()
    bX = border.getX()
    bY = border.getY()

    #Calculate radius using Euclidean distance
    radius = sqrt((cX-bX) ** 2 + (cY-bY) ** 2)
    circle = Circle(center, radius)
    circle.draw(win)


    #get second circle center
    instruct.setText("To draw the next circle, click the centerpoint agian")
    center2 = win.getMouse()
    center2.draw(win)
    cX2 = center2.getX()
    cY2 = center2.getY()

    #get second circle circumfrence
    instruct.setText("Click a point on the border of the circle.")
    border2 = win.getMouse()
    bX2 = border2.getX()
    bY2 = border2.getY()

    #Calculate radius2 using Euclidean distance
    radius2 = sqrt((cX2-bX2) ** 2 + (cY2-bY2) ** 2)
    circle2 = Circle(center2, radius2)
    circle2.draw(win)

    #determine if the circles overlap
    """to do this i am going to calculate the distance between center points if the distance bw centers is less than or equal to the combined radii, the circles overlap."""
    #calculate the distance between center points
    cpdist=sqrt((cX-cX2)**2+(cY-cY2)**2)

    #compare distance of center points to combined radii
    if cpdist <= radius+radius2:
        instruct.setText("Your circles overlap.")
    else:
        instruct.setText("Your Circles do not overlap.")

    
    # Wait for another click to exit
    
    exit=Text(Point(winWidth/2, 10),"Click anywhere to close.")
    exit.draw(win)
    win.getMouse()
    win.close()


def leapYear():
    year=int(input("What year do you want to check for a leap year?"))
    
    if year%400 == 0:
        print(year, "is a leap year!")
    elif year%4 == 0:
        if year%100 == 0:
            print(year, "is not a leap year.")
        else:
            print(year, 'is a leap year!')
    else:
        print(year,"is not a leap year")

def main():
    starter()
    circleOverlap()
    leapYear()
    writeSumOfSquares()

main()
