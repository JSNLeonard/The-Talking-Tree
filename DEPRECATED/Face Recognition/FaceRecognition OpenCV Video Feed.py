# Import the OpenCV library and the FaceRecognition module.
import cv2
from FaceRecognition import FaceRecognition
import time

# Create an instance of FaceRecognition for encoding and recognizing faces.
fr = FaceRecognition()

# Load pre-encoded face images from a folder.
fr.load_encoding_images("Images/")

# Initialize the camera for capturing video.
cap = cv2.VideoCapture(0)

# Keep track of the last time the images were loaded.
last_loaded_time = time.time()

# Loop to read frames from the camera and detect faces in them.
while True:
    # Read a frame from the camera.
    ret, frame = cap.read()
    
    # Use the FaceRecognition instance to detect known faces in the frame.
    face_locations, face_names = fr.detect_known_faces(frame)
    
    # Loop over the detected faces and draw a rectangle and name label around them.
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    
    # Show the frame in a window called "Frame".
    cv2.imshow("Face Recognition", frame)
    
    # Check if it's time to reload the images.
    if time.time() - last_loaded_time >= 60:
        fr.load_encoding_images("images/")
        last_loaded_time = time.time()
    
    # Wait for a key press and check if it's the "Esc" key (code 27).
    key = cv2.waitKey(1)
    if key == 27:
        break
    
# Release the camera and close all windows.
cap.release()
cv2.destroyAllWindows()