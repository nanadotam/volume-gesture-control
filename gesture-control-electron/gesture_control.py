import cv2
import mediapipe as mp
import time
import numpy as np
import math
import os

try:
    import HandTrackingModule as htm
    print("Modules imported successfully")
except ImportError as e:
    print(f"Error importing modules: {e}")
    exit(1)

# Width and height of the camera window (for internal use)
wCam, hCam = 1280, 480

# Open the video capture device
cap = cv2.VideoCapture(1)

# Set the width and height of the capture device
cap.set(3, wCam)
cap.set(4, hCam)

# Create an instance of the HandDetector class from the HandTrackingModule
detector = htm.HandDetector(detectionCon=0.8)

# Volume control variables
volPer = 0

def set_volume(volume_level):
    """
    Sets the system volume on macOS using osascript.
    
    Args:
        volume_level (int): The volume level (0-100).
    """
    os.system(f"osascript -e 'set volume output volume {volume_level}'")

# Run the main loop
while True:
    try:
        success, img = cap.read()
        if not success:
            print("Failed to capture image")
            break
        
        # Mirror the image horizontally
        img = cv2.flip(img, 1)
        
        # Find hands and draw landmarks on the image
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        if len(lmList) != 0:
            # Get the x and y coordinates of landmarks 4 and 8
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]

            # Calculate the distance between thumb and index finger
            length = math.hypot(x2 - x1, y2 - y1)

            # Map the distance to volume percentage
            volPer = np.interp(length, [50, 300], [0, 100])
            
            # Set the volume based on the length
            set_volume(volPer)

            # Send the volume to the Electron app
            print(f'{int(volPer)}')

    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Release the capture device
cap.release()
