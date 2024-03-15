#Author: Josh Hodges
#Date:05OCT23
#statement of problem: I will be creating a program that will contain 4 different functions.
#Function 1 to count the number of characters in a message input by the user.
#function2 will calculate the average and sum of a sequence of numbers in a list.
#function 3 will calculate the number of words and the average word length in a sentence input by user
#function 4 will print a fibonacci sequence formula Fn=Fn-1+ Fn-2
#statement of authenticity:I worked on this alone.

#function 1 
# This program calculates the number of characters in a message input by the user
def strlength():
    #function explanation
    print('This program calculates the number of characters with and without spaces in a message input by you.')  
    print('') 
    #prompt user for input
    msg=input("What message would you like to count?")
    #get my character count
    #initialize v
    v=0
    for i in msg:
        v=v+1

    #create list to get rid of spaces
    msglst=msg.split(' ')

    #initialize variable and for loop
    msgcnt=0
    for c in msglst:
        msgcnt=msgcnt+len(c)

    #output the number of characters in the message. 
    print('Your character count including spaces is:',v)
    print('Your character count without spaces is:',msgcnt)

    #function 2 calculates the average and sum of a list of numbers
def avgsum():
    #The instructions were vague so Im assuming user input is required
    print('This program will calculate the average and sum of a list of numbers input by you.')
    qnt=int(input('How many numbers are we calculating for?: '))

    print('you will get an updated list after each number you enter.')
    #begin the loop to prompt for the number of values to be listed. 
    #initialize empty list.
    lst=[]
    #initialize variables
    addaccum=0
    for i in range(qnt):
        nxt=int(input("Please enter a number to add to the list: "))
        lst.append(nxt)
        print(lst)
       
        #create loop to conduct fuction operations
    for var in lst:
        addaccum=addaccum+var
    
    #calculate average
    avg=addaccum/qnt
    #output statements
    print('Your sum of the list is: ', addaccum)
    print('Your average is: ',round(avg, 2))

#function calculates the word count and average length of the words used.
def wrd():
    print('This program calculates your word count and average word length.')
    string1=input('What is the message you would like to calculate?')
    
    #convert string to list
    lst1=string1.split(" ")

    #acquire word count
    cnt=0
    for i in lst1:
        cnt=cnt+1
        #print(cnt)

    #count characters in each word
    waccum=0
    for l in lst1:
        waccum= waccum+len(l)
        #print (len(l))
        #print(waccum)

    #calculate average word length
    avglen= waccum/cnt

    #output messages
    print('Your word count is ',cnt, "words")
    print('your average word length is ',round(avglen,2),"characters long")


#function calculates the fibonocci sequence out to a number of iterations specified by user.
def fibonacci():
    #prompt for number of items in the sequence to display
    print('this program will show you the fibonacci sequence out to the number of iterations you decide.')
    rnd=int(input('How many values in the sequence would you like to see?: '))
    #by implementing the first two variables i can use the value of f in my for loop to 
    # initialize places that exist in the list. i will have to cut 2 list items off of my
    # final list for an accurate count. 
    fib=[0,1]
    #create loop to calculate the fibonacci sequence and append to list for output

    #initialize variable for calculation
    fseq=0
    for f in range(rnd):
        #print(fib[f])
        fseq=fib[f+1]+fib[f]
        fib.append(fseq)
        
    #ouput, since the loop calculates the list 2 digits ahead, i have to chop the last two digits off of the display for the final output statement. 
    print('The fibonocci sequence out to your specified iterations is:\n',fib[0:-2])

def main():
    strlength()
    avgsum()
    wrd()
    fibonacci()


main()