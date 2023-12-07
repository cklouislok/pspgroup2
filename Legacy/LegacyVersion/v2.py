# # # import starts here # # #
import math
# # # import ends here # # #

# # # Preset constants starts here # # # 
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


# # # Preset constants ends here # # #

# # # Preset messages starts here # # # 
programPurpose = "This program is developed to resolve the problem of incomplete data collection aerial surveys and \
produce an explicit flight plan for surveyors to follow. It focuses on aerial photogrammetry by Unmanned Aerial \
Vehicles (UAVs), in particular rotary-wing UAVs, in combination with an aircraft-hinged camera. The primary output \
of the program are the aircraft flying height, number of flight lines, minimum number of aerial photographs, \
as well as the start and end coordinates of each flight line, so that users can follow the programmed \
flight plan to accurately survey and measure the terrain."

programLimitations = ["The shape of the surveyed area must be a rectangle, square included.", "The diagonal point of the \
surveyed area must have both greate Easting and Northing than the first point"]


# # # Preset messages ends here # # #

# # # def functions starts here # # #
# Calcalate Easting and Northing of the two diagonal points of the surveyed area provided by user.
def UTMSurveyArea(utmLowerLeft, utmUpperRight):
    try:
        # STORE UTMBottomLeft with Easting and Northing separated in a list
        utmLowerLeft = utmLowerLeft.split(", ")
        utmUpperRight = utmUpperRight.split(", ")
        # STRING MANIPULATION to store easting and northing of bottom left and top right corners separately
        eastingLowerLeft = float(utmLowerLeft[0])
        northingLowerLeft = float(utmLowerLeft[1])
        eastingUpperRight = float(utmUpperRight[0])
        northingUpperRight = float(utmUpperRight[1])
        # DISPLAY the coordinates in table form
        print("Point\t\t\tEasting\t\t\tNorthing")
        print("Bottom Left", " \t\t" + "%.2f" % eastingLowerLeft, " \t\t" + "%.2f" % northingLowerLeft)
        print("Top Right", " \t\t"+  "%.2f" % eastingUpperRight, " \t\t" + "%.2f" % northingUpperRight)
    except IndexError:
        print("Please re-run this program with and enter Easting and Northing in standard format.")
    except ValueError:
        print("Please re-run this program with and enter numeric values for the Easting and Northing")
    return eastingLowerLeft, northingLowerLeft, eastingUpperRight, northingUpperRight

# Calculate the dimensions and size of the surveyed area
def calculateSurveyArea(eastingUpperRight, eastingLowerLeft, northingUpperRight, northingLowerLeft):
    # Conversion of Ground Area to Width and Length
    # Easting difference between the two corners
    eastingDiff = eastingUpperRight - eastingLowerLeft
    # Northing difference between the two corners
    northingDiff = northingUpperRight - northingLowerLeft
    # Size of surveyed area
    surveySize = eastingDiff * northingDiff
    return eastingDiff, northingDiff, surveySize

# Calculate the ground coverage distance and area of one signle photograph
def imageGroundCover(sensorDimension, imageScale):
    # Calculate ground coverage distance in one dimension and ground coverage area of a single image
    # sensorLength is in mm, and imageGroundCoverageLength is in m
    imageGroundCoverLength = (sensorDimension / imageScale) / 1000 # meters
    imageGroundCoverSize = imageGroundCoverLength ** 2 # square meters
    return imageGroundCoverLength, imageGroundCoverSize

# Calculate flight height both relative to ground elevation and mean sea level
def flightHeight(focusDimension, imageScale, groundElevation):
    relAltitude = (focusDimension / imageScale) / 1000
    geoAltitude = relAltitude + groundElevation
    return relAltitude, geoAltitude

# Calculate the gap between centers of two successive images along one flight line, and gap between centers between two 
# neighboring flight lines.
# Airbase is image gap; Flight line spacing is flight line gap
def flightGaps(imageGroundCoverLength, ENDlap, SIDElap):
    imageGap = imageGroundCoverLength * ((50 + 50 - ENDlap) / 100)
    flightLineGap = imageGroundCoverLength * ((50 + 50 - SIDElap) / 100)
    return imageGap, flightLineGap

# Calculate the number of flight lines needed to cover the entire surveyed area, number of photographs required for one 
# flight line, and for the entire surveted area.
def flightLinesAndPhotos(surveyAreaShort, flightLineGap, surveyAreaLong, imageGap):
    flightLinesTotal = math.ceil(surveyAreaShort / flightLineGap) + 1
    photosNo = math.ceil(surveyAreaLong / imageGap) + 1
    totalPhotos = flightLinesTotal * photosNo
    return flightLinesTotal, photosNo, totalPhotos



# # # def functions ends here # # #

# see if it is possible to turn all user input into dictionary
# see if possible to turn formulas into def functions



# # # Main program starts here # # #
# Display program's purpose
print(programPurpose)

# DISPLAY program limitations
print("This program has the following limitations: ")
for limitation in programLimitations:
    print(limitation)

# DISPLAY programmer-defined values of camera sensor length and lens focal length
print("Programmer-defined sensor length:", sensorLength)
print("focal length:", focalLength)

# GET flight project title, planned survey date, and surveyor’s name
projectTitle = input("Please enter the aerial survey project title: ")
surveyDate = input("Please enter the planned survey date: ")
surveyorName = input("Please enter the name of the surveyor: ")

# # # OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK # # #
# GET UTM easting and northing of bottom left corner of the surveyed area
# Bottom left corner of the surveyed area
UTMBottomLeft = input("Please enter the Easting and Northing of the bottom left corner of the surveyed area \
in UTM format (XXXXXX.XX, YYYYYYY.YY): ")
# Top right corner of the surveyed area
UTMTopRight = input("Please enter the Easting and Northing of the top right corner of the surveyed area \
in UTM format (XXXXXX.XX, YYYYYYY.YY): ")

# Calculate and separate the coordinates in easting and northing usin the UTMSurveyArea function.
pointUTMList = UTMSurveyArea(UTMBottomLeft, UTMTopRight)
eastingBottomLeft = pointUTMList[0]
northingBottomLeft = pointUTMList[1]
eastingTopRight = pointUTMList[2]
northingTopRight = pointUTMList[3]
# print(eastingBottomLeft)
# print(northingBottomLeft)
# print(eastingTopRight)
# print(northingTopRight)
# # # OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK # # #

# # # OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK # # #
# Part 2
# Calculate the dimensions and size of the surveyed area using the calculateSurveyArea function.
areaDistList = calculateSurveyArea(eastingTopRight, eastingBottomLeft, northingTopRight, northingBottomLeft)
eastingDist = areaDistList[0]
northingDist = areaDistList[1]
surveyArea = areaDistList[2]

# Check shape, point locations, and flight direction.
# Check if the given two points form a rectangle (sqaure included). If it is a line, program will be terminated.
if surveyArea == 0:
    print("The surveyed area must either be a rectangle or a square. It cannot be a line.")
# Check if the second top is at a upper right location of the first point. If not, program will be terminated.
elif eastingDist < 0 or northingDist < 0:
    print("The second point shoud be located at a upper right location of the first point.")
else:
    # Check the flight direction. Flight lines always run parallel to the larger dimension of the study area.
    if northingDist > eastingDist:
        flightDirection = "StoN"
        surveyAreaWidth = eastingDist
        surveyAreaLength = northingDist
        print("The flight direction will be from South to North")
    elif northingDist < eastingDist:
        flightDirection = "WtoE"
        surveyAreaWidth = northingDist
        surveyAreaLength = eastingDist
        print("The flight direction will be from West to East")
    else:
        flightDirection = "StoN"
        surveyAreaWidth = eastingDist
        surveyAreaLength = northingDist
        print("The flight direction will be from South to North")
# # # OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK # # #

  


# # # OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK # # #
# #*********************************************************************************************************************************************#
# #Aerial Survey Flight Plan
# # date stared: November 25, 2023
# #Last Modified: december 05, 2023
# #Created by Alison Cooke, for Group 2 section 61 GEOM 67
# #this section of code is for elevation, photoscale, endlap and sidelap input from the user

# GET input from user on ground elevation of the surveyed area.
elevationUnits = input('Please enter elevation units, M for meter or Ft for feet: ') 

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
# # #*********************************************************************************************************************************************#
# # # OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK # # #

# # # OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK # # #
# Calculate the ground coverage distance and area of one signle photograph using the imageGroundCover function.
imageGroundCoverList = imageGroundCover(sensorLength, photoScale)
imageGroundCoverDistance = imageGroundCoverList[0]
imageGroundCoverArea = imageGroundCoverList[1]
print("The ground area coverage of one aerial photo is: " + str("%.2f" % imageGroundCoverArea) + " sqaure meters")

# Calculate flight height both relative to ground elevation and mean sea level using the flightHeight function
flightHeightList = flightHeight(focalLength, photoScale, elevation)
relFlightHeight = flightHeightList[0]
geoFlightHeight = flightHeightList[1]
print(relFlightHeight)
print(geoFlightHeight)

# Calculate the gap between centers of two successive images along one flight line, and gap between centers between two 
# neighboring flight lines using the flightGaps function.
flightGapsList = flightGaps(imageGroundCoverDistance, endlap, sidelap)
airbase = flightGapsList[0]
flightLineSpacing = flightGapsList[1]
print(airbase)
print(flightLineSpacing)

# Calculate the number of flight lines needed to cover the entire surveyed area, number of photographs required for one 
# flight line, and for the entire surveted area using the flightLinesAndPhotos function.
flightLinesPhotosList = flightLinesAndPhotos(surveyAreaWidth, flightLineSpacing, surveyAreaLength, airbase)
totalFlightLines = flightLinesPhotosList[0]
photosPerLine = flightLinesPhotosList[1]
totalPhotos = flightLinesPhotosList[2]
print(totalFlightLines)
print(photosPerLine)
print(totalPhotos)
# # # OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK # # #

# # #*************************************************************************************************************************#
# # date stared: November 25, 2023
# #Last Modified: december 05, 2023
# #Created by Alison Cooke, for Group 2 section 61 GEOM 67
#display at end of Def functions

print("The survey, ", projectTitle)
print("The survey was done on, ", surveyDate)
print("Surveyors name: ", surveyorName)
#displaying the name date and title of the survey before the resulting height, number of photos and number of laps
print ("Your flight height is: ", geoFlightHeight)
print ("The number of lines made", totalFlightLines) #is this number of lines or number of laps taken?
print ("the total number of pictures taken for this survey: ", totalPhotos) 
#still need to change the variable names so they match the other variables 
# # #******************************************************************************************************************************#

