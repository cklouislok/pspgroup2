#Aerial Survey Flight Plan
# date stared: November 25, 2023
#Last Modified: december 01, 2023
#Created by Alison Cooke, for Group 2 section 61 GEOM 67
#this sectino of code is for elevation, photoscale, endlap and sidelap input from the user

#get input from user, must be in meters and within a range o 45 meters and 450 meters becasue that is the 
#elevation numbers taken from this site https://en-ca.topographic-map.com/map-kc957/Canada/?center=44.19894%2C-78.61679&zoom=10&popup=49.55373%2C-49.43848
elevationUnits = input('Please enter elevatio units, M or Ft: ') 

if (elevationUnits.upper() == 'M'): 
    
    elevation = float(input("Please provide ground elevation in a range of 45 m - 1000 m: "))

else: 
    elevationFt = float(input ("what is the elevation in feet? "))
    elevation = elevationFt * 0.3048
   
if elevation >45 and elevation <1000: #figure out why this wont work it jusmps right to give photo scale
        photoScale = int(input("Please give you desired photo scale: ")) #are we asking them for their photo scale or are we making a defined function for that?
        
        endlap = float(input("Please give desired endlap in percent: "))
        if endlap <1 or endlap >100:
                print("endlap invalid")
    
        else: 
                
            sidelap = float(input("Please give desired sidelap in percent: "))
       
            if sidelap <1 or sidelap >100:
              print("Side lap invalid")
            else:
             print ("Run rest of defined programs")
                                     
           
else:
        print("Elevation invalid")



#display at end of Def functions

print("The survey, ", projectTitle)
print ("The survey was done, ", planDate)
print("Surveyors name: ", surveyprName)
print ("Your flight height is: ", flightHeight)
print("The number of Laps made", numberLaps")
print("the total number of pictures taken for this survey: ", total photographs taken) 
#still need to change the variable names so they match the other variables 
