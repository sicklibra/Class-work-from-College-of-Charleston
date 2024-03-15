# Lab5.py
# Name 1:Josh Hodges 
# Name 2: Tyler Martin
# Name 3 Bryson Fant

def nameReverse():    
    #Read a name in first-last order and display it in last-comma-first order.
    names=input("Enter your name firstname then last name.")
    #make name into list
    fstlst=names.split(" ")
    #output names in reversed order
    print('Name: '+fstlst[1]+", "+fstlst[0])

def companyName():
    site=input('enter the web address for the company.:')
    name=site.split(".")
    print("The company name is:"+ name[1])

def names():
    namesin=input('Enter first and last names with each individual seaparated by commas.:')
    #specicifically created for count of names for consolidation loop. 
    nametot= namesin.split(',')
    #divide nanmes into first and last individually
    namesplt=namesin.split(" ")
   # print(namesplt)

    initial=[]
    pos=0
    for i in namesplt:
        name= namesplt[pos]
        initial.append(name[0])
        pos=pos+1
        #print(initial)

    initials=""
    pos=0
    #Consolidate list of letters into pairs
    for i in nametot:
        initials = initials + (initial[pos]+"."+initial[pos+1]+", ")
        pos=pos+2
    output = initials.upper()

    #output for initials
    print("The initials of your names are: \n " ,output)

def piglatin():
    #getting the input sentence
    message= input("Enter Your Sentence: ")
    #splitting sentence for spaces
    sentence = message.split(" ")
    #print(sentence)
    #initializing empety latin as a string
    latin = ""
    for i in sentence:
        #getting the correct letters then adding ay
        word = str(i[1:-1]+i[0]+"ay")
        #adding to the latin string
        latin+=word+ " "
    #making latin lower case
    output = latin.casefold()
    #print
    print("Your Sentence in Pig Lain is:", output)





def thirds():
    #print the third character of each word in a scentence
    print('this program prints every three characters of your message.')
    msg=input('enter your message here: ')
    #generate empty list for individual letters
    letters=[]
    #create pos variable to reference position of letter to be used
    pos=0
    for i in msg:
        letters.append(msg[pos])
        pos=pos+1


    #final code empty list
    code=""
    #generate counter for next loop
    iteration=int(len(letters)//3)
    #reset pos to desired number
    pos=2
    #generate fial code.
    for i in range(iteration):
        code+=letters[pos]
        pos=pos+3

    print('every three letters reads as follows:\n'+str(code))


def main():
    nameReverse()
    companyName()
    names()
    thirds()
    piglatin()
    


main()
