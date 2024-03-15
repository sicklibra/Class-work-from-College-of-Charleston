#Josh Hodges
# Lab 1
# Purpose: Outputs calculated area
# Input: User inputs length and width
# Output: Output message to screen
def rectArea():
   print("Calculates the area of a rectangle.")
   #print()
   
   #User input length and width
   length = float(input("Enter length: "))
   width = float(input("Enter width: "))

   #calculate area
   area = length * width 

   #output results
   print("Area is: " + str(area))


#calculate volume of a rectangle
def calcVolume():
   #user inputs
   l=float(input("What is the length of the base of the object?:"))
   w=float(input("What is the width of the base of the object?:"))
   h=float(input("What is the height of the object?"))
   
   #calculation
   v=l*w*h

   #output
   print("The volume of you rectangular 3d shape is", v, "units cubed")


#calculates the shooting accuracy percentage
def shootingpercentage():
   #user inputs
   tot=int(input("How many total shots were attempted?:"))
   hit=int(input("What is the total number of hoops sunk?:"))

   #Calculations
   perc=(round(hit/tot,4))*100

   #output
   print("Your hit percentage is", perc,"% successful")

#donut shop
def donut():
   #figure out the cost of shipping donuts
   #cost per doz 11.50
   #delivery cost .96 per doz
   #fixed overhead 1.20 per order(once for the whole order)

   #constants
   DOZ=11.5
   DELCO=.96 #per doz
   OVR=1.2 #per order
   
   #user input
   quant=int(input("How many dozens would you like to have delivered?:"))

   #calculation
   tot=DOZ*quant+DELCO*quant+OVR

   #output
   print("Your order will be $",round(tot,2))

#kilometers to miles
def kilometersToMiles():
   #iniput number of Kilometers output number of miles
   km=float(input("Number of kilometers to convert to miles:"))

   #calculation
   mi=km/1.6

   #output
   print(km, "Kilometers is equivalent of", mi, "miles")






def main():
   rectArea()
   calcVolume()
   shootingpercentage()
   donut()
   kilometersToMiles()

   for dodist in range(3):
      donut()
      kilometersToMiles()

main ()
