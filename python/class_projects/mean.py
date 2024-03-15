#Author: Josh Hodges
#Date:10sep23
#statement of problem: This program aims to calculate the arithmatic mean,
#the Root Mean Square, the Harmonic mean, and the Geometric mean of a series
#of values the number and value of which to be input by the user. 

#statement of authenticity: I worked on this project alone

#layman problem/solution:
#calculate different means from the same inputs. 
#step 1: Identify the number of variables to be included in average and assign number
#to variable quant

#step 2: gain variable input through prompts. the inital and final variables will be
#calculated outside of the loop. the loop will repeat quant-2 times to allow for 
#different input prompts for user freindliness

#step 3: run calculations with provided variables and output them rounded to the hundreths decimal.

#equasions needed:
#arithmatic mean- x1+x2+x3.../n
#harmonicMean- n(number of inputs)/the sum of 1/x1+1/x2....
#root mean square- square root(sum of each value of x**2/n)
#geometric mean- (x1*x2*x3...)**1/n

#user inputs: number of values to be averaged, values to be utilized.  
import math
def mean():
    #user input
    quant=int(input("How many variables are to be entered?:"))
    
    #acquire variables
    #initial variable entered.
    var=float(input("What is the first number in your list to be averaged?:"))
    print("")
    #initializing central variables for loop
    midvar=0
    pimidvar=1
    harmidvar=0
    rmsmidvar=0
    #this loop will generate the values of the middle variables as they relate to each equasion
    #ie( arithmatic x+x, harmonic:(1/x)+(1/x), root mean square (x**2/n)+(x**2/n) and geometric(x*x*x))
    for dat in range(quant-2):
        accumvar=float(input("What is the next number?"))

        #arithmatic
        midvar= midvar+accumvar
        
        #geometric
        pimidvar=pimidvar*accumvar

        #harmonic
        harmidvar=round(harmidvar+(1/accumvar),2)

        #root mean square
        rmsmidvar=rmsmidvar+accumvar**2

        print("")

    #The final variables to be used in the final calculation
    lasvar=float(input("What is the final number in your list?"))

    finvar=midvar+var+lasvar #arithmatic final value for equasion

    harlasvar=round((1/var)+harmidvar+(1/lasvar),2)#harmonic final value

    pilasvar=var*pimidvar*lasvar #geometric final value

    rmslasvar=((var**2)+rmsmidvar+(lasvar**2))
    

    #calculations
    #arithmatic mean- x1+x2+x3.../n
    armean=finvar/quant
    # harmonicMean= n(number of inputs)/the sum of 1/x1+1/x2....
    harmean=quant/harlasvar
    #root mean square- square root(sum of each value of x**2/n)
    rms=round(math.sqrt(rmslasvar/quant),2)
    #geometric mean- x1*x2*x3...**1/n
    geomean=round(pilasvar**(1/quant),2)

    #output lines
    print("")
    print("Your arithmatic mean is:",armean)
    print("----------")
    print("Your Harmonic Mean is:", harmean)
    print("----------")
    print("Your Root Mean Square is:", rms)
    print("----------")
    print("Your Geometric mean is:",geomean)


def main():
    mean()

main()
