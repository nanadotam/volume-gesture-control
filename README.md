# Hand Tracking Volume Control

## Overview

This project leverages computer vision to control the system volume using hand gestures. It utilizes the Mediapipe library for hand tracking and OpenCV for video capture and display. The system captures hand movements to adjust the volume level on macOS in real-time.

## Features

- **Real-time Hand Tracking:** Detects and tracks hand landmarks using Mediapipe.
- **Volume Control:** Maps the distance between thumb and index finger to control the system volume.
- **Visual Feedback:** Displays the volume level and frame rate on the video feed.

## Requirements

- Python 3.6+
- OpenCV
- Mediapipe
- NumPy

You can install the required Python packages using pip:

```bash
pip install opencv-python mediapipe numpy
```

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nanadotam/hand-tracking-volume-control.git
   cd hand-tracking-volume-control
   ```

2. **Run the script:**

   Make sure your camera is connected and recognized by the system. Then, execute the following command:

   ```bash
   python volume_control.py
   ```

3. **Adjust System Volume:**

   - Position your hand in front of the camera.
   - Move your thumb and index finger apart or together to increase or decrease the volume, respectively.
   - The system volume is updated in real-time based on the distance between your thumb and index finger.

4. **Exit the Program:**

   Press `q` while the video window is focused to exit the program.

## Code Explanation

- **`volume_control.py`:** The main script that captures video, processes hand gestures, and controls the volume.
- **`HandTrackingModule.py`:** Contains the `HandDetector` class for hand tracking and landmark detection.

### `volume_control.py`

This script captures video from the camera, detects hand gestures, calculates the distance between the thumb and index finger, and adjusts the system volume accordingly. It also displays a visual representation of the volume level and frame rate.

### `HandTrackingModule.py`

Defines the `HandDetector` class for hand detection and tracking using Mediapipe. The class includes methods to find hands and landmarks and to list working cameras.

## Troubleshooting

- **Camera Not Detected:** Ensure that your camera is properly connected and recognized by the system. You can use the `list_working_cameras` function to check for available cameras.
- **Volume Control Not Working:** Make sure you have the correct permissions to change system volume and that your system is running macOS.
