import tkinter as tk
from tkinter import messagebox
import cv2
import threading
import time
import numpy as np
import math
import os
import HandTrackingModule as htm

class GestureControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gesture Volume Control")
        self.root.geometry("400x300")
        
        self.running = False

        self.start_button = tk.Button(root, text="Start", command=self.start_control)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_control, state=tk.DISABLED)
        self.stop_button.pack(pady=20)

        self.volume_label = tk.Label(root, text="Volume: 50%", font=("Helvetica", 16))
        self.volume_label.pack(pady=20)

        self.status_label = tk.Label(root, text="Status: Idle", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        self.volume = 50  # Default volume level

    def start_control(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Running")
        threading.Thread(target=self.gesture_control_loop).start()

    def stop_control(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Stopped")

    def gesture_control_loop(self):
        # Initialize gesture control components
        wCam, hCam = 640, 480
        cap = cv2.VideoCapture(1)
        cap.set(3, wCam)
        cap.set(4, hCam)
        detector = htm.HandDetector(detectionCon=0.8)
        previous_angle = 0

        while self.running:
            success, img = cap.read()
            if not success:
                break
            
            img = cv2.flip(img, 1)
            img = detector.findHands(img)
            lmList = detector.findPosition(img)

            if len(lmList) != 0:
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
                angle_difference = angle - previous_angle
                
                if abs(angle_difference) > 10:  # Adjust threshold as needed
                    if angle_difference > 0:
                        self.volume = min(100, self.volume + 2)
                    else:
                        self.volume = max(0, self.volume - 2)
                    
                    self.update_volume_display()
                    self.set_volume(self.volume)

                previous_angle = angle

            # Slow down the loop to avoid excessive CPU usage
            time.sleep(0.05)

        cap.release()

    def set_volume(self, volume_level):
        os.system(f"osascript -e 'set volume output volume {volume_level}'")

    def update_volume_display(self):
        self.volume_label.config(text=f"Volume: {self.volume}%")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GestureControlApp(root)
    root.mainloop()
