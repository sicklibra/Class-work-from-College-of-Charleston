#Author: Josh Hodges
#Date: 05SEP23
#Statement of problem: This Program aims to provide volume and surface area of
                    #provided number of Prisms and cylinders Given the necessary
                    #information provided by the user.
#statement of Authenticity: I worked on this alone.
#Required information for prism: pb=length of any side of base provided  base is square
                                #ph= height of the prism pq=prism quantity
#Required information for cylinder: ch= height cr= radius of the cylinder cq=cylinder quantity.
#The program will prompt for all required information before running the calculations.
#Once inputs received, program will calculate and display volume, surface area, and totals for the quantity of specified shapes. 
import math

def volsa():
# opening statement
    print("For accuracy when calculating the volume and surface area of a prism,")
    print("the prism must have a square bottom.")
    print("")
    print("")

#prism function
def prism():
   #prism info query
    print("Lets start with the Prism you wish to calculate for.")
    print("If you do not wish to calculate for a shape, enter 0 for prompts")
    pb=float(input("What is the length of one side of the prism's square base? : "))
    ph=float(input("What is the prism's height? : "))
    pq=int(input("How many prisms do you wish to calculate for? : "))

    #calculate Volume
    pv=pb**2*ph
    #calculate surface area
    psa=4*pb*ph+2*pb**2

    #calculate totals (loops)
    pvt=0
    psat=0

    for tpv in range(pq):
        pvt=pvt+pv
    for tpsa in range(pq):
       psat=psat+psa

    #output statements
    print("")
    print("The volume of each prism is ", pv, "units.")
    print("The surface area of each prism is ", psa, "units.")
    print("Your total pirsm volume is ", pvt, "units.")
    print("Your total prism surface area is ", psat, "units.")
    print("")
#cylinder function
def cylinder():
     #cylinder info
    print("Now let's gather information on the cylinder!")
    cr=float(input("What is the cylinder's radius? If you have the diameter, divide by 2 for radius. : "))
    ch=float(input("What is the height of the cylinder? : "))
    cq=int(input("How many cylinders do you wish to calculate for? : "))

    #calculate Volume
    cv=math.pi*cr**2*ch

    #calculate surface area
    csa=2*math.pi*cr**2+2*3.14*cr*ch

    #loops
    cvt=0
    csat=0
    for tcv in range(cq):
       cvt=cvt+cv
    for tcsa in range(cq):
        csat=csat+csa
          

    #output
    print("")
    print("")
    print("The volume of each cylinder is ", round(cv, 2), "units.")
    print("The surface area of each cylinderis ", round(csa, 2) ,"units.")
    print("Your total cylinder volume is ", round(cvt, 2), "units.")
    print("Your total cylinder surface area is ", round(csat, 2), "units.")

def main():
    volsa()
    prism()
    cylinder()
    
main()
