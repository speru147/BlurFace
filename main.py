# Import required libraries
import cv2
import os
import numpy as np 

# Define the path to the input image
image_path = os.path.join('face.jpg')
# Read the image using OpenCV
img_face = cv2.imread(image_path)

# Convert image to grayscale for better face detection
# Face detection algorithm works better with grayscale images
frame_gray = cv2.cvtColor(img_face, cv2.COLOR_BGR2GRAY)

# Load pre-trained Haar Cascade classifier for face detection
# This XML file contains the trained model for frontal face detection
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# Normalize the image histogram to improve contrast
# This helps with face detection across different lighting conditions
frame_gray = cv2.equalizeHist(frame_gray)

# Detect faces in the image
# Returns a list of (x, y, width, height) tuples for each detected face
faces = face_classifier.detectMultiScale(frame_gray)

# Process each detected face
for (x,y,w,h) in faces:
    # Draw a blue rectangle around the detected face
    face_frame = cv2.rectangle(img_face, (x, y), (x+w, y+h), (255, 0, 0), 4)
    # Extract the region of interest (ROI) containing the face
    faceROI = face_frame[y:y+h,x:x+w]

    kSize = 15
    # Apply Gaussian blur to the face region
    img_blur = cv2.blur(faceROI, (kSize, kSize))
    # Replace the original face region with the blurred version
    face_frame[y:y+h,x:x+w] = img_blur

cv2.imshow('face_frame', face_frame)
cv2.waitKey(0)