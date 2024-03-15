# CSCI 220L - Lab 10
#
# Name 1:Josh Hodges
#
# Name 2:Mackenzie Linn
#
import random

def findAndRemove(list, value):
    pos=list.index(value)
    list.insert(pos, "Josh")
    list.pop(pos+1)

def readData(filename):
    infile=open(filename,'r')
    datlst=[]
    line=infile.readline()
    while line !="":
        # datlst.append(line[:-1])
        newlst=line[:-1].split()
        datlst.extend(newlst)
        line=infile.readline()

    # datlst.split(' ')
    return datlst

def foundPosition(searchval, values):
    i=0
    num=values[i]
    while i<=len(values)-1:
        num=int(values[i])
        # print(searchval,i,num)                
        if num==searchval:
            return i 
        i+=1 
        
    return -1

def goodInput():
    cycle=1 
    while cycle==1:
        try:
            num=int(input('Please enter a whole number in the teens or fifties: '))
        except ValueError:
            print('That is not a whole number')
        if (num>9 and num<20)or(num>49 and num<60):
            return num
        elif num<10:
            print("Your number is too low.")
        elif num<50 and num>19:
            print('The number is not a teen or a fifty')
        elif num>59:
            print('Your number is too high!')


def numDigits():
    num=1
    while num>0:
        test=True
        try:
            num=int(input("please enter a number.\nIf you are done entering numbers enter 0 or a negative number")) 
        except ValueError:
            print("That is not a valid number. Please enter a whole number.")
        counter=0
        currentnum=num
        if num>0:
            while currentnum>0:
                currentnum=currentnum//10
                counter+=1
            print(num,'is',counter,'digits long')
        
def hiLowGame():
    target=random.randint(1,100)
    print("You Have 7 guesses to figure out the number between 1 and 100.")
    counter=0
    while counter<7:
        try:
            guess=int(input("What is your guess?"))
        except ValueError:
            print("That is not a valid number. Please enter a whole number.")
        if guess==target:
            print("You Win! in ",counter+1,'guesses')
            return
        elif guess>target:
            print("Too High!")
        elif guess<target:
            print('Too Low!')
        counter+=1
    print('Sorry you loose, the target number was',target)



def main():
    test=[2,5,8,34,61,22,43,17,18,14,6,5]
    cycle=1
    
    while cycle==1:
        print(test)
        try:
            value=int(input("What value would you like to try to replace with your name?: "))
            try:
                pos=test.index(value)
                cycle=2
            except ValueError:
                print('The value you entered is not in the list.')
            
        except ValueError:
            print('that is not a valid number.')
        
            
    findAndRemove(test, value)
    print('Your new list is',test)
    file='dataSorted.txt'
    datlst=readData(file)
    print(datlst)
    while cycle==2:
        try:
            searchval=int(input("What value would you like to find?: "))
            cycle=1
        except ValueError:
            print('That is not a valid number. Please try again.')
    position=foundPosition(searchval, datlst)
    print('Your values position is, ', position)
    gip=goodInput()
    print('Your input',gip, 'Was accepted.')
    numDigits()
    hiLowGame()
    

main()