# File: FlightPlan.py
# Program purpose:  
# Created by: Class 2023 GEOM 67, Section 61, Group 02
# Last modified November 29, 2023
# Inputs: 
# Assumes: 
# Outputs: 
# Inputs are entered with keyboard
# Outputs are displayed on screen and export as a .csv file
# User has a choice of 
#  range 
# User has a choice of 
#  must be between 
# The program includes specific and general exception handlers




import math

### SET sensorLength and focalLength = constant
# Define camera sensor length and width (in mm)
# Camera sensor size = 24 mm × 24 mm, which is the maximum 1:1 size of a full frame sensor. Note: a standard 35 mm full frame sensor has dimensions of 36 mm × 24 mm.
sensorLength = 24

# Define camera lens focal length (in mm)
# Focal length of camera lens = 152 mm, typically used for aerial photogrammetry suggested by NRCan and USGS. (NRCan source: https://natural-resources.canada.ca/maps-tools-and-publications/satellite-imagery-and-air-photos/tutorial-fundamentals-remote-sensing/satellites-and-sensors/cameras-and-aerial-photography/9351. USGS source: https://www.usgs.gov/faqs/how-much-area-does-aerial-photograph-cover. )
focalLength = 152


#FUNCTIONS AND CALCULATIONS 


#write the constants here

#Function to calculate the Length of the surveying area
def  calSurveyedAreaLength(E1,E0):
    EastingDistance= E1 - E0
    return EastingDistance
#Function to calculate the width of the surveying area
def calSurveyedAreaWidth(N1,N0):
    NorthingDistance = N1 - N0 
    return NorthingDistance

def calSurveyedAreaSize(EastingDistance,NorthingDistance):
    AreaOfSurveyedLand = EastingDistance * NorthingDistance
    return AreaOfSurveyedLand
def calImageGroundCoverageLength(PhotoScale):
    ImageGroundCoverageLength = SensorLength/PhotoScale 
    return calImageGroundCoverageLength

def calImageGroundCoveragewidth(PhotoScale):
    ImageGroundCoverageWidth=sensorWidth / PhotoScale
    return ImageGroundCoverageWidth
    

def calImageGroundCoverageArea(ImageGroundCoverageLength):
    ImageGroundCoverageArea = ImageGroundCoverageLength**2 
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
    




     



### DISPLAY program’s purpose
# Display program's purpose
programPurpose = "This program is developed to resolve the problem of incomplete data collection aerial surveys and produce an explicit flight plan for surveyors to follow. It focuses on aerial photogrammetry by Unmanned Aerial Vehicles (UAVs), in particular rotary-wing UAVs, in combination with an aircraft-hinged camera. The primary output of the program are the aircraft flying height, number of flight lines, minimum number of aerial photographs, as well as the start and end coordinates of each flight line, so that users can follow the programmed flight plan to accurately survey and measure the terrain."
print(programPurpose)

### DISPLAY programmer-defined values of camera sensor length and lens focal length using List
# (to be completed)


### DISPLAY a prompt message for input
### GET flight project title, date, and surveyor’s name
projectTitle = input("Please enter the project title: ")
planDate = input("Please enter the flight planning date: ")
surveyorName = input("Please enter the name of the surveyor: ")
# (to be completed)

### DISPLAY a prompt message for input
### GET UTM easting and northing of bottom left corner of the surveyed area
# Lower left corner of the surveyed area
bottomLeftUTM = input("Please enter the Easting and Northing of the bottom left corner of the surveyed are in UTM format (XXXXXX.XX, YYYYYYY.YY): ")

### STRING MANIPULATION to store easting and northing of bottom left corner separately
eastingBottomLeft = int(
northingBottomLeft = int(
# (to be completed)

### DISPLAY a prompt message for input
### GET UTM easting and northing of top right corner of the surveyed area
# Top right corner of the surveyed area
topRightUTM = input("Please enter the Easting and Northing of the top right corner of the surveyed are in UTM format (XXXXXX.XX, YYYYYYY.YY): ")

### STRING MANIPULATION to store easting and northing of top right corner separately
eastingTopRight = int(
northingTopRight = int(
# (to be completed)

# Difference in 

### IF the two given points form a line but not a rectangle or a square THEN
# Check if the given two points form a rectangle



# Conversion of Ground Area to Width and Length
# Longitude difference between the two corners
longDiff = longTopRight - longLowerLeft

# Latitude difference between the two corners
latDiff = latTopRight - latLowerLeft

# Define which of the longitude and latitude difference is the length and width of the area respectively
# If any of them is longer than the other, the survey area will be in the shape of an rectangle; otherwise it is in a square shape
if longDiff > latDiff:
    surveyAreaLength = longDiff
    surveyAreaWidth = latDiff
elif latDiff > longDiff:
    surveyAreaLength = latDiff
    surveyAreaWidth = longDiff
else:
    surveyAreaLength = longDiff
    surveyAreaWidth = latDiff

# Ground area of the surveyed area
surveyAreaSize = surveyAreaLength * surveyAreaWidth

# Equipment specifications
# Obtain the specifications of equipment being used in the aerial survey from the user

# Camera specfications
# Sensor size
sensorLength = float(input("Please enter the length of the camera sensor in milimeters: "))
sensorWidth = float(input("Please enter the width of the camera sensor in milimeters: "))

# Focal length of the lens
focalLength = float(input("Please enter the focal length of the camera lens in milimeters: "))

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
relFlightHeight = (groundSampleDistance * focalLength * imageWidth / sensorWidth)

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
num_flightLines = math.ceil((surveyAreaLength - imageGroundLength_m) / flightLineSpacing) / flightLineSpacing)

