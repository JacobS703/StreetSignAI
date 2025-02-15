# Import Libs

import cv2
import pytesseract

# Setup Camera IO
vid = cv2.VideoCapture(0)
ret, frame = vid.read()

# Take Photo and save to disk
cv2.imwrite("/Users/jacob/Desktop/Code_Stuff/Projects/Google/Photos/1.png", frame)
image = cv2.imread('Photos/1.png')

# Pre-Process Image
thresh = cv2.inRange(image, (200,200,200),(255,255,255))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = opening

# Preform OCR
text = pytesseract.image_to_string(invert, lang='eng', config="--psm 11")

# Display Image
cv2.imshow('0', image)

# Display B/W Image, w/ Thresh Param 1
cv2.imshow('1', thresh)

# Further Processing
thresh = cv2.inRange(image, (0,0,0),(60,60,60))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
text = text+pytesseract.image_to_string(opening, lang='eng', config="--psm 11")
text = text+pytesseract.image_to_string(opening, lang='eng', config="--psm 6")

# Print Recognized Streets to Console
print(text)

# Display B/W Image, w/ Thresh Param 2
cv2.imshow('3', thresh)

# Debug
#cv2.imshow('4', kernel)
#cv2.imshow('5', opening)
#cv2.imshow('6', invert)

# Process Text
index = text.replace("\n","")
index = index.split(None)

street = ""
sign = 0
direction = ""

# Detect & Interpret Sinage

for i in range(0,len(index)):
    #print(index[0])
    #print(index[1])
    if index [i] == "South":
        direction = "S"
    if index [i] == "S":
        direction = "S"
    
    if index [i] == "North":
        direction = "N"
    if index [i] == "N":
        direction = "N"

    if index [i] == "East":
        direction = "E"
    if index [i] == "E":
        direction = "E"

    if index [i] == "West":
        direction = "W"
    if index [i] == "W":
        direction = "W"
    
    if index[i] == "st":
        street = direction+index[i-1]+" st"
        sign = 1
    if index[i] == "street":
        street = direction+index[i-1]+" st"
        sign = 1
    if index[i] == "rd":
        street = direction+index[i-1]+" rd"
        sign = 1
    if index[i] == "road":
        street = direction+index[i-1]+" rd"
        sign = 1
    if index[i] == "dr":
        street = direction+index[i-1]+" dr"
        sign = 1
    if index[i] == "drive":
        street = direction+index[i-1]+" dr"
        sign = 1
    if index[i] == "blvd":
        street = direction+index[i-1]+" blvd"
        sign = 1
    if index[i] == "boulevard":
        street = direction+index[i-1]+" blvd"
        sign = 1

# Raise Errors
if sign == 0:
    print("No Sign Found")
else:
    print("Sign Found!")
    print("Location:\t"+street)

# Declare Vars
Time = ""
Clock = False
index = text.split()

# Identify Text Matching 12 Hour Time And Seperate Values
for i in range(len(index)):
    if index[i].find(":") != -1:
        index2 = index[i]
        index2 = index2.split(":")
        #print(index2)
        Time=[index2[0],index2[1]]
        Clock=True

# Raise Errors
if Clock == False:
    print("No Time Found")
# Print Time To Console
else:
    print("Time Found!")
    print("Hour:\t\t"+Time[0])
    print("Minute:\t\t"+Time[1])


    


cv2.waitKey(0)