#Author: Josh Hodges
#Date:30Nov23
"""statement of problem: Create method classes to 1) create student with attributes
2)method to read student records form file name<space>score 3)Selction sort will sort students info based on score 4) output sorted file"""
#statement of authenticity:
#layman problem/solution:

#takes the students and scores from text file and creates a list with said info. 
def refFile(filename):
    file=open(filename)
    line=file.readline()
    students=[]
    while (line != "") :
        students.append(line)
        line=file.readline()
    file.close
    return students

#Short function to write the students onto a new file
def writefile(filename, list):
    outfile=open(filename,'w')
    for i in list:
        name=i.getname()
        score=i.getscore()
        print("{0:15} {1:2}".format(name,score), file=outfile)
    outfile.close

#creates the student object class
class Student:
    #Initiates object with name and score.
    def __init__(self, name, score):
       self.name=name
       self.score=score

    #method to get the name of student in object
    def getname(self):
       return self.name

    #method to get score of student in object.
    def getscore(self):
       return self.score
    
def selectionSort(stus):
    n=len(stus)
    for low in range(n-1):
        #becomes the new bottom of the list(0,1,2,3...) 
        m=low
        #starts at beginning of list and compares the numbers starting at pos1
        for i in range(low+1,n):
            #compares pos1 to pos of iteration in parent loop
            if stus[i].getscore()<stus[m].getscore():
                #identifies the position in which one is larger than current position
                m=i
        swap(stus,m,low)

def swap(values, m, low):
    #saves the value at the bottom of the list
    lowerval=values[low]
    #changes value at bottom of list to the next value ie 3,2,5 changes to 2,2,5
    values[low]=values[m]
    #replaces the value of the next one with the saved value 2,3,5
    values[m]=lowerval
