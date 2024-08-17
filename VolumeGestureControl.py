import cv2
import mediapipe as mp
import time
import numpy as np
import math
import HandTrackingModule as htm

# Width and height of the camera window
wCam, hCam = 1280, 480

# Open the video capture device
cap = cv2.VideoCapture(1)

# Set the width and height of the capture device
cap.set(3, wCam)
cap.set(4, hCam)

# Create an instance of the HandDetector class from the HandTrackingModule
detector = htm.HandDetector(detectionCon=0.8)

# Variables to calculate FPS
pTime = 0
cTime = 0

# Run the main loop
while True:
    # Read a frame from the capture device
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
        # Print the coordinates of specific landmarks
        # print(lmList[4], lmList[8])

        # Get the x and y coordinates of specific landmarks
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Draw circles at the specified landmarks
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)  # Circle at landmark 4
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)  # Circle at landmark 8
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)  # Line connecting landmarks 4 and 8
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)  # Circle at the center of landmarks 4 and 8


        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)  # Circle at the center of landmarks 4 and 8



    # Calculate the FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display the FPS on the image
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 
                3, (0, 255, 0), 3)

    # Display the image with hand landmarks
    cv2.imshow("Image", img)

    # Quit the program on keypress 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture device and destroy all windows
cap.release()
cv2.destroyAllWindows()
