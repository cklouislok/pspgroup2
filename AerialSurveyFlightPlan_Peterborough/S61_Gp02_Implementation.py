########### Aerial Survey Flight Plan ###########
# Group 2 section 61, GEOM 67 Problem Solviong and Programing
# Date last modified: December 06, 2023
# Authors of application and contribution:
# Chi Kin Lok-
# Alison Cooke- user inputs for elevation, photo scale, end lap and side lap as well as final out put display, comments and editing 
# Athulya Sabu-
# Dennis Kurian-
# AshwinBalaji Srinivasan-
# The purpose of this code is to create a survey flight plan to be follwed by a drone used by a surveyor. 
# This code will be used to create a rectangular survey flight plan.
# Program structure: recieveing input from user, to create a csv file that will be imported into an ArcGIS 
# project to convert the coorindates into points, and export a shapefile containing the flight line end points. 
# Assumptions: it is assumed the camera being used has a set focal length and sensor length, as well is is
# Limitations: must be a rectangualr survey area, with a consistant fleight height and elevation. it is limited to a north to southward direction flight plan, 
# the coordinates must then be diagonal to eachother to confirm it is a rectangular flight plan
# Known Problem 1: Program does not validate the UTM Easting and Northing entered by the user. This could produce unrealistic 
# results for the coordinate output. 
# Known Problem 2: 
# Inputs: Name of survey, name of surveyor, date of survey, UTM zone, Coordinates of bottom left and top right corners, elevation in meters, photo scale, side lap and end lap
# Output: Fleight height, number of photos taken, number of lines in survey, title of survey, date, and surveyors name. the final output it a csv file and exported arcpy coordinates
# Team members implimentation contribution:
# Chi Kin Lok-
# Alison Cooke: Testing output, editing, comments
# Athulya Sabu-
# Dennis Kurian-
# AshwinBalaji Srinivasan-

# # # # # Program Starts Here # # # # #  

# # # # # import starts here # # # # #  
import math
import csv
import arcpy
import os
# # # # # import ends here # # # # #  

# # # # # ArcGIS Pro workspace setup starts here # # # # #  
# Get current working directory
cwd = os.getcwd()


# Set up workspace
myWorkspace = cwd + r"\AerialSurveyFlightPlan.gdb"
arcpy.env.workspace = myWorkspace
# # # # # ArcGIS Pro workspace setup ends here # # # # # 

# # # # # Preset constants starts here # # # # # 
# Program-defined data input: sensorLength, focalLength
# Define camera sensor length and width (in mm)
# Camera sensor size = 24 mm × 24 mm, which is the maximum 1:1 size of a full frame sensor. 
# Note: a standard 35 mm full frame sensor has dimensions of 36 mm × 24 mm.
sensorLength = 24   # in mm

# Define camera lens focal length (in mm)
# Focal length of camera lens = 152 mm, typically used for aerial photogrammetry suggested by NRCan and USGS. 
# (NRCan source: https://natural-resources.canada.ca/maps-tools-and-publications/satellite-imagery-and-air-photos/tutorial-fundamentals-remote-sensing/satellites-and-sensors/cameras-and-aerial-photography/9351. 
# USGS source: https://www.usgs.gov/faqs/how-much-area-does-aerial-photograph-cover. )
focalLength = 152   # in mm
# # # # # Preset constants ends here # # # # # 

# # # # # Preset messages starts here # # # # # 
programPurpose = """This program is developed to produce an explicit flight plan for surveyors to follow.
The final output will be an exported csv file and a shapefile containing the plotted end points of each flight line."""

programLimitations = ["The shape of the surveyed area must be a rectangle, square included.", "The second point of the \
surveyed area must have both a great Easting and Northing than the first point."]
# # # # # Preset messages ends here # # # # # 

# # # # # def functions starts here # # # # # 
# Calcalate Easting and Northing of the two diagonal points of the surveyed area provided by user.
def UTMSurveyArea(utmLowerLeft, utmUpperRight):
    # STORE UTMBottomLeft with Easting and Northing separated in a list
    utmLowerLeft = utmLowerLeft.split(", ")
    utmUpperRight = utmUpperRight.split(", ")
    # STRING MANIPULATION to store easting and northing of bottom left and top right corners separately
    eastingLowerLeft = float(utmLowerLeft[0])
    northingLowerLeft = float(utmLowerLeft[1])
    eastingUpperRight = float(utmUpperRight[0])
    northingUpperRight = float(utmUpperRight[1])
    # DISPLAY the coordinates in table form
    print("*************************************************************************************")
    print("Point\t\t\tEasting\t\t\tNorthing")
    print("Bottom Left", " \t\t" + "%.2f" % eastingLowerLeft, " \t\t" + "%.2f" % northingLowerLeft)
    print("Top Right", " \t\t"+  "%.2f" % eastingUpperRight, " \t\t" + "%.2f" % northingUpperRight)
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
    imageGroundCoverLength = (sensorDimension / imageScale) / 1000      # meters
    imageGroundCoverSize = imageGroundCoverLength ** 2      # square meters
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

# Calculate the UTM coordinates for each end points of the flight lines. Export the coordinates to a CSV file
def outputCoordinates(endPointsTotal, firstEasting, firstNorthing, flightLineGap, flightLineDistance, flightRoute, x_field, y_field):

    # Set up a new CoordinatesData.csv file for exporting the UTM coordinates of each end point
    outputCSV = "CoordinatesData.csv"
    databaseCSV = open(outputCSV, "w", newline="")
    databasewriter = csv.writer(databaseCSV)

    # Set the field (column) names
    field_X = x_field
    field_Y = y_field
    fieldNames = ["Flight Point ID", field_X, field_Y]
    databasewriter.writerow(fieldNames)
 
    # Run a for loop to calculate the Easting and Northing of each end point, and write the result in the 
    # CoordinatesData.csv file
    # endPointID is the id number of of the two ends of the flight lines
    for endPointID in range(endPointsTotal):

        # Create an empty list for each end point to store the respective Easting and Northing
        coordinatesList = []

        # Define flightPoint as the the id of (endPointID + 1) to make the point number to be exported to CSV to 
        # start at 1, instead of 0
        flightPoint = endPointID + 1

        # Determine which function to use given the flight direction
        # flight direction is StoN
        if flightRoute == "StoN":

            # Calculate Easting of an end point
            ptEasting = firstEasting + (((endPointID + 1 + 1) // 2 - 1) * flightLineGap)

            # Calculate Northing of an end point
            # flightEndPointAdjusted is defined to make the formula works with the correct endPointID order
            flightEndPointAdjusted = endPointID + 1
            ptNorthing = firstNorthing + flightLineDistance * (flightEndPointAdjusted // 2 % 2)

            # Append the resulting flightPoint id, respective Easting and Northing, to the empty coordinatesList
            # One flightPoint belongs to one individual list
            coordinatesList.append(flightPoint)
            coordinatesList.append("%.2f" % ptEasting)
            coordinatesList.append("%.2f" % ptNorthing)

            # Write the coordinateList of the current flightPoint to the CoordinatesData.csv file
            databasewriter.writerow(coordinatesList)

        # flight direction is WtoE
        elif flightRoute == "WtoE":

            # Calculate Easting of an end point
            # flightEndPointAdjusted is defined to make the formula works with the correct endPointID order
            flightEndPointAdjusted = endPointID + 1
            ptEasting = firstEasting + flightLineDistance * (flightEndPointAdjusted // 2 % 2)

            # Calculate Northing of an end point
            ptNorthing = firstNorthing + (((endPointID + 1 + 1) // 2 - 1) * flightLineGap)

            # Append the resulting flightPoint id, respective Easting and Northing, to the empty coordinatesList
            # One flightPoint belongs to one individual list
            coordinatesList.append(flightPoint)
            coordinatesList.append(ptEasting)
            coordinatesList.append(ptNorthing)

            # Write the coordinateList of the current flightPoint to the CoordinatesData.csv file
            databasewriter.writerow(coordinatesList)

    # Close the CoordinatesData.csv file after writing all flightPoint information
    databaseCSV.close()

# Define the functions for running the "XY Table to Points" tool on ArcGIS Pro
def PlotEndPoints(Coordinates_Data, Coordinate_System, Points_Output, X_Field, Y_Field):  # Plot End Points

    # Set Geoprocessing environments
    arcpy.env.extent = "DEFAULT"
    # To allow overwriting outputs change overwriteOutput option.
    arcpy.env.overwriteOutput = True

    # Set the z-value of all points to zero to fulfill the requirement of having input for every required and optional
    # parameters for the tool.
    Z_Field = ""

    # Process: XY Table To Point (XY Table To Point) (management)
    arcpy.management.XYTableToPoint(Coordinates_Data, Points_Output, X_Field, Y_Field, Z_Field, Coordinate_System)
# # # # # def functions ends here # # # # # 

# # # # # Main program starts here # # # # # 
try:
    # Display program's purpose
    print("*************************************************************************************")
    print(programPurpose)
    print("*************************************************************************************")
    # DISPLAY program limitations
    print("This program has the following limitations: ")
    for limitation in programLimitations:
        print(limitation)
    # DISPLAY programmer-defined values of camera sensor length and lens focal length
    print("Default camera sensor length (mm): ", sensorLength)
    print("Default lens ocal length (mm): ", focalLength)
    print("*************************************************************************************")

    # GET flight project title, planned survey date, and surveyor’s name
    projectTitle = input("Please enter the aerial survey project title: ")
    surveyDate = input("Please enter the planned survey date: ")
    surveyorName = input("Please enter the name of the surveyor: ")
    print("*************************************************************************************")
    # Get UTM zone number of the surveyed area from user
    UTMzone = input("Please enter the WGS 1984 UTM zone of the surveyed area, e.g. 17N: ")
    UTMZONE = UTMzone.upper()

    # Check if the user entered a valid UTM zone number. The numeric value must be between 1 and 60, and the character must
    # be either N (Northern Hemisphere) or S (Southern Hemisphere). Prompt message to user and terminate program if the UTM
    # zone is invalid.
    zoneNumber = int(UTMZONE[:-1])
    hemisphere = UTMZONE[-1]
    # Record the UTM zone for use in plotting end points at a later section
    if zoneNumber not in range(1, 61) or hemisphere not in "NS":
        print("Invalid UTM zone input. Please re-run program.")
        print("*************************************************************************************")
    else:
        mapProjection = "WGS_1984_UTM_Zone_" + UTMZONE
        print("The surveyed area is located in the", UTMZONE, "UTM zone.")
        print("*************************************************************************************")

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

        # Calculate the dimensions and size of the surveyed area using the calculateSurveyArea function.
        areaDistList = calculateSurveyArea(eastingTopRight, eastingBottomLeft, northingTopRight, northingBottomLeft)
        eastingDist = areaDistList[0]
        northingDist = areaDistList[1]
        surveyArea = areaDistList[2]

        # Check shape, point locations, and flight direction.
        # Check if the given two points form a rectangle (sqaure included). If it is a line, program will be terminated.
        if surveyArea == 0:
            print("The surveyed area must either be a rectangle or a square. It cannot be a line.")
            print("*************************************************************************************")
        # Check if the second top is at a upper right location of the first point. If not, program will be terminated.
        elif eastingDist < 0 or northingDist < 0:
            print("The second point shoud be located at a upper right location of the first point. Please re-run this program.")
            print("*************************************************************************************")
        else:
            # Check the flight direction. Flight lines always run parallel to the larger dimension of the study area.
            if northingDist > eastingDist:
                flightDirection = "StoN"
                surveyAreaWidth = eastingDist
                surveyAreaLength = northingDist
                print("The flight direction will be from South to North")
                print("*************************************************************************************")
            elif northingDist < eastingDist:
                flightDirection = "WtoE"
                surveyAreaWidth = northingDist
                surveyAreaLength = eastingDist
                print("The flight direction will be from West to East")
                print("*************************************************************************************")
            else:
                flightDirection = "StoN"
                surveyAreaWidth = eastingDist
                surveyAreaLength = northingDist
                print("The flight direction will be from South to North")
                print("*************************************************************************************")

        # #this section of code is for elevation, photoscale, endlap and sidelap input from the user

            # GET input from user on ground elevation of the surveyed area.
            elevationUnits = input('Please enter elevation units, M for meter or Ft for feet: ') 
            if (elevationUnits.upper() == 'M'): 
                elevation = float(input("Please provide ground elevation in a range from -420 m to +8848 m: "))
            else: 
                elevationFt = float(input("What is the elevation in feet? "))
                elevation = elevationFt * 0.3048    #change elevation to meters if user enters feet 
            # lowest land elevation on Earth is -420 meters, and highest land elevation is +8,848 meters.
            if elevation < -420 or elevation > 8848: 
                print("Invalid elevation.")
                print("Please re-run this program with a valid elevation value between -420m and +8848m, both ends inclusive")
                print("*************************************************************************************")
            else:                             
                scaleRatio = int(input("Please give you desired photo scale in 1 to ___ (whole number): ")) 
                photoScale = 1 / scaleRatio
                if photoScale > 1 or photoScale <= 0:                  
                    print("Invalid input. Please re-run this program with a valid scale ratio.")
                    print("The acceptable resulting scale ranges from 0 to 1, both ends exclusive.")
                    print("*************************************************************************************")
                else:
                    endlap = int(input("Please give desired endlap in percent (whole number): "))
                    if endlap <= 0 or endlap >= 100:
                            print("Invalid end lap.")
                            print("Please re-run this program with a valid end lap value between 0 and 100, both ends exclusive.")
                            print("*************************************************************************************")
                    else: 
                        sidelap = int(input("Please give desired sidelap in percent (whole number): "))
                        if sidelap <= 0 or sidelap >= 100:
                            print("Invalid side lap.")
                            print("Please re-run this program with a valid side lap value between 0 and 100, both ends exclusive.")
                            print("*************************************************************************************")
                        else:
                            print("*************************************************************************************")
                            # Calculate the ground coverage distance and area of one signle photograph using the imageGroundCover function.
                            imageGroundCoverList = imageGroundCover(sensorLength, photoScale)
                            imageGroundCoverDistance = imageGroundCoverList[0]
                            imageGroundCoverArea = imageGroundCoverList[1]

                            # Calculate flight height both relative to ground elevation and mean sea level using the flightHeight function
                            flightHeightList = flightHeight(focalLength, photoScale, elevation)
                            relFlightHeight = flightHeightList[0]
                            geoFlightHeight = "%.2f" % flightHeightList[1]

                            # Calculate the gap between centers of two successive images along one flight line, and gap between centers between two 
                            # neighboring flight lines using the flightGaps function.
                            flightGapsList = flightGaps(imageGroundCoverDistance, endlap, sidelap)
                            airbase = flightGapsList[0]
                            flightLineSpacing = flightGapsList[1]

                            # Calculate the number of flight lines needed to cover the entire surveyed area, number of photographs required for one 
                            # flight line, and for the entire surveted area using the flightLinesAndPhotos function.
                            flightLinesPhotosList = flightLinesAndPhotos(surveyAreaWidth, flightLineSpacing, surveyAreaLength, airbase)
                            totalFlightLines = flightLinesPhotosList[0]
                            photosPerLine = flightLinesPhotosList[1]
                            totalPhotos = flightLinesPhotosList[2]

                            # Prepare parameters for the calculateCoordinates function, and PlotEndPoints function (ArcPy)
                            flightLineLength = airbase * photosPerLine
                            totalEndPoints = totalFlightLines * 2
                            XField = "Easting"
                            YField = "Northing"
                            
                            # # # # # Calculate and export the UTM coordinates of the end points of each flight line to a csv file # # # # # 
                            # Call the calculateCoordinates function to calculate the UTM coordinates for each end points of the flight lines. 
                            # Export the coordinates to a CSV file. No results will be displayed on screen.

                            # # # # # Flight start & end coordinates module starts here # # # # # 
                            outputCoordinates(totalEndPoints, eastingBottomLeft, northingBottomLeft, flightLineSpacing, flightLineLength, flightDirection, XField, YField)
                            print("UTM coordinates of the start and end points of each flight line has been exported.")
                            print("Coordinates saved as CoordinatesData.csv at the same file path containing this python program.")
                            print("*************************************************************************************")
                            # # # # # Flight start & end coordinates module ends here # # # # # 

                            # # # # # ArcPy module starts here # # # # #
                            # Check if the script is run as a standalone program. If yes, proceed with calling the PlotEndPoints function.
                            # the PlotEndPoints function will convert the UTM coordinates into points in ArcGIS project, and export a shapefile.
                            if __name__ == '__main__':
                                # Global Environment settings
                                with arcpy.EnvManager(scratchWorkspace=cwd + r"\Output", workspace=cwd + r"\Output"):

                                    # Define the parameters for the PlotEndPoints function.
                                    coorindatesInput = cwd + r"\CoordinatesData.csv"
                                    pointsOutput = cwd + r"\Output\EndPoint.shp"
                                    coordinateSystem = arcpy.SpatialReference(mapProjection)

                                    # Set the Easting and Northing columns in accordance with CoordinatesData.csv
                                    outputEasting = XField
                                    outputNorthing = YField

                                    # Call the function PlotEndPoints with the above arguments.
                                    PlotEndPoints(coorindatesInput, coordinateSystem, pointsOutput, outputEasting, outputNorthing)

                            # Create an ArcGIS Project object. An ArcGIS Project named AerialSurveyFlightPlan.aprx 
                            # has already been set up in the same file path as this python script.
                            aprx = arcpy.mp.ArcGISProject(cwd + r"\AerialSurveyFlightPlan.aprx")
                            map = aprx.listMaps()[0]

                            # Check if there are existing layers in the map within the ArcGIS Project.
                            # If there are existing layers with the same name as our result point feature layer, remove the existing layer so that 
                            # the map will only have one layer at a time.
                            existingLayer = map.listLayers()
                            for layer in existingLayer:
                                if layer.name == "EndPoint":
                                    map.removeLayer(layer)

                            #Import the resulted shapefile containing the flight end points into the ArcGIS Pro project.
                            pointLayer = map.addDataFromPath(cwd + r"\Output\EndPoint.shp")

                            # Save ArcGIS project
                            aprx.save()

                            # Free up memory
                            del aprx

                            # DISPLAY message to let user know the shapefile for plotted points
                            print("Flight line start and end points have been plotted and save in EndPoint.shp at \Output folder.")
                            print("*************************************************************************************")
                            # # # # # ArcPy module ends here # # # # # 
                            
                            # # # # # Result display starts here # # # # # 
                            print("*************************************************************************************")
                            print("The survey, " + projectTitle + ", will be conducted on " + surveyDate + " by " + surveyorName + ".")
                            #displaying the name date and title of the survey before the resulting height, number of photos and number of laps
                            print ("The required flight height is:", geoFlightHeight, "meters above sea level.")
                            print ("A total of", totalFlightLines, "flight lines are required.") 
                            print ("A total of", totalPhotos, "aerial photographs shall be taken.")
                            print("*************************************************************************************")
                            # # # # # Result display ends here # # # # # 
except ValueError: 
    print("Invalid value input. Please re-run program with valid input.")
    print("*************************************************************************************")
except IndexError:
    print("Please re-run this program and enter Easting and Northing in standard format.")
    print("*************************************************************************************")
except ZeroDivisionError:
    print("Input of zero is not allowed. Please re-run this program with valid values.")
except UnboundLocalError:
    print("Please use standard formating")
    print("*************************************************************************************")
except Exception:
    print("Please re-try.")
    print("*************************************************************************************")
# # # # # Program Ends Here # # # # #

# hidden from output
print("Current working directory is :" + cwd)
print("The ground area coverage of one aerial photo is: " + str("%.2f" % imageGroundCoverArea) + " sqaure meters")
# print("Relative flight height: ", relFlightHeight)
print("Flight height as per mean sea level: ", geoFlightHeight)
print("Airbase: ", airbase)
print("Flight line spacing: ", flightLineSpacing)
print("Total number of flight lines: ", totalFlightLines)
print("Number of photos per line: ", photosPerLine)
print("Total number of photos: ", totalPhotos)