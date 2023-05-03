# Importing the OpenCV, Sys, and Time libraries.
import cv2
import sys
import time

# Frame size.
FRAME_W = 320
FRAME_H = 200

# Cascade Classifier for face tracking.
cascPath = 'C:/Users/Jason/Documents/College Year 4/Semester 2/Final Year Project/The-Talking-Tree/lbpcascade_frontalface_improved.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

# Start video capture.
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
time.sleep(2)

while True:
    # Capture frame-by-frame.
    ret, frame = cap.read()
    
    if ret == False:
        print("Error getting image")
        continue

    # Convert to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Do face detection.
    faces = faceCascade.detectMultiScale(frame, 1.1, 3, 0, (10, 10))
    
    # Draw rectangles around faces.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame.
    cv2.imshow('Face Tracking Windows',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and clean up.
cap.release()
cv2.destroyAllWindows()