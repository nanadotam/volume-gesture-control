"""
Minimum code required to do hand tracking. program using the Mediapipe library and OpenCV to perform gesture 
control using hand tracking.
"""

import cv2
import mediapipe as mp
import time

"""
Lists the indices of working cameras.

Args:
    max_cameras (int, optional): The maximum number of cameras to check. Defaults to 5.

Returns:
    list: A list of indices of working cameras.
"""
# def list_working_cameras(max_cameras=5):
#     available_cameras = []
#     for index in range(max_cameras):
#         cap = cv2.VideoCapture(index)
#         if cap.isOpened():
#             ret, _ = cap.read()
#             if ret:
#                 print(f"Camera {index} is working")
#                 available_cameras.append(index)
#             cap.release()
#     return available_cameras

# working_cameras = list_working_cameras()

# if not working_cameras:
#     print("No working cameras found.")
# else:
#     print(f"Working cameras: {working_cameras}")


# Working cameras: 2 (FaceTime HD Cam)
# Working cameras: 1 (iPhone Cam)
# Working cameras: 0 (OBS)
cap = cv2.VideoCapture(2)

# Initialize Mediapipe hands module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils    

# Variables to calculate FPS
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    
    # Mirror image
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    # Check if there are multiple hand landmarks detected
    if results.multi_hand_landmarks:
        # Iterate through each hand landmark
        for handLms in results.multi_hand_landmarks:
            # Draw landmarks and connections on the image
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
            # Extract information for each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                
                # Highlight the first landmark with a circle
                if id == 0:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
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
