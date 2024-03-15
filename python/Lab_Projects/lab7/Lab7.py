# CSCI 220L - Lab 7 
#
# Name 1:Josh Hodges
#
#I worked on this project alone.

from encodeFunction import encode
from encodeFunction import encodeBetter


#This function takes the inported isbn number from the main function it then splits the numbers
#into a list to utilize each value independently then multiplies each number by its position
#in the list ie 635243=6*6+3*5+5*4+2*3+4*2+3*1
def calcCheckSum(isbn):
    #Get the length of digits from input
    place=len(isbn)
    #initialize accumulating variable
    accum=0
    #i will act as each string item in the inported string
    try:
        for i in isbn:
        #utilize i(being each character in the string) to build the number
            accum=(place*int(i))+accum
        #utilize a count down from the length
            place=place-1
            #return final checksum number
        return(accum)
    #exception for having a letter or decimal in the number
    except (ValueError):
        print("Please check your number and try again.")

    

def sendMessage(file, friend,):
    #open file
    infile=open(file,'r')
    #create and open new file with imported name
    outfilename=friend+".txt"
    outfile=open(outfilename,'w')
    #process lines to new file
    for i in infile:
        #remove \n
        i=i[:-1]
        print(i, file=outfile)

    print('your file has been processed...enjoy.')
    
    #close files
    infile.close()
    outfile.close()

def sendSafemessage(file,friend,key):
    #open and create necessary files
    infile=open(file,'r')
    outfilename=friend+".txt"
    outfile=open(outfilename,'w')
    #process lines of text
    for i in infile.readlines():
        #remove \n
        i=i[:-1]
        #send line to be encoded
        codeline=encode(i,key)
        #write new file content
        print(codeline, file=outfile)

    print('your file has been processed...enjoy.')
    
    #close files
    infile.close()
    outfile.close()
    
def sendUncrackableMessage(file,friend,pad):
    infile=open(file,'r')
    outfilename=friend+".txt"
    """When attempting to write outfile, an error was occoring that would kick out an
     undefined value and crash the program. So i had to open the file as a utf-8 encoding which will now print to new text file. However, it is irreversable """
    outfile=open(outfilename,'w',encoding="utf-8")
    padfile=open(pad,'r')
    key=padfile.readline()
    #process lines of text
    
    for line in infile.readlines():
        line=line[:-1]
        #send to encoding function
        codeline=encodeBetter(line,key)
        #print content to new file
        print(codeline,file=outfile)
    print('your file has been processed...enjoy.')
    
    #close files
    infile.close()
    outfile.close()
    padfile.close()

"""def encode(message,key):
    encodedMsg = ""
    for ch in message:
        encodedMsg += chr(ord(ch)+key)
    return (encodedMsg)"""


"""def encodeBetter(message,pad):
    #message = input("Enter a message: ")
    #key = input("Enter your cipher message: ")
    #print (message)
    #print(ord(pad))

    encodedMsg = ""
    for i in range(len(message)):
        encodedMsg = encodedMsg + chr(ord(message[i])+ord(pad[i])-ord("a"))
        
        
    return(str(encodedMsg))"""
    

def main():
    print("This first function calculates the checksum number of an ISBN.")
    print("")
    isbn=input("please input the ISBN")
    checksum=calcCheckSum(isbn)
    if checksum !=None:
        print("your checkusm number is",checksum)
    else:
        print("please restart program")

    #message to a friend
    print("Next lets create a message for a freind in a new file.")
    #Gather inputs
    friend=input("What is the name of the frend the file is for?: ")
    file=input("What file would you like to send to said friend?: ")
    #send inputs to function to write new file.
    sendMessage(file, friend)
    
    #begin the coded text file protocol
    print('Now lets encode a message to a friend')
    friend2=input('What is the name of the friend this message is for?: ')
    file2=input('What is the name of the file you wish to encrypt: ')
    #two chances to enter a whole number for key
    try:
        key=int(input('Enter a whole number for your encryption key: '))
    except(ValueError):
        print('that is not a valid key.\n')
        key=int(input('Enter a whole number for your encryption key: '))


    sendSafemessage(file2,friend2,key)

    #execute send uncrackable message.
    print('\nNow lets make this cypher bullet proof!\n')
    friend3=input('What is the name of the friend you want to send the uncrackable message to?: ')
    file3=input('What file would you like to make uncrackable?: ')
    pad=input('what is the name of the file containing the pad key?: ')
    sendUncrackableMessage(file3,friend3,pad)


main()