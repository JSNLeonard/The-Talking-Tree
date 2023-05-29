# Name: Jason Leonard

# Project Name: Talking Tree

# File Name: FaceRecognition & Tracking PanTiltHat.py

# File Description: This code is intended to detect and track faces using OpenCV's cascade classifier and a pan-tilt camera connected to a Raspberry Pi.
# ################# It first imports the required libraries, such as OpenCV, Sys, Time, OS, GLOB, PanTiltHat, and FaceRecognition, before configuring the camera driver and frame rate.
# ################# Following that, it sets up variables for the camera's pan and tilt angles, loads the face detection and recognition models, and encodes images.
# ################# It loops indefinitely to detect and track faces by checking the Images folder for new files and reloading images as needed.
# ################# This loop reads a frame from the camera, converts it to grayscale, applies histogram equalisation, and uses the cascade classifier to detect faces.
# ################# It then loops through each detected face, calculates its center, calculates the pan-tilt camera's turn angles, and updates the camera's pan-tilt angles.
# ################# It then limits the pan-tilt angles to 0 to 180 degrees, moves the pan-tilt camera to the new angles, and exits the loop after processing the first detected face.
# ################# It also checks if it has been at least 2 seconds since the faces were recognised and detects known faces in the current frame using the detect_known_faces() method of the FaceRecogniser object that was previously created.
# ################# It assigns the recognised face locations and names to variables and iterates over them using the built-in zip() function.
# ################# Afterwards, it unpacks the face location into four variables (top, right, bottom, and left), and draws the person's recognised name above their face using the OpenCV library's putText() method.

# Importing required libraries such as OpenCV, Sys, Time, OS, GLOB, PanTiltHat, and FaceRecognition.
import cv2, sys, time, os, glob
from pantilthat import *
from FaceRecognition import FaceRecognition

# Enabling the camera driver and setting up the framerate to 60FPS.
os.system('sudo modprobe bcm2835-v4l2')
os.system('v4l2-ctl -p 60')

# Setting the resolution (W = 1920, 1280, 640, 320) (H = 1080, 720, 480, 200).
# Lower resolution = Smoother tracking.
# Higher resolution = More accurate and longer distance tracking.
FRAME_W = 640
FRAME_H = 480

# Initialising variables for pan and tilt angles.
cam_pan = 90
cam_tilt = 90

# Loading the face detection model.
cascPath = '/home/pi/Documents/The-Talking-Tree/lbpcascade_frontalface_improved.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

# Reading a frame from the camera.
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)
time.sleep(2)

# Loading the face recognition model and encoding images.
fr = FaceRecognition()
last_modified_time = os.path.getmtime("Images/")
fr.load_encoding_images("Images/")

# Initialising variables for the face recognition, adding a timer as to when the last time a face was recognised.
last_recognized_time = time.time()
recognized_face_locations = []
recognized_face_names = []

# Looping indefinitely to detect and track faces.
while True:

    # Check for new files added to "Images" folder and reload the images if necessary.
    if last_modified_time != os.path.getmtime("Images/"):
        fr.load_encoding_images("Images/")
        last_modified_time = os.path.getmtime("Images/")

    # Reads the camera capture and then flips the camera feed.
    ret, frame1 = cap.read()
    frame1 = cv2.flip(frame1, -1)

    # Checking if the frame was captured successfully.
    if ret == False:
        print("Error Obtaining Image")
        continue

    # Converting the frame to grayscale and performing histogram equalisation.
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Detecting faces in the grayscale frame using the cascade classifier.
    faces = faceCascade.detectMultiScale(frame1, 1.1, 3, 0, (10, 10))

    # Check if it's been at least 2 seconds since the last time the faces were recognised.
    if time.time() - last_recognized_time >= 2:

        # Detects the known faces in the current frame using the detect_known_faces() method of the fr object (which is a FaceRecogniser object created earlier).
        face_locations, face_names = fr.detect_known_faces(frame1)

        # Assigns the recognised face locations to a variable called recognized_face_locations.
        recognized_face_locations = face_locations

        # Assigns the recognised face names to a variable called recognized_face_names.
        recognized_face_names = face_names

        # Updates the value of last_recognized_time to the current time.
        last_recognized_time = time.time()

    # Iterates over the recognised face locations and names using the built-in zip() function.
    for face_loc, name in zip(recognized_face_locations, recognized_face_names):

        # Unpacks the face location into 4 variables (top, right, bottom, left).
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        # Draws the recognised name of the person above their face using the putText() method of the OpenCV library.
        cv2.putText(frame1, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)

        # Draws a rectangle around the recognised face using the rectangle() method of the OpenCV library.
        cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 0, 200), 4)
    
    # Looping through each face detected.
    for (x, y, w, h) in faces:

        # Drawing a rectangle around the face.
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 4)

        # Calculating the center of the face.
        x = x + (w/2)
        y = y + (h/2)

        # Calculating the turn angles for the pan-tilt camera.
        turn_x = float(x - (FRAME_W/2))
        turn_y = float(y - (FRAME_H/2))
        turn_x /= float(FRAME_W/2)
        turn_y /= float(FRAME_H/2)

        # Update the camera pan-tilt angles these values can be adjusted to smooth out or speed up the camera's speed.
        turn_x *= 2.5
        turn_y *= 2.5
        cam_pan += -turn_x
        cam_tilt += turn_y

        # Printing off the angle of the pan and tilt.
        print(cam_pan-90, cam_tilt-90)

        # Limit the pan-tilt angles within the allowed range (0 to 180 degrees).
        cam_pan = max(0, min(180, cam_pan))
        cam_tilt = max(0, min(180, cam_tilt))

        # Move the pan-tilt camera to the new angles.
        pan(int(cam_pan-90))
        tilt(int(cam_tilt-90))

        # Break out of the loop after processing the first detected face.
        break

    # Displays the current frame with recognised faces and names in a window titled "Face Tracking & Face Recognition".
    cv2.imshow("Face Tracking & Face Recognition", frame1)

    # Waits for a key press and checks if it's the 'q' key.
    if cv2.waitKey(1) == ord('q'):
        # Breaks out of the loop if the 'q' key was pressed.
        break

# Releases the video capture object created earlier.
video_capture.release()

# Destroys all windows created by OpenCV.
cv2.destroyAllWindows()