#Author: Josh Hodges
#Date:30Nov23
"""statement of problem: This will test my classes file via import by creating instance of
student class from student record (txt file) sort them based on scores and write to an output
file."""
#statement of authenticity: I worked on this alone.
"""layman problem/solution: first i will call a function that will read a file line by line.
I will create a loop that uses the student class and pack each line into a
list. I will then take that list, using mod of i and if elif statements create a list with the
scores only and have it adjust the original list in a mirror of what is happening to the scores
only list. """


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

def main():
    print('This program will take students from a database file and sort them\n The format must be Single name<space>score')
    exist=False
    while exist==False:
        file=input('what is the file name you wish to sort?: ')

        #generates the list of students with scores        
        try:
            stulst=refFile(file)  
            exist=True          
        except FileNotFoundError:
            print("I'm sorry, I'm having trouble finding that.")


    #initialize empty list for objects
    outfile=input("What would you like to name the file for the sorted class list?: ")
    stuclaslst=[]
    #create for loop to turn each student to an object
    for i in stulst:
        stuinfo=i.split(" ")
        stu=Student(stuinfo[0], stuinfo[1])
        stuclaslst.append(stu)
    
    #sorts the students order based on scores lowest to highest.
    selectionSort(stuclaslst)

    #writes sorted list to new file.
    writefile(outfile,stuclaslst)
    print('Your sorted file has been created.')



main()
    
