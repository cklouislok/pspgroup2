import math

### SET sensorLength and focalLength = constant
# Define camera sensor length and width (in mm)
# Camera sensor size = 24 mm × 24 mm, which is the maximum 1:1 size of a full frame sensor. Note: a standard 35 mm full frame sensor has dimensions of 36 mm × 24 mm.
sensorLength = 24  #in mm
# Define camera lens focal length (in mm)
# Focal length of camera lens = 152 mm, typically used for aerial photogrammetry suggested by NRCan and USGS. (NRCan source: https://natural-resources.canada.ca/maps-tools-and-publications/satellite-imagery-and-air-photos/tutorial-fundamentals-remote-sensing/satellites-and-sensors/cameras-and-aerial-photography/9351. USGS source: https://www.usgs.gov/faqs/how-much-area-does-aerial-photograph-cover. )
focalLength = 152 #in mm
# def(sensor_focal):                                                #remove
#     sensor_focal.sensorlength=sensor_focal.sensorLength           #remove
#     sensor_focal.focallength=sensor_focal.focalLength             #remove

# ### DISPLAY program’s purpose
# # Display program's purpose
programPurpose = "This program is developed to resolve the problem of incomplete data collection aerial surveys and produce an explicit flight plan for surveyors to follow. \
 It focuses on aerial photogrammetry by Unmanned Aerial Vehicles (UAVs), in particular rotary-wing UAVs, in combination with an aircraft-hinged camera. The primary output \
 of the program are the aircraft flying height, number of flight lines, minimum number of aerial photographs, as well as the start and end coordinates of each flight line, \
 so that users can follow the programmed flight plan to accurately survey and measure the terrain."
print(programPurpose)

### DISPLAY programmer-defined values of camera sensor length and lens focal length using List
# cameraSettings = [sensor_focal.sensorLength,sensor_focal.focalLength]
print("Programmer-defined sensor length:", sensorLength)
print("focal length:", focalLength)

### DISPLAY a prompt message for input
### GET flight project title, date, and surveyor’s name
projectTitle = input("Please enter the project title: ")
surveyDate = input("Please enter the survey date: ")
surveyorName = input("Please enter the name of the surveyor: ")

### DISPLAY a prompt message for input
### GET UTM easting and northing of bottom left corner of the surveyed area
# Lower left corner of the surveyed area
bottomLeftUTM = input("Please enter the Easting and Northing of the bottom left corner of the surveyed are in UTM format (XXXXXX.XX, YYYYYYY.YY): ")
# eastingString, northingString = str[[start][:][end]]          #remove

### STRING MANIPULATION to store easting and northing of bottom left corner separately
eastingLeft = float(bottomLeftUTM[0:9])
northingLeft = float(bottomLeftUTM[11:len(bottomLeftUTM)])

# eastingString[[start][:][end]]                     #remove
# northingLeft = northingString[[start][:][end]]     #remove

print("The Easting of the bottom left corner =", eastingLeft)
print("The Northing of the bottom left corner = ", northingLeft)

### DISPLAY a prompt message for input
### GET UTM easting and northing of top right corner of the surveyed area
# Top right corner of the surveyed area
topRightUTM = input("Please enter the Easting and Northing of the top right corner of the surveyed are in UTM format (XXXXXX.XX, YYYYYYY.YY): ")
# eastingString, northingString = str[[start] [:] [end]]      #remove

### STRING MANIPULATION to store easting and northing of top right corner separately
eastingRight = float(topRightUTM[0:9])
northingRight = float(topRightUTM[11:len(topRightUTM)])

# eastingString[[start][:][end]]                    #remove
# northingRight=northingString[[start][:][end]]     #remove

print("The easting of the bottom right corner =", eastingRight)
print("The northing of the bottom r corner= ", northingRight)


# Part 2
# Conversion of Ground Area to Width and Length
# Longitude difference between the two corners
eastingDiff = eastingRight - eastingLeft

# Latitude difference between the two corners
northingDiff = northingRight - northingLeft

if eastingDiff == 0 or northingDiff == 0:
    print("The surveyed area must form either a rectangle or a square. It cannot be a line")

elif eastingDiff < 0 or northingDiff < 0:
    print("The second point shoud be located at the upper right of the first point")

else:
    # Assuming northing_distance and easting_distance are defined earlier in the program
    if northingDiff > eastingDiff:
        flightDirection = "StoN"
        print("The flight direction will be from South to North")
    elif northingDiff < eastingDiff:
        flightDirection = "WtoE"
        print("The flight direction will be from West to East")
    else:
        print("The flight direction will be from South to North")














    

def calImageGroundCoverageArea(ImageGroundCoverageLength):
     
    return ImageGroundCoverageArea
# Flying Height relative to ground elevation = Focal Length of camera ÷ Photo Scale 

# Flying Height relative to mean sea level = Flying Height relative to ground elevation + Ground

def calFlightHeight(PhotoScale):
    FlightHeightRelativeToGroundElevation=focalLength/PhotoScale
    FlightHeightRelativeToMeanSeaLevel=FlightHeightRelativeToGroundElevation+Groundelevation
    return FlightHeightRelativeToGroundElevation

def  calAirbase(ImageGroundCoverageLength,endLap):
    Airbase=ImageGroundCoverageLength*((50+50-PercentageOfendLap)/100)
    
    return Airbase


def calNoOfPhotoIn1FlightLine(surveyAreaLength,Airbase):
    NoOfPhotoIn1FlightLine=round((surveyAreaLength/Airbase)+1)
    return NoOfPhotoIn1FlightLine

def calFlightLineSpacing():
 FlightLineSpacing=ImageGroundCoverageWidth * ((50 + 50 - PercentageOfSideLap) / 100)
 return flightLineSpacing

def calNoOfFlightLines(surveyAreaWidth,flightLineSpacing):
    NoOfFlightLines=Round((SurveyedAreaWidth / FlightLineSpacing) + 1 )
    return NoOfFlightLines


def calTotalNoOfPhoto(NoOfPhotoIn1FlightLine,calNoOfFlightLines):
   TotalNoOfPhoto=NoOfPhotoIn1FlightLine*NoOfFlightLines
   return TotalNoOfPhoto

def calStartEndCoordinates():





# Difference in 

### IF the two given points form a line but not a rectangle or a square THEN
# Check if the given two points form a rectangle



# Ground area of the surveyed area
surveyAreaSize = northingDiff * eastingDiff

# Image size
imageLength = int(input("Please enter the number of horizontal pixels of the image: "))
imageWidth = int(input("Please enter the number of vertical pixels of the image: "))

# Ground Sample Distance i.e. resolution, the ground distance the one pixel in the image represents
groundSampleDistance = int(input("Please enter the desired resolution of the aerial photographs in cm/px: "))
# groundSampleDistance = (sensorWidth * relFlightHeight) / (focalLength * imageWidth)
# groundSampleDistance2 = (sensorLength * relFlightHeight) / (focalLength * imageLength)

# Calculate relative flight heigth i.e. height above the surveyed area
# Scale = Focal Length / Relative Flight Height
# Ground Sample Distance = (Sensor Width in mm x Relative Flight Height in cm) / (Focal Length in mm x Image Width in pixels) in cm/pixel 
relFlightHeight = (groundSampleDistance * focalLength * imageWidth / sensorLength)

#*********************************************************************************************************************************************#
# #Aerial Survey Flight Plan
# # date stared: November 25, 2023
# #Last Modified: december 05, 2023
# #Created by Alison Cooke, for Group 2 section 61 GEOM 67
# #this section of code is for elevation, photoscale, endlap and sidelap input from the user

#get input from user, must be in meters and within a range o 45 meters and 450 meters becasue that is the 
#elevation numbers taken from this site https://en-ca.topographic-map.com/map-kc957/Canada/?center=44.19894%2C-78.61679&zoom=10&popup=49.55373%2C-49.43848
elevationUnits = input('Please enter elevatio units, M or Ft: ') 

if (elevationUnits.upper() == 'M'): 
    elevation = float(input("Please provide ground elevation in a range of 45 m - 1000 m: "))

else: 
    elevationFt = float(input ("what is the elevation in feet? "))
    elevation = elevationFt * 0.3048
   
if elevation >= -420 and elevation <= 8848:                               # lowest land elevation on Earth is -420 meters, and highest land elevation is +8,848 meters 
    scaleRatio = float(input("Please give you desired photo scale in 1 to ___: ")) 
    photoScale = 1 / scaleRatio
    if photoScale > 1 or photoScale < 0:                  # try except
         print("End")
    else:
        endlap = int(input("Please give desired endlap in percent: "))
        if endlap < 1 or endlap >= 100:
                print("endlap invalid")

        else: 
            sidelap = int(input("Please give desired sidelap in percent: "))

            if sidelap < 1 or sidelap >= 100:
                print("Side lap invalid")
            else:
                print ("Run rest of defined programs")
else:
        print("Elevation invalid")


#*********************************************************************************************************************************************#

imageGroundCoverageLength = sensorLength / photoScale 
imageGroundCoverageArea = imageGroundCoverageLength ** 2




# Calculate scale
scale = focalLength / relFlightHeight

# Percentage of side lap
sideLap = int("Please enter the percentage of side lap: ")
endLap = int("Please enter the percentage of end lap: ")

# Calculate ground area coverage of a single photograph
imageGroundLength_mm = sensorLength / scale
imageGroundLength_m = imageGroundLength_mm * 1000
imageGroundWidth_mm = sensorWidth / scale
imageGroundWidth_m = imageGroundWidth_mm * 1000
imageGroundAreaCoverage_m2 = imageGroundLength_m * imageGroundWidth_m
print("The ground area coverage of one aerial photo is: " + str(imageGroundAreaCoverage_m2) + "sqaure meters")

# Flight line spacing: distance between each flight line
flightLineSpacing = imageGroundLength_m * ((50 + 50 - sideLap) / 100)

# Number of flight lines
num_flightLines = math.ceil((surveyAreaLength - imageGroundLength_m) / flightLineSpacing) / (flightLineSpacing)

# #*************************************************************************************************************************#
# # # date stared: November 25, 2023
# # #Last Modified: december 05, 2023
# # #Created by Alison Cooke, for Group 2 section 61 GEOM 67
# #display at end of Def functions

# print("The survey, ", projectTitle)
# print ("The survey was done, ", surveyDate)
# print("Surveyors name: ", surveyorName)
# #displaying the name date and title of the survey before the resulting height, number of photos and number of laps
# print ("Your flight height is: ", fcalFlightHeight)
# print ("The number of Laps made", numberLaps) #is this number of lines or number of laps taken?
# print ("the total number of pictures taken for this survey: ", totalphotographstaken) 
# #still need to change the variable names so they match the other variables 
# #******************************************************************************************************************************#