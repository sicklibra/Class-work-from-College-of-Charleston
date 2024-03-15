#Author: Josh Hodges
#Date:12OCT23
#statement of problem: create a program that generates a weighted average for each student in
#a text file and then generates a class average. 
#statement of authenticity:I worked on this alone.
#layman problem/solution:
#I will access a text file that will have student names, weght, grade weight grade
#ie: Billy Brother 20(weight) 89(grade) 30(weight) 94(grade)...
#the formula for the weighted average will be as follws:
#(w1*g1)+(w2*g2)+..../100
#The class average will be (sum of all final grades)/n(number of grades calculated)


def weightedavg():
    #Statement of purpouse
    print('This program calculates the average scores from a weighted average format text file.\n It will then calculate the class average based on the results')
    
    #access file via prompt
    fname=input("What file do you need to access?:")
    infile=open(fname,"r")
    
    #create loop that will access each line in the file and then conduct calculations
    #Empty list for final average
    finavg=[]
    for line in infile.readlines():
        #split everything in the line based on spaces
        lstline=line.split(' ')
        #line must contain space at the end to avoid line break then isolate numbers under
        #the assumption that the name is a first and last name separated by a space.
        values=lstline[2:]
        #print (values)
        
        #create variables for iteration for average
        #variable for counter to limit loop
        gradecnt=int(len(values)/2)
        #accumulating variable for total from loop
        wtdscraccum=0
        #variable to maintain reference position in list
        counter=0
        #use loop to calculate the total for grade and weight grades of students
        for i in range(gradecnt):
            #accumulate grade/wt totals based on list position
            wtdscraccum=wtdscraccum+(int(values[counter])*int(values[counter+1]))
            counter=counter+2


        #take accumulation from previous loop and apply for total grade
        grade=float(round(wtdscraccum/100,2))
        print(str(lstline[0]),str(lstline[1])+"'s average is:",round(grade,2))
        #add value to list of final grades to be evaluated for class total
        finavg.append(grade)
        


    avg=finalAvg(finavg)
    #close the file
    infile.close()


    #output statements

    print('\nClass average: ', avg)

def finalAvg(finavg):
    #print(inlist)
    #get the number of iterations based on the number of values sent in the incoming list
    qnt=len(finavg)
    #initialize accumulating variable for sum total
    sumgrades=0
    #run loop to generate total sum based on incoming list
    for i in range(qnt):
        sumgrades=sumgrades+float(finavg[i])
       # print(sumgrades)
    #calculate average and assign to variable for return
    average=sumgrades/qnt
    #send variable back to main function
    return average

def main():
    weightedavg()

main()