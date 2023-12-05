# Test values
# Determine from previous sections
flightDirection = "StoN"
originEasting = 709519.558                              # Change to variable name when merged
originNorthing = 4904884.260                            # Change to variable name when merged
flightLineSpacing = 80                                  # Change to variable name when merged
flightLineLength = 750                                  # Change to variable name when merged
numberOfFlightLines = 20                                # Change to variable name when merged
numberOfEndPoints = numberOfFlightLines * 2

import csv

# Define function
# # # # # # # # # # # numberOfEndPoints, flightLineSpacing, flightLineLength, flightDirection, originEasting, originNorthing
def calculateCoordinates(endPointsTotal, firstEasting, firstNorthing, flightLineGap, flightLineDistance, flightRoute):

    # Set up a new CoordinatesData.csv file for exporting the UTM coordinates of each end point
    outputCSV = "CoordinatesData.csv"
    databaseCSV = open(outputCSV, "w", newline="")
    databasewriter = csv.writer(databaseCSV)

    # Set the field (column) names
    field_X = "Easting"
    field_Y = "Northing"
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
            coordinatesList.append(ptEasting)
            coordinatesList.append(ptNorthing)

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

    # # Close the CoordinatesData.csv file after writing all flightPoint information
    databaseCSV.close()

# Call the calculateCoordinates function
calculateCoordinates(numberOfEndPoints, originEasting, originNorthing, flightLineSpacing, flightLineLength, flightDirection)
