#Name:Josh Hodges
#authenticity: I worked solo on this
"""I noticed in the time comparison for the sorts that the python sort is exponentially
more efficient than a select sort. the python sort took less than 1/10th of a second and the selction sort took a little over 2 seconds for a list of 10,000 elements."""
from graphics import *

def readData(filename):
    file = open(filename, "r")
    line = file.readline()
    allNums = []
    while(line != ""):
        numbers = line.split()
        i = 0
        while i < len(numbers):
            allNums.append(eval(numbers[i]))
            i+=1
        line = file.readline()
    return allNums


def isinLinear(searchvalues, values):
    for i in searchvalues:
        if i==values:
            return True
    return False

def isinBinary(searchval, values):
    high=len(values)
    low=values[0]
    while low<= high:
        mid=(high+low)//2
        if values[mid]==searchval:
            return True
        elif values[mid]<searchval:
            low=mid+1
        else:
            high=mid-1

    return False

def selectionSort(values):
    n=len(values)
    for low in range(n-1):
        #becomes the new bottom of the list(0,1,2,3...) 
        m=low
        #starts at beginning of list and compares the numbers starting at pos1
        for i in range(low+1,n):
            #compares pos1 to pos of iteration in parent loop
            if values[i]<values[m]:
                #identifies the position in which one is larger than current position
                m=i
        swap(values,m,low)

def swap(values, m, low):
    #saves the value at the bottom of the list
    lowerval=values[low]
    #changes value at bottom of list to the next value ie 3,2,5 changes to 2,2,5
    values[low]=values[m]
    #replaces the value of the next one with the saved value 2,3,5
    values[m]=lowerval


def rectSort(rectangles):
    n=len(rectangles)
    for bottom in range(n-1):
        m=bottom
        for i in range(bottom+1,n):
            if calcArea(rectangles[i])<calcArea(rectangles[m]):
                m=i
        swap(rectangles,m,bottom)

        

def calcArea(rect):
    y1=rect.getP1().getY()
    y2=rect.getP2().getY()
    height=abs(y1-y2)
    x1=rect.getP1().getX()
    x2=rect.getP2().getX()
    width=abs(x1-x2)
    area=height*width
    return area

def main():
    rect1=Rectangle(Point(45,64),Point(66,125))
    rect2=Rectangle(Point(15,37),Point(125,415))
    rect3=Rectangle(Point(1,3),Point(15,12))
    rect4=Rectangle(Point(94,115),Point(284,12))
    rect5=Rectangle(Point(61,25),Point(37,75))
    rectangles=[rect1,rect2,rect3,rect4,rect5]
    print(rectangles)
    rectSort(rectangles)
    print (rectangles)
main()