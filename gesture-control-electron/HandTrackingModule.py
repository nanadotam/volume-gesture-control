"""
Title: HandTrackingModule
By: Nana Amoako
About: Simple program using the Mediapipe library and OpenCV to perform gesture 
control using hand tracking.
"""

import cv2
import mediapipe as mp
import time

class HandDetector:
    """
    Initializes the HandTrackingModule.

    Args:
        mode (bool, optional): The mode of the HandTrackingModule. Defaults to False.
        maxHands (int, optional): The maximum number of hands to detect. Defaults to 2.
        detectionCon (float, optional): The minimum confidence for hand detection. Defaults to 0.5.
        trackCon (float, optional): The minimum confidence for hand tracking. Defaults to 0.5.

    Returns: 
        None
    """
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # Initialize Mediapipe hands module
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, 
                                        min_detection_confidence=self.detectionCon, 
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.results = None  # Initialize the results attribute

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)  # Store the results

        # Check if there are multiple hand landmarks detected
        if self.results.multi_hand_landmarks:
            # Iterate through each hand landmark
            for handLms in self.results.multi_hand_landmarks:
                # Draw landmarks and connections on the image
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results and self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
        return lmList 

def list_working_cameras(max_cameras=5):
    """
    Lists the indices of working cameras.

    Args:
        max_cameras (int, optional): The maximum number of cameras to check. Defaults to 5.

    Returns:
        list: A list of indices of working cameras.
    """
    available_cameras = []
    for index in range(max_cameras):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            ret, _ = cap.read()
            if ret:
                print(f"Camera {index} is working")
                available_cameras.append(index)
            cap.release()
    return available_cameras

def main():
    cap = cv2.VideoCapture(2)  # Use the correct index for your camera

    # Initialize HandDetector
    detector = HandDetector()

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

if __name__ == "__main__":
    main()
