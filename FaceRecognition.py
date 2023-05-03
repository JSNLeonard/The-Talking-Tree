# Import the OpenCV, Face Recognition, OS, GLOB and Numpy library.
import face_recognition
import cv2
import os
import glob
import numpy as np

# Initialisation of the FaceRecognition class which is used in other Python programs within this project.
class FaceRecognition:
    def __init__(self):
        
        # Initialize empty lists for storing face encodings and names.
        self.known_face_encodings = []
        self.known_face_names = []
        
        # Resize frame for a faster speed.
        self.frame_resizing = 0.25
        
    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path: path to the folder containing the encoding images
        """
        
        # Load Images.
        images_path = glob.glob(os.path.join(images_path, "*.*"))        
        print("{} Encoding Images Found".format(len(images_path)))
        
        # Store image encoding and names.
        for img_path in images_path:
            
            # Read image from path.
            img = cv2.imread(img_path)
            
            # Convert BGR color (used by OpenCV) to RGB color (used by face_recognition).
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            
            # Get encoding.
            img_encoding = face_recognition.face_encodings(rgb_img)[0]
            
            # Store file name and file encoding.
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        
        # Prints off Encoding Images Loaded
        print("Encoding Images Loaded")
        
    def detect_known_faces(self, frame):
        
        # Resize the frame for a faster processing speed.
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        
        # Convert BGR color (used by OpenCV) to RGB color (used by face_recognition).
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        # Find all the faces and face encodings in the current frame of video.
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            
            # See if the face is a match for the known face(s).
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            
            # Use the known face with the smallest distance to the new face.
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)
            
        # Convert to numpy array to adjust coordinates with frame resizing quickly.
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names