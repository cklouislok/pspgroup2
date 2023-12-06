



import math

### SET sensorLength and focalLength = constant
# Define camera sensor length and width (in mm)
# Camera sensor size = 24 mm × 24 mm, which is the maximum 1:1 size of a full frame sensor. Note: a standard 35 mm full frame sensor has dimensions of 36 mm × 24 mm.
sensorLength=24  #in mm
# Define camera lens focal length (in mm)
# Focal length of camera lens = 152 mm, typically used for aerial photogrammetry suggested by NRCan and USGS. (NRCan source: https://natural-resources.canada.ca/maps-tools-and-publications/satellite-imagery-and-air-photos/tutorial-fundamentals-remote-sensing/satellites-and-sensors/cameras-and-aerial-photography/9351. USGS source: https://www.usgs.gov/faqs/how-much-area-does-aerial-photograph-cover. )
focalLength = 152 #in mm
def(sensor_focal):
 sensor_focal.sensorlength=sensor_focal.sensorLength
 sensor_focal.focallength=sensor_focal.focalLength

### DISPLAY program’s purpose
# Display program's purpose
 programPurpose = "This program is developed to resolve the problem of incomplete data collection aerial surveys and produce an explicit flight plan for surveyors to follow. It focuses on aerial photogrammetry by Unmanned Aerial Vehicles (UAVs), in particular rotary-wing UAVs, in combination with an aircraft-hinged camera. The primary output of the program are the aircraft flying height, number of flight lines, minimum number of aerial photographs, as well as the start and end coordinates of each flight line, so that users can follow the programmed flight plan to accurately survey and measure the terrain."
 print(programPurpose)


### DISPLAY programmer-defined values of camera sensor length and lens focal length using List
 cameraSettings = [sensor_focal.sensorLength,sensor_focal.focalLength]
 print("Programmer-defined sensor length and focal length:", cameraSettings)

### DISPLAY a prompt message for input
### GET flight project title, date, and surveyor’s name
 projectTitle = input("Please enter the project title: ")
 planDate = input("Please enter the flight planning date: ")
 surveyorName = input("Please enter the name of the surveyor: ")

### DISPLAY a prompt message for input
### GET UTM easting and northing of bottom left corner of the surveyed area
# Lower left corner of the surveyed area
 bottomLeftUTM = input("Please enter the Easting and Northing of the bottom left corner of the surveyed are in UTM format (XXXXXX.XX, YYYYYYY.YY): ")
 eastingString, northingString = str[[start] [:] [end]]

### STRING MANIPULATION to store easting and northing of bottom left corner separately
eastingLeft = eastingString[[start][:][end]]
northingLeft = northingString[[start][:][end]]

print("the easting of the bottom left corner=",eastingLeft)
print("the northing of the bottom left corner= ",northingLeft)

### DISPLAY a prompt message for input
### GET UTM easting and northing of top right corner of the surveyed area
# Top right corner of the surveyed area
topRightUTM = input("Please enter the Easting and Northing of the top right corner of the surveyed are in UTM format (XXXXXX.XX, YYYYYYY.YY): ")
eastingString, northingString = str[[start] [:] [end]]

### STRING MANIPULATION to store easting and northing of top right corner separately
eastingRight=eastingString[[start][:][end]]
northingRight=northingString[[start][:][end]]

print ("the easting of the bottom right corner=",eastingRight)
print("the northing of the bottom r corner= ",northingRight)






