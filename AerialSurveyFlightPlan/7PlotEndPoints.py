# Get UTM zone number of the surveyed area from user
UTMzone = input("Please enter the WGS 1984 UTM zone of the surveyed area, e.g. 17N: ")
UTMZONE = UTMzone.upper()

# Check if the user entered a valid UTM zone number. The numeric value must be between 1 and 60, and the character must
# be either N (Northern Hemisphere) or S (Southern Hemisphere). Prompt message to user and terminate program if the UTM
# zone is invalid.
try:
    zoneNumber = int(UTMZONE[:-1])
    hemisphere = UTMZONE[-1]
    if zoneNumber in range(1, 61) and hemisphere in "NS":
        # Record the UTM zone for use in plotting end points at a later section
        mapProjection = "WGS_1984_UTM_Zone_" + UTMZONE
        print("The UTM zone is " + UTMZONE + ".")
    else:
        print("Invalid UTM zone input.")
except ValueError:
    print("Invalid UTM zon input. Please provide a valdie numberic UTM zone number followed by N or S")

# # # # # # # # # # # # # # #　

import arcpy
import os

# Get current working directory
cwd = os.getcwd()
print("Current working directory is :" + cwd) # do not show in final product; just for test

# Set up workspace
myWorkspace = cwd + r"\AerialSurveyFlightPlan.gdb"
arcpy.env.workspace = myWorkspace

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

# Check if the script is run as a standalone program. If yes, proceed with the subsequent lines. 
if __name__ == '__main__':

    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=cwd + r"\Output", workspace=cwd + r"\Output"):

        # Define the parameters for the PlotEndPoints function.
        coorindatesInput = cwd + r"\CoordinatesData.csv"                # Change to outputCSV when combined with CalculateCoordinates
        pointsOutput = cwd + r"\Output\EndPoint.shp"
        coordinateSystem = arcpy.SpatialReference(mapProjection)

        # Set the Easting and Northing columns in accordance with CoordinatesData.csv
        outputEasting = "Easting"                                       # Change to field_X when merged with CalculateCoordinates
        outputNorthing = "Northing"                                     # Change to field_Y when merged with CalculateCoordinates

        # Call the function PlotEndPoints with the above arguments.
        PlotEndPoints(coorindatesInput, coordinateSystem, pointsOutput, outputEasting, outputNorthing)

# Create the ArcGIS Project object
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
aprx.save()                                                             # May change to saveACopy

# Free up memory
del aprx