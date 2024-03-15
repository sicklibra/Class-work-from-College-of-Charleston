#Author: Josh Hodges
#Date:
#statement of problem: Create a mad lib
#statement of authenticity: I worked on this alone
#layman problem/solution:The first thing in the main is that i will have to get a user inputed file
"""The program will read the file from the read story function. i will use the read story function to collect the lists of user input words that will be used to construct the mad lib. 
the get words function will generate the word lists and send them back to the read function. the build story function will build the story inserting the new words in place of the trigger characters. and send it to the final function that will write the finished mad lib to a new file designated by the user. """


"""this function is the primary hub for information collection. I will use it to generate
 the lists and send off for final processing."""
def readStory(filename):
    #open file
    infile=open(filename,'r')
    #Read story as a single string
    story=infile.read()
    #because story is now a long string, i can close file.
    infile.close
    #initialize empyt lists for input word
    nouns=[]
    verbs=[]
    adj=[]
    #this loop will take each letter of the file and identify specific characters
    #it will take each special character and put it into its own list for getWords
    for word in story:
        if word=="$":
            nouns.append(word)
        elif word=="^":
            verbs.append(word)
        elif word=="@":
            adj.append(word)
    #change trigger characters into user input words
    nounlst=getWords(nouns, story)
    verblst=getWords(verbs, story)
    adjlst=getWords(adj, story)

    # print(nounlst)
    # print(verblst)
    # print(adjlst)
    #send lists and story string to be built
    buildStory(story,nounlst,verblst,adjlst)
    

def getWords(wordType, Story):
    #get number of words to be prompted
    count= len(wordType)
    #create new list for export
    export=[]
    #for each type of word, it will construct a new list changing the place holders to 
    #user inputed words.
    for i in range (count):
        #$=noun  verbs= “^”, adjectives @
        #the if statements will concentrate the prompts appropriately to the correct part 
        #of the loop.
        if wordType[0]=="$":
            word=input('Please enter a noun:')
            export.append(word)
        elif wordType[0]=="^":
            word=input('Please enter a verb:')
            export.append(word)
        elif wordType[0]=="@":
            word=input('Please enter an adjective:')
            export.append(word)
    #Send out the newly constructed list to read story function
    return(export)


def buildStory(story, nouns, verbs, adjectives):
    #initialize new string for the output story and variables for word placement in the list 
    compstory=""
    verbcounter=0
    adjcounter=0
    nouncounter=0
    #begin loop to concatonate string
    for words in story:
        #when variable characters are encountered.
        #$=noun  verbs= “^”, adjectives @
        if words=="$":
            compstory+= nouns[nouncounter]
            nouncounter+=1
        elif words=="^":
            compstory+= verbs[verbcounter]
            verbcounter+=1
        elif words=="@":
            compstory+=adjectives[adjcounter]
            adjcounter+=1
        else:
            compstory+=words
    #send the finished story to print to file
    outfile=input("What is the name of the file you would like the completed mad lib in?: ")
    printToFile(outfile, compstory)
    
        

def printToFile(filename, story):
    complete=open(filename,"w")
    print(story, file=complete)
    complete.close
    print('Your Mad Lib has been created. Please open',filename,'to view it.')
    print("\nNote the Mad Lib game is a registered trademark. For more information, visit http://www.madlibs.com/history/")


def main():
    #to kick this off, i will need to reference the file name.
    print('This program will take a "Mad Lib" text file and fill in the blanks\n with words provided by you!')
    origfile=input('What "Mad Lib" file would you like to do?')
    #send to the read story function
    complete=readStory(origfile)

main()
