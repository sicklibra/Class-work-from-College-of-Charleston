from graphics import *
import time
def wallchk(ball, win):
    center=ball.getCenter().getX()
    if center>680:
        return True
    else:
        return False

def main():
    test=GraphWin('',700,700)
    ball=Circle(Point(100,100),10)
    ball.draw(test)
    lst=ball.getCenter().getX()

    rock=Rectangle(Point(20,0),Point(0,20))
    rock.draw(test)

    # p1=test.getMouse()
    # rock.move(p1.getX()-10,p1.getY()-10)

    tick=0
    me=True
    while me==True:
       
        ball.move(5,5)
        ballcollide=wallchk(ball,test)
        if ballcollide==True:
            ball.move(-680,-680)
            tick=tick+1
        if tick==3:
            me=False
        time.sleep(.1)


    test.getMouse()
    test.close

main()