#Author: Josh Hodges
#Date:19SEP23
#statement of problem: This program aims to create a fall 
#greeting card that displays a Jack-o-lantern and happy fall messages
#this program also needs a button to close.
#statement of authenticity:I worked on this project alone.
#layman problem/solution:I will do this in several steps
#1first i will set the background to a night sky and create a rectangle that encompasses the bottom of the window for the ground
#2Create a moon as a circle that will utilize a loop to move across the sky,  and display the message "Happy Halloween"
#3create a pumpkin using overlapping orange ovals with black outlines. 
#4 make the eyes utilizing points input by the user creating two triangles that will then fall exposing flickering eye holes
#5 will make the mouth using a polygon function with a ton of points
#6 once the animations have finished have a button pop up in the bottom center of the screen that says click to close. clicking closes the window. 

#center x=725 center y=360

import time
import copy
from graphics import*
    
def greet():
    #open window with night background
    card=GraphWin("Spooky Wishes",1500,720)
    card.setBackground("midnight blue")
   
    #create moon
    moon=Circle(Point(0,475), 130)
    moon.setFill("peachpuff")
    moon.setOutline("peachpuff")
    moon.draw(card)

    #create ground
    ground=Rectangle(Point(0,360),Point(1500,720))
    ground.setFill("dark green")
    ground.draw(card)
    
    #create greeting message
    greeting=Text(Point(725,100),"Happy Halloween!")
    greeting.setSize(20)
    greeting.setStyle("bold italic")
    greeting.setFace("times roman")
    greeting.draw(card)

    #Draw the pumpkin
    #background fillers
    pumpbackleft=Oval(Point(612,325),Point(737,600))
    pumpbackleft.setFill("orange")
    pumpbackleft.setOutline("black")
    pumpbackleft.draw(card)

    pumpbackright=Oval(Point(712,325),Point(837,600))
    pumpbackright.setFill("orange")
    pumpbackright.setOutline("black")
    pumpbackright.draw(card)

     #pumpkin right/left 100wide 250high 50px overlap
    pumpright=Oval(Point(825,350),Point(925,600))
    pumpright.setFill("orange")
    pumpright.setOutline("black")
    pumpright.draw(card)

    pumpleft=Oval(Point(525,350),Point(625,600))
    pumpleft.setFill("orange")
    pumpleft.setOutline("black")
    pumpleft.draw(card)


    #mid right/left 125 wide 275 high with 50pix overlap
    pumpmidright=Oval(Point(750,325),Point(875,600))
    pumpmidright.setFill("orange")
    pumpmidright.setOutline("black")
    pumpmidright.draw(card)

    pumpmidleft=Oval(Point(575,325),Point(700,600))
    pumpmidleft.setFill("orange")
    pumpmidleft.setOutline("black")
    pumpmidleft.draw(card)

   
    #pumpkin center shows over top 150 wide 300 high
    pumpkincent=Oval(Point(650,300),Point(800,600))
    pumpkincent.setFill("orange")
    pumpkincent.setOutline("black")
    pumpkincent.draw(card)
    
    #prompt to make the eyes
    promptback=Rectangle(Point(525,165),Point(925,215))
    promptback.setFill("purple")
    promptback.draw(card)

    prompt1=Text(Point(725,190),"click each point to make 2 triangles for the eyes!")
    prompt1.setFill("light green")
    prompt1.draw(card)

    
    

    #Get points for eye1
    p1=card.getMouse()
    p1.draw(card)
    p2=card.getMouse()
    l1=Line(p1,p2)
    l1.draw(card)
    p3=card.getMouse()
    e1l2=Line(p2,p3)
    e1l2.draw(card)
    e1l3=Line(p1,p3)
    e1l3.draw(card) 
       
    #make eye 2
    p4=card.getMouse()
    p4.draw(card)
    p5=card.getMouse()
    l2=Line(p4,p5)
    l2.draw(card)
    p6=card.getMouse()
    e2l2=Line(p5,p6)
    e2l2.draw(card)
    e2l3=Line(p4,p6)
    e2l3.draw(card)
    

    #Create mouth corners 500-900 on x axis475 on y bottom corners550-850x 550y
    #top of bottom teeth y= bottom of top teeth y=500
    mouth=Polygon(Point(550,475),Point(575,500),Point(625,475),Point(675,500),Point(725,475),Point(775,500),Point(825,475),Point(875,500),Point(900,475),Point(875,550),Point(825,525),Point(775,550),Point(725,525),Point(675,550),Point(625,525),Point(575,550))
    mouth.setFill("yellow")
    mouth.setOutline("black")
    mouth.draw(card)

    #make eye 1 back
    eye1bk=Polygon(p1,p2,p3)
    eye1bk.setFill("yellow")
    eye1bk.draw(card)
    #make eye1 drop out
    eye1drp=Polygon(p1,p2,p3)
    eye1drp.setFill("orange")
    eye1drp.setOutline("black")
    eye1drp.draw(card)
    #make eye 2 hole
    eye2bk=Polygon(p4,p5,p6)
    eye2bk.setFill("yellow")
    eye2bk.draw(card)
    #make eye 2 drop out
    eye2drp=Polygon(p4,p5,p6)
    eye2drp.setFill("Orange")
    eye2drp.setOutline("black")
    eye2drp.draw(card)

    #place witch here!
    #make witch
    #brmstk=Rectangle(Point(100,150), Point(175,160))
    #brmstk.setFill("black")
    #brmstk.draw(card)
    #brstl=Polygon(Point(175,150),Point(225,125),Point(225,195),Point(175,160))
    #brstl.setFill("black")
    #brstl.draw(card)
    #leg=Polygon(Point(133,160),Point(125,180),Point(144,185),Point(130,180),Point(138,160))
    #body=Polygon(Point(128,150),Point(167,150),Point(112,115))
    #brim=Rectangle(Point(84,110),Point(140,114))
    #hat=Polygon(Point(112,75),Point(98,110),Point(126,110))
    #build witch polygon
    witch=Polygon(Point(100,150),Point(100,160),Point(133,160),Point(125,180),Point(144,185),Point(130,180),Point(138,160),Point(175,160),Point(225,195),Point(225,125),Point(175,150),Point(167,150),Point(112,115),Point(140,114),Point(140,110),Point(126,110),Point(112,75),Point(98,110),Point(84,110),Point(84,114),Point(112,115),Point(128,150),Point(100,150))
    witch.setFill("black")
    witch.draw(card)
    #move witch off screen from build location for fly by
    witch.move(2000,95)

    #get points for various polygon construction using mouse inputs
    #print(p1.getX(), p1.getY())
    #print(p2.getX(),p2.getY())
    #print(p3.getX(),p3.getY())
    #print(p4.getX(),p4.getY())
    #print(p5.getX(),p5.getY())
    #print(p6.getX(),p6.getY())     
    

    #remove prompt
    prompt1.undraw()
    promptback.undraw()

    #create flicker variable
    fire=["orange","red","orange","Yellow"]

    #move moon to center top (750,60)x moves 750y moves-415
    #include flash for eye background and eye pieces falling 
    for moonrise in range(83):
        moon.move(9,-5)
        #drop the cut outs
        eye1drp.move(0,5)
        eye2drp.move(0,5)
        #move witch from right side of screen to left
        witch.move(-15,0)
        #time.sleep(.1)
        
        #create eye/mouth flash
        for light in fire:
            eye1bk.setFill(light)
            eye2bk.setFill(light)
            mouth.setFill(light)
            time.sleep(.025)
    #remove eye cutouts.
    eye1drp.undraw()
    eye2drp.undraw()

    print(moon)
    #set moon (1500,475), and continue flicker effect and witch flyby
    for moonset in range(88):
        moon.move(9,5)
        witch.move(-15,0)

        #create eye flash
        for light in fire:
            eye1bk.setFill(light)
            eye2bk.setFill(light)
            mouth.setFill(light)
            time.sleep(.025)

    #Create exit button
    exitbk=Rectangle(Point(620,600),Point(820,700))
    exitbk.setFill("black")
    exitbk.draw(card)
    exit=Text(Point(720,650),"Click to Exit")
    exit.setFill("red")
    exit.setSize(15)
    exit.setStyle("bold")
    exit.draw(card)
       

    
    #close window
    card.getMouse()
    card.close()


def main():
    greet()

main()

