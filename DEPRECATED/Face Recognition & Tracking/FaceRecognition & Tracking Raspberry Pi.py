# Import the OpenCV, System, Time, & FaceRecognition Modules/Libraries.
import cv2
import sys
import time
from FaceRecognition import FaceRecognition

# Frame size.
FRAME_W = 640
FRAME_H = 480

# Cascade Classifier for face tracking.
cascPath = '/home/pi/Documents/The-Talking-Tree/lbpcascade_frontalface_improved.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

# Start video capture.
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
time.sleep(2)

# Create an instance of FaceRecognition for encoding and recognizing faces.
fr = FaceRecognition()

# Load pre-encoded face images from a folder.
fr.load_encoding_images("Images/")

# Keep track of the last time the images were loaded.
last_loaded_time = time.time()

while True:
    # Capture frame-by-frame for face tracking.
    ret, frame1 = cap.read()

    # Convert to grayscale.
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Do face detection.
    faces = faceCascade.detectMultiScale(frame1, 1.1, 3, 0, (10, 10))

    # Draw rectangles around faces for face tracking.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Use the FaceRecognition instance to detect known faces in the frame.
    ret, frame2 = cap.read()
    face_locations, face_names = fr.detect_known_faces(frame2)

    # Loop over the detected faces and draw a rectangle and name label around them.
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame2, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame2, (x1, y1), (x2, y2), (0, 0, 200), 4)

    # Display the resulting frames in two separate windows.
    cv2.imshow('Face Tracking', frame1)
    cv2.imshow("Face Recognition", frame2)

    # Check if it's time to reload the images for face recognition.
    if time.time() - last_loaded_time >= 60:
        fr.load_encoding_images("images/")
        last_loaded_time = time.time()

    # Wait for a key press and check if it's the "Esc" key (code 27).
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the capture and clean up.
cap.release()
cv2.destroyAllWindows()