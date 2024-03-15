# Lab4.py
# Name 1:Josh Hodges
# Name 2: Ryan Walace

from graphics import *
import math


def target():
    #Open window
    width=500
    height=width
    target=GraphWin('Archery', width, height)

    centerpt=Point(width/2, height/2)
    #white
    whtring=Circle(centerpt,width/2)
    whtring.setFill('white')
    whtring.draw(target)
    #black
    blkring=Circle(centerpt,width/2.5)
    blkring.setFill('black')
    blkring.draw(target)
    #blue 
    bluring=Circle(centerpt,width/3.3)
    bluring.setFill('blue')
    bluring.draw(target)
    #red
    redring=Circle(centerpt,width/5)
    redring.setFill('red')
    redring.draw(target)
    #yellow
    yelring=Circle(centerpt,width/10)
    yelring.setFill('yellow')
    yelring.draw(target)

    prompt=Text(Point((width/2), 200),"Click to close")
    prompt.draw(target)

    promptbk=Rectangle(Point((width/4), 150), Point((width*.75),250))
    promptbk.draw(target)
    #close window
    target.getMouse()
    target.close()
    

def circle():
    
    #open window
    cir=GraphWin('Draw circle',500,500)
    #get center
    center=cir.getMouse()
    
    pt1=Point(center.getX(),center.getY())
    pt1.draw(cir)

    #get circumference edge
    edge=cir.getMouse()
    

    #calculate radius
    rad=math.sqrt((center.getX()-edge.getX())**2+(center.getY()-edge.getY())**2)

    circle=Circle(Point(center.getX(),center.getY()), rad)
    circle.draw(cir)

    raddis=Text(Point(250,100),"The radius of your circle is "+str(round(rad,2))+" units.")
    raddis.draw(cir)

    prompt=Text(Point(250,400),'Click to close!')
    prompt.draw(cir)

    cir.getMouse()
    cir.close


def colorShape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    #create window
    winWidth = 400
    winHeight = 400
    win = GraphWin("Color Shape", winWidth, winHeight)
    win.setBackground("white")

    #create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(winWidth/2, winHeight-20), msg)
    inst.draw(win)

    #create circle in window's center
    shape = Circle(Point(winWidth/2, winHeight/2 - 30), 50)
    shape.draw(win)

    #redTexPt is 50 pixels to the left and forty pixels down from center
    redTextPt = Point(winWidth/2 - 50, winHeight/2 + 40)
    redText = Text(redTextPt, "Red: ")
    redText.setTextColor("red")

    #greenTextPt is 30 pixels down from red
    greenTextPt = redTextPt.clone()
    greenTextPt.move(0,30)
    greenText = Text(greenTextPt, "Green: ")
    greenText.setTextColor("green")

    #blueTextPt is 60 pixels down from red
    blueTextPt = redTextPt.clone()
    blueTextPt.move(0,60)
    blueText = Text(blueTextPt, "Blue: ")
    blueText.setTextColor("blue")

    #display rgb text
    redText.draw(win)
    greenText.draw(win)
    blueText.draw(win)

    #create red entry box
    redent=Entry(Point(winWidth/2, winHeight/2 + 40),5)
    redent.setText(0)
    redent.draw(win)
    #create green entry box
    greenent=redent.clone()
    greenent.move(0,30)
    greenent.draw(win)
    #create blue entry box
    blueent=redent.clone()
    blueent.move(0,60)
    blueent.draw(win)

    

    for i in range(4):
        win.getMouse()
        rednum=int(redent.getText())
        greennum=int(greenent.getText())
        bluenum=int(blueent.getText())
    #set the color
        shape.setFill(color_rgb(rednum,greennum,bluenum))
        reset=Text(Point((winWidth/2), (winHeight/10)),'Click to reset for new color')
        reset.draw(win)
        win.getMouse()
        reset.undraw()
        greenent.setText('0')
        redent.setText('0')
        blueent.setText('0')
    reset.undraw()
    exit=Text((winWidth/2), (winHeight/10),'Click to exit')
    exit.draw(win)
    win.getMouse()
    win.close

def processString():
    str1=input('input your message:')
    print('The first character of your message is:',str1[0])
    print('The last character of your message is:',str1[-1])
    print('The characters in position 2-5 are:',str1[2:5])
    print('The concatonation of the first and last characters of the string is:',str1[0]+str1[-1])
    print(str1[0:3]*10)
    for i in str1:
        print(i)
    print(len(str1))
    
def processList():
    pt=Point(5,10)

    values=[15,'hi',2.5,'there',pt,'7.2']

    #a
    x=values[1]+values[3]
    print(x)
    #b
    x=values[0]+values[2]
    print(x)
    #c
    x=str(values[1])*15
    print(x)
    #d
    x=[values[2],values[3],values[4]]
    print(x)
    #e
    x=[values[2],values[3],values[0]]
    print(x)
    #f
    x=[values[2],values[0],float(values[5])]
    print(x)
    #g
    x=float(values[5])+values[2]+values[0]
    print(x)
    #h
    x=len(values)
    print(x)


    
def main():
    #target()
    #circle()
    #colorShape()
    processString()
    processList()


main()





