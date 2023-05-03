# Import the OpenCV, System, Time, OS & FaceRecognition Modules/Libraries.
import cv2
import sys
import time
import os
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
last_modified_time = os.path.getmtime("Images/")
fr.load_encoding_images("Images/")

# Keep track of the last time a face was recognized.
last_recognized_time = time.time()

# Keep track of the recognized faces and their locations.
recognized_face_locations = []
recognized_face_names = []

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

    # If it's been 2 seconds since the last recognition, perform face recognition on the current frame.
    if time.time() - last_recognized_time >= 2:
        # Use the FaceRecognition instance to detect known faces in the frame.
        face_locations, face_names = fr.detect_known_faces(frame1)

        # Update the recognized face locations and names.
        recognized_face_locations = face_locations
        recognized_face_names = face_names

        # Update the time of the last recognition.
        last_recognized_time = time.time()

    # Draw rectangles and labels around the recognized faces.
    for face_loc, name in zip(recognized_face_locations, recognized_face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame1, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 0, 200), 4)

    # Display the resulting frame in a window.
    cv2.imshow('Face Tracking & Recognition', frame1)

    # Check if there are any new images in the "Images/" folder.
    current_modified_time = os.path.getmtime("Images/")
    if current_modified_time > last_modified_time:
        # If the folder has been modified since the last check, reload the pre-encoded face images.
        fr.load_encoding_images("Images/")
        last_modified_time = current_modified_time

    # Exit program if 'q' key is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and destroy all windows.
cap.release()
cv2.destroyAllWindows()