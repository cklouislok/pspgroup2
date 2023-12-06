import math


# see if it is possible to turn all user input into dictionary
# see if possible to turn formulas into def functions


# Program-defined data input: sensorLength, focalLength

# Define camera sensor length and width (in mm)
# Camera sensor size = 24 mm × 24 mm, which is the maximum 1:1 size of a full frame sensor. 
# Note: a standard 35 mm full frame sensor has dimensions of 36 mm × 24 mm.
sensorLength = 24  #in mm


# Define camera lens focal length (in mm)
# Focal length of camera lens = 152 mm, typically used for aerial photogrammetry suggested by NRCan and USGS. 
# (NRCan source: https://natural-resources.canada.ca/maps-tools-and-publications/satellite-imagery-and-air-photos/tutorial-fundamentals-remote-sensing/satellites-and-sensors/cameras-and-aerial-photography/9351. 
# USGS source: https://www.usgs.gov/faqs/how-much-area-does-aerial-photograph-cover. )
focalLength = 152 #in mm


# Display program's purpose
programPurpose = "This program is developed to resolve the problem of incomplete data collection aerial surveys and \
produce an explicit flight plan for surveyors to follow. It focuses on aerial photogrammetry by Unmanned Aerial \
Vehicles (UAVs), in particular rotary-wing UAVs, in combination with an aircraft-hinged camera. The primary output \
of the program are the aircraft flying height, number of flight lines, minimum number of aerial photographs, \
as well as the start and end coordinates of each flight line, so that users can follow the programmed \
flight plan to accurately survey and measure the terrain."
print(programPurpose)


# Display program limitations
programLimitations = ["The shape of the surveyed area must be a rectangle, square included.", "The diagonal point of the \
surveyed area must have both greate Easting and Northing than the first point"]
print("This program has the following limitations: ")
for limitation in programLimitations:
    print(limitation)


# DISPLAY programmer-defined values of camera sensor length and lens focal length using List
# cameraSettings = [sensor_focal.sensorLength,sensor_focal.focalLength]
print("Programmer-defined sensor length:", sensorLength)
print("focal length:", focalLength)


# GET flight project title, planned survey date, and surveyor’s name
projectTitle = input("Please enter the aerial survey project title: ")
surveyDate = input("Please enter the planned survey date: ")
surveyorName = input("Please enter the name of the surveyor: ")


# GET UTM easting and northing of bottom left corner of the surveyed area
try:
    # Lower left corner of the surveyed area
    UTMBottomLeft = input("Please enter the Easting and Northing of the bottom left corner of the surveyed area \
in UTM format (XXXXXX.XX, YYYYYYY.YY): ")
    UTMTopRight = input("Please enter the Easting and Northing of the top right corner of the surveyed area \
in UTM format (XXXXXX.XX, YYYYYYY.YY): ")

    # Store UTMBottomLeft with Easting and Northing separated in a list
    UTMENBottomLeft = UTMBottomLeft.split(", ")
    UTMENTopRight = UTMTopRight.split(", ")

    # STRING MANIPULATION to store easting and northing of bottom left and top right corners separately
    eastingBottomLeft = float(UTMENBottomLeft[0])
    northingBottomLeft = float(UTMENBottomLeft[1])
    eastingTopRight = float(UTMENTopRight[0])
    northingTopRight = float(UTMENTopRight[1])

    print("Point\t\t\tEasting\t\t\tNorthing")
    print("Bottom Left", " \t\t" + "%.2f" % eastingBottomLeft, " \t\t" + "%.2f" % northingBottomLeft)
    print("Top Right", " \t\t"+  "%.2f" % eastingTopRight, " \t\t" + "%.2f" % northingTopRight)

except (IndexError):
    print("Please re-run this program with and enter Easting and Northing in standard format.")
except (ValueError):
    print("Please re-run this program with and enter numeric values for the Easting and Northing")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Part 2
# Conversion of Ground Area to Width and Length
# Easting difference between the two corners
eastingDiff = eastingTopRight - eastingBottomLeft

# Northing difference between the two corners
northingDiff = northingTopRight - northingBottomLeft

# Check if the given two points form a rectangle (sqaure included). If it is a line, program will be terminated.
if eastingDiff == 0 or northingDiff == 0:
    print("The surveyed area must form either a rectangle or a square. It cannot be a line")

elif eastingDiff < 0 or northingDiff < 0:
    print("The second point shoud be located at a upper right location of the first point")

else:
    # Check the flight direction. Flight lines always run parallel to the larger dimension of the study area.
    if northingDiff > eastingDiff:
        flightDirection = "StoN"
        print("The flight direction will be from South to North")
    elif northingDiff < eastingDiff:
        flightDirection = "WtoE"
        print("The flight direction will be from West to East")
    else:
        print("The flight direction will be from South to North")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
  



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
    # lowest land elevation on Earth is -420 meters, and highest land elevation is +8,848 meters.
    elevation = float(input("Please provide ground elevation in a range from -420 m to +8848 m: "))
    
else: 
    elevationFt = float(input ("What is the elevation in feet? "))
    elevation = elevationFt * 0.3048
   
if elevation < -420 or elevation > 8848: 
    print("Invalid elevation. Please re-run this program with a valid elevation value between -420m and + 8848m, both ends excluded")
else:                             
    scaleRatio = int(input("Please give you desired photo scale in 1 to ___: ")) 
    photoScale = 1 / scaleRatio
    if photoScale > 1 or photoScale < 0:                  # try except
        print("Invalid scale. Please re-run this program with a valid scale between 0 and 1, both ends excluded")
    else:
        endlap = int(input("Please give desired endlap in percent: "))
        if endlap <= 0 or endlap >= 100:
                print("Invalid end lap. Please re-run this program with a valid endlap value between 1 and 100, both ends excluded")
        else: 
            sidelap = int(input("Please give desired sidelap in percent: "))
            if sidelap <= 0 or endlap >= 100:
                print("Invalid side lap. Please re-run this program with a valid endlap value between 1 and 100, both ends excluded")
            else:
                print("Run rest of defined programs")



# #*********************************************************************************************************************************************#

# Calcalate ground area of the surveyed area
surveyAreaSize = northingDiff * eastingDiff

# Calculate ground coverage distance in one dimension and ground coverage area of a single image
# sensorLength is in mm, and imageGroundCoverageLength is in m
imageGroundCoverageLength = (sensorLength / photoScale) / 1000 # meters
imageGroundCoverageArea = imageGroundCoverageLength ** 2 # square meters

print("The ground area coverage of one aerial photo is: " + str(imageGroundCoverageArea) + "sqaure meters")

# Calculate the relative flight height
relFlightHeight = focalLength / photoScale

# Calculate airbase (distance between two successive images along the same Flight Line)
airbase = imageGroundCoverageLength * ((50 + 50 - endlap) / 100)

# Calculate number of photographs required in one flight line
photosOneLine = math.ceil(imageGroundCoverageLength / airbase) + 1

# Calculate flight line spacing: distance between each flight line
flightLineSpacing = imageGroundCoverageLength * ((50 + 50 - sidelap) / 100)

# Calculate total number of flight lines
totalFlightLines = math.ceil(imageGroundCoverageLength / flightLineSpacing)

# Calculate total number of photographs required to cover the entire surveyed area
totalPhotos = photosOneLine * totalFlightLines

# # # # # # 

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





# Calculate relative flight heigth i.e. height above the surveyed area
# Scale = Focal Length / Relative Flight Height
# Ground Sample Distance = (Sensor Width in mm x Relative Flight Height in cm) / (Focal Length in mm x Image Width in pixels) in cm/pixel 
relFlightHeight = (groundSampleDistance * focalLength * imageWidth / sensorLength)



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