#Name:Josh Hodges
#date:16NOV23
#statement of authenticity: I worked on this alone

from random import *
from algorithms import *

    
def tradeAlert():
    tradefile="trades.txt"
    daybysec=readData(tradefile)
    warning(daybysec)

def warning(daybysec):
    n=len(daybysec)
    print(n)
    for i in range(n):
        seconds=int(i+1)
        if daybysec[i]==500:            
            time=seconds
            print(time,"Pay attention")
        elif daybysec[i]>=830:
            time=seconds
            print(time,"Warning!")

def timecalc(seconds):
    mintot=seconds//60
    hours=mintot//60
    minremain=mintot%60
    minutes=minremain//60
    seconds=minremain%60
    time=str(hours)+':'+str(minutes)+":"+str(seconds)
    return time



def main():
    tradeAlert()

main()
