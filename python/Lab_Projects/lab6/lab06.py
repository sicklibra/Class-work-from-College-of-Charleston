# Lab6.py
# Name 1:Josh Hodges
# Name 2:Joseph Hoover


#main() should be the only file executed when you are checked off for this lab
#thus add code to main() to call any functions you write.
import math
def cipher(msg,key):   
    cipher=""
    for i in msg:
        code=ord(i)
        codechar=chr(code+key)
        cipher=cipher+codechar

    return(cipher)

def encryptFile():
    key = int(input("What whole number key would you like to encrypt the file with?"))
    #Open the file you want to encrypt.
    #read its contents
    infileName = "input.txt"
    infile = open(infileName, 'r')
    #define out file name
    outfileName = "encrypt.txt"
    #open out file
    outfile = open(outfileName, 'w')
    #create a for loop to read each separate character
    cipher = " "
    for line in infile.readlines():
        line = line [0:-1]
        for i in line:
            encrypt = ord(i)
            codecharacter = chr(encrypt + key)
            cipher = cipher + codecharacter
            #print(cipher, file = outfile)
    
    print(cipher)

    #close the file
    infile.close()
    outfile.close()

def encryptBetter():
    #runs the cypher program
    print('This program encodes your message')
    #get input message
    msg=input('What message would you like to encode?')
    #get cipher key
    key=(input("Enter a series of letters without spaces to act as your key"))   
    cipher=""
    counter=0
    for i in msg:
        code=ord(i)
        codechar=chr(code+(ord(key[counter])-97))
        cipher=cipher+codechar
        counter=counter+1

    print(cipher)

def sphereArea(radius):
    #calculate surface
    area=4*math.pi*float(radius)**2
    area=round(area, 2)
    return (area)




def hourlyWages(infileName, outfileName):
    infile=open(infileName,"r")

    outfile=open(outfileName,"w")
    newline=""
    for line in infile.readlines():
        lstline=line.split(" ")

        values=lstline[2:-1]
        newwage=float(lstline[2])+1.65
        tot=newwage*float(lstline[3])
        lstline.append(tot)
        newline=newline+str(lstline)
        print(newline, file=outfile)
        newline=""

    infile.close()
    outfile.close()
        

def main():
    #runs the cypher program
    print('This program encodes your message')
    #get input message
    msg=input('What message would you like to encode?')
    #get cipher key
    key=int(input("Enter a whole number for your cipher key"))
    encrypted=cipher(msg,key)
    print(encrypted)

    encryptFile()
    
    encryptBetter()

    #surface area of a sphere
    print ("Now let's calculate the surface area of a sphere!")
    rad=input('What is the radius of your sphere?')
    print("The surface area of the sphere is", sphereArea(rad),'units squared.')

    #hourly wages
    wageFilein=input("What wage file would you like to access?: ")
    wagefileout=input('what would you like your new file name to be?:')
    hourlyWages(wageFilein,wagefileout)
    print('your file has been processed.')

#main()
encryptBetter()

    
