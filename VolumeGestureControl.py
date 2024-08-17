import cv2
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm

# Width of camera window
wCam, hCam = 1280, 480

cap = cv2.VideoCapture(2)

cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.HandDetector()

# Variables to calculate FPS
pTime = 0
cTime = 0

# Run
while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    
    # Mirror image
    img = cv2.flip(img, 1)

    # Find hands and draw landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    # if len(lmList) != 0:
        # print(lmList)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display FPS on image
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 
                3, (0, 255, 0), 3)

    # Display the image with hand landmarks
    cv2.imshow("Image", img)

    # Quit program on keypress 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
