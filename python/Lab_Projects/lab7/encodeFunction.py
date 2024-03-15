# Separate file for encode call from lab7.py

def encode(message,key):
    encodedMsg = ""
    for ch in message:
        encodedMsg += chr(ord(ch)+key)
    return (encodedMsg)

def encodeBetter(message,pad):
    #message = input("Enter a message: ")
    #key = input("Enter your cipher message: ")
    #print (message)
    #print(ord(pad))

    encodedMsg = ""
    for i in range(len(message)):
        encodedMsg = encodedMsg + chr(ord(message[i])+ord(pad[i])-ord("a"))
        
        
    return(str(encodedMsg))

